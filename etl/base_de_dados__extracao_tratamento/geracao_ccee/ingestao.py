from copy import deepcopy
from datetime import date, datetime
from modelo_geracao_ccee import (
    GeracaoEmpresaMes,
    GeracaoEmpresaMesUF,
    GeracaoFonteEnergeticaMesUF,
    GeracaoMesUF,
    ModeloGeracaoCCEE,
    RegiaoBrasil,
    TipoRegimeConcessao,
    UnidadeFederativa)
from os import listdir
from os.path import isfile, join

import argparse
import csv
import os
import pandas as pd
import sys
import traceback


class Relatorio:
    lista_empresas = []
    lista_fontes_energeticas = []
    total_pago = None
    total_recebido = None
    total_energia_entregue = None
    total_energia_recebida = None
    total_capacidade = None
    total_garantia_fisica = None
    total_geracao_centro_gravidade = None
    total_geracao_ponto_conexao = None

    def __init__(self, nome_tabela: str, ano: int, mes: int,
                 uf: str = None, fonte_energetica: str = None, empresa: str = None):
        self.nome_tabela = nome_tabela
        self.ano = ano
        self.mes = mes
        self.uf = uf
        self.fonte_energetica = fonte_energetica,
        self.empresa = empresa

        if self.empresa is None or len(self.empresa) == 0:
            self.lista_empresas = None

        self.total_pago = 0
        self.total_recebido = 0
        self.total_energia_entregue = 0
        self.total_energia_recebida = 0
        self.total_capacidade = 0
        self.total_garantia_fisica = 0
        self.total_geracao_centro_gravidade = 0
        self.total_geracao_ponto_conexao = 0

    def atualiza_dados(self, record):
        if self.empresa is None or len(self.empresa) == 0:
            if record.razao_social not in self.lista_empresas:
                self.lista_empresas.append(record.razao_social)

        self.total_pago = self.total_pago + record.pagamento_mre
        self.total_recebido = self.total_recebido + record.recebimento_mre
        self.total_energia_entregue = self.total_energia_entregue + record.energia_entregue_ao_mre
        self.total_energia_recebida = self.total_energia_recebida + record.energia_recebida_mre
        self.total_capacidade = self.total_capacidade + record.capacidade_usina

    def monta_query_insert(self):
        query_part_1 = f'INSERT INTO {self.nome_tabela} ()'


class BDGeracaoMesUF:
    bd = dict()
    bd_mes = dict()

    def __init__(self):
        pass

    def add_record(self, record):
        self.add_record_geral(record)
        self.add_record_mes(record)

    def add_record_geral(self, record):
        if record.ano not in self.bd:
            self.bd[record.ano] = dict()
        if record.mes not in self.bd[record.ano]:
            self.bd[record.ano][record.mes] = dict()
        if record.uf not in self.bd[record.ano][record.mes]:
            self.bd[record.ano][record.mes][record.uf] = {
                'empresas_distintas': list(),
                'total_pago': 0.0,
                'total_recebido': 0.0,
                'total_energia_entregue': 0.0,
                'total_energia_recebida': 0.0,
                'total_capacidade': 0,
                'total_geracao_centro_gravidade': 0
            }

        if record.razao_social not in self.bd[record.ano][record.mes][record.uf]['empresas_distintas']:
            self.bd[record.ano][record.mes][record.uf]['empresas_distintas'].append(record.razao_social)

        self.bd[record.ano][record.mes][record.uf]['total_pago'] += record.pagamento_mre
        self.bd[record.ano][record.mes][record.uf]['total_recebido'] += record.recebimento_mre
        self.bd[record.ano][record.mes][record.uf]['total_energia_entregue'] += record.energia_entregue_ao_mre
        self.bd[record.ano][record.mes][record.uf]['total_energia_recebida'] += record.energia_recebida_mre
        self.bd[record.ano][record.mes][record.uf]['total_capacidade'] += record.capacidade_usina
        self.bd[record.ano][record.mes][record.uf]['total_geracao_centro_gravidade'] += record.geracao_centro_gravidade


    def add_record_mes(self, record):
        if record.ano not in self.bd_mes:
            self.bd_mes[record.ano] = dict()
        if record.mes not in self.bd_mes[record.ano]:
            self.bd_mes[record.ano][record.mes] = {
                'total_pago': 0.0,
                'total_recebido': 0.0,
                'total_energia_entregue': 0.0,
                'total_energia_recebida': 0.0,
                'total_capacidade': 0,
                'total_geracao_centro_gravidade': 0
            }

        self.bd_mes[record.ano][record.mes]['total_pago'] += record.pagamento_mre
        self.bd_mes[record.ano][record.mes]['total_recebido'] += record.recebimento_mre
        self.bd_mes[record.ano][record.mes]['total_energia_entregue'] += record.energia_entregue_ao_mre
        self.bd_mes[record.ano][record.mes]['total_energia_recebida'] += record.energia_recebida_mre
        self.bd_mes[record.ano][record.mes]['total_capacidade'] += record.capacidade_usina
        self.bd_mes[record.ano][record.mes]['total_geracao_centro_gravidade'] += record.geracao_centro_gravidade

    def exporta_ano_mes(self):
        pass

    def exporta_ano_mes_uf(self):
        registros = []
        cabecalho = ['data', 'uf', 'total_pago', 'total_recebido', 'total_energia_entregue',
                     'total_energia_recebida', 'total_capacidade', 'total_geracao_centro_gravidade']
        for ano in self.bd.keys():
            for mes in self.bd[ano].keys():
                for uf in self.bd[ano][mes].keys():
                    info = self.bd[ano][mes][uf]
                    dt = datetime(int(ano), int(mes), 1, 0, 0, 0).date()
                    registro = [dt.strftime('%Y-%m-%d'), uf, info['total_pago'], info['total_recebido'],
                                info['total_energia_entregue'], info['total_energia_recebida'],
                                info['total_capacidade'], info['total_geracao_centro_gravidade']]
                    registros.append(registro)

        nome_arquivo = 'ano_mes_uf.csv'
        contador_linha = 0
        with open(nome_arquivo, 'w') as arquivo:
            linha_cabecalho = ';'.join(cabecalho)
            # print(linha_cabecalho, file=arquivo, end='')
            arquivo.write(linha_cabecalho + '\n')
            for linha in registros:
                # Processando a linha antes
                contador_item = 0
                while contador_item < len(linha):
                    if linha[contador_item] is None:
                        linha[contador_item] = ''
                    elif isinstance(linha[contador_item], float):
                        linha[contador_item] = str(linha[contador_item])
                    elif isinstance(linha[contador_item], int):
                        linha[contador_item] = str(linha[contador_item])
                    elif isinstance(linha[contador_item], bool):
                        if linha[contador_item] is True:
                            linha[contador_item] = 'V'
                        else:
                            linha[contador_item] = 'F'
                    contador_item += 1
                linha_str = ';'.join(linha)
                # print(linha, file=arquivo, end='')
                arquivo.write(linha_str + '\n')
                contador_linha += 1
        print(f'{contador_linha} linhas escritas no arquivo {nome_arquivo}')


