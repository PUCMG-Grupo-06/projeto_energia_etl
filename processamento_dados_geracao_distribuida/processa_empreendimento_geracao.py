from datetime import date, datetime
from modelo_empreendimentos_geracao import ModeloEmpreendimentosGeracao, ProducaoMensal

import csv
import os
import sys


bd_producao = dict()

dt_inicio = datetime(1960, 1, 1, 0, 0, 0)
dt_fim = datetime(2022, 4, 30, 0, 0, 0)


class ProcessaDadosEmpreendimentosGeracao:
    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo

    def _get_proximo_mes_ano(self, data):
        vira_ano = False
        mes = data.month + 1
        if mes > 12:
            mes = 1
            vira_ano = True

        ano = data.year if not vira_ano else data.year + 1
        if datetime(ano, mes, 1, 0, 0, 0) > dt_fim:
            return None, None
        return ano, mes

    def gera_relatorio(self, conteudo_csv):
        for item in conteudo_csv:
            ano_corrente = item.data_base_inicio_contagem.year
            mes_corrente = item.data_base_inicio_contagem.month

            while True:
                data_corrente = datetime(ano_corrente, mes_corrente, 1, 0, 0, 0)
                if ano_corrente is None or mes_corrente is None:
                    break

                uf = item.uf_principal
                combustivel = item.tipo_combustivel

                if ano_corrente not in bd_producao:
                    bd_producao[ano_corrente]
                if mes_corrente not in bd_producao[ano_corrente]:
                    bd_producao[ano_corrente][mes_corrente] = dict()

                if item.uf_principal not in bd_producao[ano_corrente][mes_corrente]:
                    bd_producao[ano_corrente][mes_corrente][uf] = dict()
                if combustivel not in bd_producao[ano][mes][uf]:
                    bd_producao[ano_corrente][mes_corrente][uf][combustivel] = None

                if bd_producao[ano_corrente][mes_corrente][uf][combustivel] is None:
                    pm = ProducaoMensal(mes_corrente, ano_corrente, uf, combustivel, item.potencia_operacao)
                    bd_producao[ano_corrente][mes_corrente][uf][combustivel] = pm
                else:
                    bd_producao[ano_corrente][mes_corrente][uf][combustivel].energia_produzida += \
                        item.potencia_operacao

                ano_corrente, mes_corrente = self._get_proximo_mes_ano(data_corrente)

    def executa(self):
        conteudo_csv = []
        with open(self.caminho_arquivo, 'r', encoding='utf-16') as arquivo:
            arquivo_csv = csv.reader(arquivo, delimiter=';')
            for i, linha in enumerate(arquivo_csv):
                if i == 0:
                    # Linha de cabeçalho. Passo reto.
                    continue
                modelo_geracao = ModeloEmpreendimentosGeracao.from_linha_csv(linha)
                modelo_geracao.processa()
                conteudo_csv.append(modelo_geracao)

        self.gera_relatorio(conteudo_csv)


if __name__ == '__main__':
    if isinstance(sys.argv[1], list):
        file_path = sys.argv[1][0]
    else:
        file_path = sys.argv[1]

    print(f'sys.argv: {sys.argv}')
    processador = ProcessaDadosEmpreendimentosGeracao(file_path)
    processador.executa()
