from datetime import date, datetime
from modelo_empreendimentos_geracao import ModeloEmpreendimentosGeracao, ProducaoMensal

import csv
import os
import sys


bd_producao = dict()
bd_sem_dict = []

dt_inicio = datetime(1960, 1, 1, 0, 0, 0)
dt_fim = datetime(2022, 4, 30, 0, 0, 0)

csv_file_result = 'Consumo.csv'
sql_file_result = 'Consumo.sql'


class ProcessaDadosEmpreendimentosGeracao:
    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo
        self.contador_erros = 0

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

            if item.registro_com_erro:
                self.contador_erros += 1
                continue

            while True:
                if ano_corrente is None or mes_corrente is None:
                    break

                data_corrente = datetime(ano_corrente, mes_corrente, 1, 0, 0, 0)
                uf = item.uf_principal
                combustivel = item.tipo_combustivel

                if ano_corrente not in bd_producao:
                    bd_producao[ano_corrente] = dict()
                if mes_corrente not in bd_producao[ano_corrente]:
                    bd_producao[ano_corrente][mes_corrente] = dict()

                if item.uf_principal not in bd_producao[ano_corrente][mes_corrente]:
                    bd_producao[ano_corrente][mes_corrente][uf] = dict()
                if combustivel not in bd_producao[ano_corrente][mes_corrente][uf]:
                    bd_producao[ano_corrente][mes_corrente][uf][combustivel] = {'dados': None}

                if bd_producao[ano_corrente][mes_corrente][uf][combustivel]['dados'] is None:
                    data_referencia = datetime(ano_corrente, mes_corrente, 1, 0, 0, 0).date()
                    pm = ProducaoMensal(
                        mes=mes_corrente, ano=ano_corrente,
                        data_referencia=data_referencia,
                        uf=uf,
                        tipo_combustivel=combustivel,
                        energia_produzida=item.potencia_operacao)
                    bd_producao[ano_corrente][mes_corrente][uf][combustivel]['dados'] = pm
                else:
                    bd_producao[ano_corrente][mes_corrente][uf][combustivel]['dados'].energia_produzida += \
                        item.potencia_operacao

                ano_corrente, mes_corrente = self._get_proximo_mes_ano(data_corrente)
        self._monta_bd_sem_dict()

    def _monta_bd_sem_dict(self):
        # Separando os objetos:
        for ano in bd_producao.keys():
            for mes in bd_producao[ano].keys():
                for uf in bd_producao[ano][mes].keys():
                    for combustivel in bd_producao[ano][mes][uf].keys():
                        bd_sem_dict.append(bd_producao[ano][mes][uf][combustivel]['dados'])

    def gera_sql(self):
        sequencia_sql = list()
        for item in bd_sem_dict:
            query = f"INSERT INTO consumo(ano, mes, data_referencia, uf, tipo_combustivel, potencia_gerada) " \
                    f"values({item.ano}, {item.mes}, '{str(item.data_referencia)}', " \
                    f"'{item.uf}', '{item.tipo_combustivel}', {item.energia_produzida});"
            sequencia_sql.append(query)

        print(f'{len(sequencia_sql)} queries geradas')
        self.escreve_arquivo_sql(sequencia_sql)

    def escreve_arquivo_csv(self):
        if os.path.isfile(csv_file_result):
            os.remove(csv_file_result)
        header = ['ano', 'mes', 'data_referencia', 'uf', 'tipo_combustivel', 'potencia_gerada']

        with open(csv_file_result, 'w', encoding='utf-16') as f:
            writer = csv.writer(f)
            writer.writerow(header)

            rows = [x.to_csv() for x in bd_sem_dict]
            writer.writerows(rows)

    def escreve_arquivo_sql(self, sequencia_sql):
        if os.path.isfile(sql_file_result):
            os.remove(sql_file_result)

        query_create_database = 'create database if not exists projeto_energia;\n'
        query_use_db = 'use projeto_energia;\n'

        query_create_table = 'create table if not exists consumo(' \
                             'id int not null auto_increment primary key, ' \
                             'ano int not null, ' \
                             'mes int not null, ' \
                             'data_referencia date not null, ' \
                             'uf varchar(2) not null, ' \
                             'tipo_combustivel varchar(120), ' \
                             'potencia_gerada double);\n'

        with open(sql_file_result, 'w', encoding='utf-16') as f:
            f.write(query_create_database)
            f.write(query_use_db)
            f.write(query_create_table)
            for sql in sequencia_sql:
                f.write(f'{sql}\n')

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

                if modelo_geracao.fase_atual_agente_gerador == 'Operação':
                    # Só contabilizo as usinas em operação
                    conteudo_csv.append(modelo_geracao)

        print('Gerando o relatório pra importar no banco')
        self.gera_relatorio(conteudo_csv)
        print(f'Total de erros: {self.contador_erros}')
        self.gera_sql()
        self.escreve_arquivo_csv()


if __name__ == '__main__':
    if isinstance(sys.argv[1], list):
        file_path = sys.argv[1][0]
    else:
        file_path = sys.argv[1]

    print(f'sys.argv: {sys.argv}')
    processador = ProcessaDadosEmpreendimentosGeracao(file_path)
    processador.executa()