class BDGeracaoFonteEnergeticaMesUF:
    bd = dict()
    bd_fonte_energetica = dict()

    def __init__(self):
        pass

    def add_record(self, record):
        self.add_record_geral(record)
        self.add_record_fonte_energetica(record)

    def add_record_geral(self, record):
        if record.ano not in self.bd:
            self.bd[record.ano] = dict()
        if record.mes not in self.bd[record.ano]:
            self.bd[record.ano][record.mes] = dict()
        if record.uf not in self.bd[record.ano][record.mes]:
            self.bd[record.ano][record.mes][record.uf] = dict()
        if record.fonte_energia not in self.bd[record.ano][record.mes][record.uf]:
            self.bd[record.ano][record.mes][record.uf][record.fonte_energia] = {
                'empresas_distintas': [],
                'total_pago': 0.0,
                'total_recebido': 0.0,
                'total_energia_entregue': 0.0,
                'total_energia_recebida': 0.0,
                'total_capacidade': 0,
                'total_geracao_centro_gravidade': 0
            }

        if record.razao_social not in self.bd[record.ano][record.mes][record.uf][record.fonte_energia]['empresas_distintas']:
            self.bd[record.ano][record.mes][record.uf][record.fonte_energia]['empresas_distintas'].append(record.razao_social)
        self.bd[record.ano][record.mes][record.uf][record.fonte_energia]['total_pago'] += record.pagamento_mre
        self.bd[record.ano][record.mes][record.uf][record.fonte_energia]['total_recebido'] += record.recebimento_mre
        self.bd[record.ano][record.mes][record.uf][record.fonte_energia]['total_energia_entregue'] += record.energia_entregue_ao_mre
        self.bd[record.ano][record.mes][record.uf][record.fonte_energia]['total_energia_recebida'] += record.energia_recebida_mre
        self.bd[record.ano][record.mes][record.uf][record.fonte_energia]['total_capacidade'] += record.capacidade_usina
        self.bd[record.ano][record.mes][record.uf][record.fonte_energia]['total_geracao_centro_gravidade'] += record.geracao_centro_gravidade

    def add_record_fonte_energetica(self, record):
        if record.ano  not in self.bd_fonte_energetica:
            self.bd_fonte_energetica[record.ano] = dict()
        if record.mes not in self.bd_fonte_energetica[record.ano]:
            self.bd_fonte_energetica[record.ano][record.mes] = dict()
        if record.fonte_energia not in self.bd_fonte_energetica[record.ano][record.mes]:
            self.bd_fonte_energetica[record.ano][record.mes][record.fonte_energia] = {
                'empresas_distintas': [],
                'total_pago': 0.0,
                'total_recebido': 0.0,
                'total_energia_entregue': 0.0,
                'total_energia_recebida': 0.0,
                'total_capacidade': 0,
                'total_geracao_centro_gravidade': 0
            }

        if record.razao_social not in self.bd_fonte_energetica[record.ano][record.mes][record.fonte_energia]['empresas_distintas']:
            self.bd_fonte_energetica[record.ano][record.mes][record.fonte_energia]['empresas_distintas'].append(record.razao_social)

    def exporta_ano_mes_uf_fonte_energia(self):
        registros = []
        cabecalho = ['data', 'uf', 'fonte_energia', 'total_pago', 'total_recebido',
                     'total_energia_entregue', 'total_energia_recebida', 'total_capacidade',
                     'total_geracao_centro_gravidade']

        for ano in self.bd.keys():
            for mes in self.bd[ano].keys():
                for uf in self.bd[ano][mes].keys():
                    for fonte_energia in self.bd[ano][mes][uf].keys():
                        info = self.bd[ano][mes][uf][fonte_energia]
                        dt = datetime(int(ano), int(mes), 1, 0, 0, 0).date()
                        registro = [dt.strftime('%Y-%m-%d'), uf, fonte_energia,
                                    info['total_pago'], info['total_recebido'],
                                    info['total_energia_entregue'], info['total_energia_recebida'],
                                    info['total_capacidade'], info['total_geracao_centro_gravidade']]
                        registros.append(registro)

        nome_arquivo = 'ano_mes_uf_fonte.csv'
        contador_linha = 0
        with open(nome_arquivo, 'w') as arquivo:
            linha_cabecalho = ';'.join(cabecalho)
            # print(linha_cabecalho, file=arquivo, end='')
            arquivo.write(linha_cabecalho + '\n')
            for linha in registros:
                # Processando a linha antes
                contador_item = 0
                while contador_item < len(linha):
                    if linha[contador_item] is None:
                        linha[contador_item] = ''
                    elif isinstance(linha[contador_item], float):
                        linha[contador_item] = str(linha[contador_item])
                    elif isinstance(linha[contador_item], int):
                        linha[contador_item] = str(linha[contador_item])
                    elif isinstance(linha[contador_item], bool):
                        if linha[contador_item] is True:
                            linha[contador_item] = 'V'
                        else:
                            linha[contador_item] = 'F'
                    contador_item += 1
                linha_str = ';'.join(linha)
                # print(linha, file=arquivo, end='')
                arquivo.write(linha_str + '\n')
                contador_linha += 1
        print(f'{contador_linha} linhas escritas no arquivo {nome_arquivo}')

    def exporta_ano_mes_fonte_energia(self):
        registros = []
        cabecalho = ['data', 'fonte_energia', 'total_pago', 'total_recebido',
                     'total_energia_entregue', 'total_energia_recebida', 'total_capacidade',
                     'total_geracao_centro_gravidade']

        for ano in self.bd_fonte_energetica.keys():
            for mes in self.bd_fonte_energetica[ano].keys():
                for fonte_energia in self.bd_fonte_energetica[ano][mes].keys():
                    info = self.bd_fonte_energetica[ano][mes][fonte_energia]
                    dt = datetime(int(ano), int(mes), 1, 0, 0, 0).date()
                    registro = [dt.strftime('%Y-%m-%d'), fonte_energia, info['total_pago'],
                                info['total_recebido'],
                                info['total_energia_entregue'], info['total_energia_recebida'],
                                info['total_capacidade'], info['total_geracao_centro_gravidade']]
                    registros.append(registro)

        nome_arquivo = 'ano_mes_fonte.csv'
        contador_linha = 0
        with open(nome_arquivo, 'w') as arquivo:
            linha_cabecalho = ';'.join(cabecalho)
            # print(linha_cabecalho, file=arquivo, end='')
            arquivo.write(linha_cabecalho + '\n')
            for linha in registros:
                # Processando a linha antes
                contador_item = 0
                while contador_item < len(linha):
                    if linha[contador_item] is None:
                        linha[contador_item] = ''
                    elif isinstance(linha[contador_item], float):
                        linha[contador_item] = str(linha[contador_item])
                    elif isinstance(linha[contador_item], int):
                        linha[contador_item] = str(linha[contador_item])
                    elif isinstance(linha[contador_item], bool):
                        if linha[contador_item] is True:
                            linha[contador_item] = 'V'
                        else:
                            linha[contador_item] = 'F'
                    contador_item += 1
                linha_str = ';'.join(linha)
                # print(linha, file=arquivo, end='')
                arquivo.write(linha_str + '\n')
                contador_linha += 1
        print(f'{contador_linha} linhas escritas no arquivo {nome_arquivo}')


class BDGeracaoEmpresaMes:
    bd = dict()
    bd_empresa = dict()

    def __init__(self):
        pass

    def add_record(self, record):
        self.add_record_geral(record)
        self.add_record_empresa(record)

    def add_record_geral(self, record):
        pass

    def add_record_empresa(self, record):
        pass


class BDGeracaoEmpresaMesUF:
    bd = dict()
    bd_empresa = dict()
    bd_empresa_mes = dict()

    def __init__(self):
        pass

    def add_record(self, record):
        self.add_record_geral(record)
        self.add_record_empresa(record)
        self.add_record_empresa_mes(record)

    def add_record_geral(self, record):
        pass

    def add_record_empresa(self, record):
        pass

    def add_record_empresa_mes(self, record):
        pass


class BD:
    todos_registros = []
    bd_geracao_mes_uf = None
    bd_geracao_fonte_energetica_mes_uf = None
    bd_geracao_empresa_mes = None
    bd_geracao_empresa_mes_uf = None

    def __init__(self):
        self.bd_geracao_mes_uf = BDGeracaoMesUF()
        self.bd_geracao_fonte_energetica_mes_uf = BDGeracaoFonteEnergeticaMesUF()
        self.bd_geracao_empresa_mes = BDGeracaoEmpresaMes()
        self.bd_geracao_empresa_mes_uf = BDGeracaoEmpresaMesUF()

    def add_record(self, record):
        self.todos_registros.append(record)
        self.bd_geracao_mes_uf.add_record(record)
        self.bd_geracao_fonte_energetica_mes_uf.add_record(record)
        self.bd_geracao_empresa_mes.add_record(record)
        self.bd_geracao_empresa_mes_uf.add_record(record)


class ProcessaDadosGeracaoCCEE:
    bd = None

    def __init__(self, args=None):
        self.args = args
        self.pasta_dados = self.args.pasta_dados \
            if self.args is not None and self.args.data_directory is not None \
            else f'..{os.sep}dados_ccee{os.sep}dados_consolidados'
        self.bd = BD()

    def get_lista_arquivos(self):
        lista_arquivos_raw = listdir(self.pasta_dados)
        lista_arquivos = list()
        for item in lista_arquivos_raw:
            if isfile(join(self.pasta_dados, item)) and '.csv' in item:
                lista_arquivos.append(f'{self.pasta_dados}{os.sep}{item}')
        return lista_arquivos

    def importa_csv_para_pandas(self, dados_modelo_csv):
        lista_para_pandas = [x.to_pandas() for x in dados_modelo_csv]
        return pd.DataFrame.from_records(lista_para_pandas)

    def _captura_somente_nome_arquivo(self, caminho_arquivo):
        partes_caminho_arquivo = caminho_arquivo.split(os.sep)
        nome_completo_arquivo = partes_caminho_arquivo[len(partes_caminho_arquivo) - 1]
        nome_arquivo = nome_completo_arquivo.split('.')[0]
        return nome_arquivo

    def _processa_arquivo(self, arquivo):
        with open(arquivo, 'r', encoding='utf-16') as f:
            contador_linha = 0
            nome_arquivo = self._captura_somente_nome_arquivo(arquivo)
            nome_arquivo_partes = nome_arquivo.split('-')
            ano = nome_arquivo_partes[0]
            mes = nome_arquivo_partes[1]
            for line in csv.reader(f, delimiter='\t'):
                if contador_linha > 0:
                    # Pra pular a primeira linha de cabeçalho...
                    geracao_ccee = ModeloGeracaoCCEE.from_list(
                        ano=ano, mes=mes, registro=line)
                    self.bd.add_record(geracao_ccee)
                contador_linha += 1

    def executa(self):
        arquivos_para_parsear = self.get_lista_arquivos()
        contador_arquivos = 0
        for arquivo in arquivos_para_parsear:
            print(f'Processando arquivo {arquivo}')
            self._processa_arquivo(arquivo)
            contador_arquivos += 1
        print(f'Foram processados {contador_arquivos} arquivos')
        print('\n\n')
        self.exporta()

    def exporta(self):
        self.bd.bd_geracao_mes_uf.exporta_ano_mes_uf()


if __name__ == '__main__':
    print('Iniciando.....')

    parser = argparse.ArgumentParser('Ingest CCEE')
    parser.add_argument('-d', '--data-directory', dest='data_directory')
    parser.add_argument('-v', '--version', dest='version')
    parser.add_argument('-vv', '--verbose', action='store_false', dest='verbose')
    args = parser.parse_args()

    processador = ProcessaDadosGeracaoCCEE()
    try:
        processador.executa()
    except KeyboardInterrupt:
        pass
    except SystemExit:
        pass
