from datetime import date, datetime
from os import listdir
from os.path import isfile, join

import argparse
import csv
import os
import sys


# Algumas configs
csv_final = f"..{os.sep}csv's{os.sep}geracao.csv"


def trata_texto_numero(texto: str = None):
    numero = 0

    # O "número" vem em português. Vou fazer a "tradução"
    if texto is not None and len(texto) > 0:
        if '.' in texto:
            texto = texto.replace('.', '')
        if ',' in texto:
            texto = texto.replace(',', '.')
        if '.' in texto:
            numero = float(texto)
        else:
            numero = int(texto)

    return numero


class ModeloGeracaoCCEE:
    data_dados = None
    data_evento = None
    def __init__(self, ano: int, mes: int,
                 cod_usina: int,
                 razao_social: str,
                 ceg_empreendimento: str,
                 sigla_ativo: str,
                 fonte_energia: str,
                 participante_mre: bool,
                 submercado: str,
                 uf: str,
                 tipo_despacho_usina: str,
                 tipo_regime_concessao: str,
                 capacidade_usina: float,
                 garantia_fisica: float,
                 cod_parcela_usina: int,
                 sigla_parcela_usina: str,
                 ano_mes_evento: str,
                 geracao_centro_gravidade: int,
                 geracao_teste_centro_gravidade: int,
                 geracao_ponto_conexao: int,
                 geracao_teste_ponto_conexao: int,
                 geracao_manutencao_reserva_operativa: int,
                 geracao_restricao_operacao_constrained_on: int,
                 geracao_seguranca_energetica: int,
                 garantia_fisica_centro_gravidade_apurada_lastro: int,
                 garantia_fisica_centro_gravidade: int,
                 garantia_fisica_modulada_ajustada_centro_gravidade: int,
                 energia_entregue_ao_mre: int,
                 energia_recebida_mre: int,
                 pagamento_mre: int,
                 recebimento_mre: int):
        self.ano = ano
        self.mes = mes
        self.cod_usina = cod_usina
        self.razao_social = razao_social
        self.ceg_empreendimento = ceg_empreendimento
        self.sigla_ativo = sigla_ativo
        self.fonte_energia = fonte_energia
        self.participante_mre = participante_mre
        self.submercado = submercado
        self.uf = uf
        self.tipo_despacho_usina = tipo_despacho_usina
        self.tipo_regime_concessao = tipo_regime_concessao
        self.capacidade_usina = capacidade_usina
        self.garantia_fisica = garantia_fisica
        self.cod_parcela_usina = cod_parcela_usina
        self.sigla_parcela_usina = sigla_parcela_usina
        self.ano_mes_evento = ano_mes_evento
        self.geracao_centro_gravidade = geracao_centro_gravidade
        self.geracao_teste_centro_gravidade = geracao_teste_centro_gravidade
        self.geracao_ponto_conexao = geracao_ponto_conexao
        self.geracao_teste_ponto_conexao = geracao_teste_ponto_conexao
        self.geracao_manutencao_reserva_operativa = geracao_manutencao_reserva_operativa
        self.geracao_restricao_operacao_constrained_on = geracao_restricao_operacao_constrained_on
        self.geracao_seguranca_energetica = geracao_seguranca_energetica
        self.garantia_fisica_centro_gravidade_apurada_lastro=garantia_fisica_centro_gravidade_apurada_lastro
        self.garantia_fisica_centro_gravidade = garantia_fisica_centro_gravidade
        self.garantia_fisica_modulada_ajustada_centro_gravidade = garantia_fisica_modulada_ajustada_centro_gravidade
        self.energia_entregue_ao_mre = energia_entregue_ao_mre
        self.energia_recebida_mre = energia_recebida_mre
        self.pagamento_mre = pagamento_mre
        self.recebimento_mre = recebimento_mre

    @classmethod
    def from_list(cls, ano: int, mes: int, registro: list):
        return ModeloGeracaoCCEE(
            ano=ano,
            mes=mes,
            cod_usina=registro[0],
            razao_social=registro[1],
            ceg_empreendimento=registro[2],
            sigla_ativo=registro[3],
            fonte_energia=registro[4],
            participante_mre=registro[5],
            submercado=registro[6],
            uf=registro[7],
            tipo_despacho_usina=registro[8],
            tipo_regime_concessao=registro[9],
            capacidade_usina=trata_texto_numero(registro[10]),
            garantia_fisica=trata_texto_numero(registro[11]),
            cod_parcela_usina=registro[12],
            sigla_parcela_usina=registro[13],
            ano_mes_evento=registro[14],
            geracao_centro_gravidade=trata_texto_numero(registro[15]),
            geracao_teste_centro_gravidade=registro[16],
            geracao_ponto_conexao=registro[17],
            geracao_teste_ponto_conexao=registro[18],
            geracao_manutencao_reserva_operativa=registro[19],
            geracao_restricao_operacao_constrained_on=registro[20],
            geracao_seguranca_energetica=registro[21],
            garantia_fisica_centro_gravidade_apurada_lastro=registro[22],
            garantia_fisica_centro_gravidade=registro[23],
            garantia_fisica_modulada_ajustada_centro_gravidade=registro[24],
            energia_entregue_ao_mre=trata_texto_numero(registro[25]),
            energia_recebida_mre=trata_texto_numero(registro[26]),
            pagamento_mre=trata_texto_numero(registro[27]),
            recebimento_mre=trata_texto_numero(registro[28]))

    def _corrige_numerico(self, valor_str, considerar_decimal=False):
        if valor_str is None or len(valor_str) == 0:
            return 0
        if '.' in valor_str:
            # O ponto aparece separando milhares. Deve ser removido.
            valor_str = valor_str.replace('.', '')
        if considerar_decimal and ',' in valor_str:
            # A vírgula aparece separando os decimais. Deve ser convertida pra ponto (.)
            valor_str = valor_str.replace(',', '.')

        if considerar_decimal:
            return float(valor_str)
        return int(valor_str)


    def processa(self):
        if self.ano is None or self.ano == 0 or self.mes is None or self.mes == 0:
            raise Exception('Mês ou ano dos dados inválido')

        self.data_dados = datetime(self.ano, self.mes, 1, 0, 0, 0).date()

        if self.ano_mes_evento is not None and len(self.ano_mes_evento) > 0:
            ano_mes_evento_partes = self.ano_mes_evento.split('/')
            ano_evento = int(ano_mes_evento_partes[0])
            mes_evento = int(ano_mes_evento_partes[1])
            self.data_evento = datetime(ano_evento, mes_evento, 1, 0, 0, 0).date()

        # Passando as strings de numéricos para numéricos de fato
        self.cod_usina = self._corrige_numerico(self.cod_usina)

        if self.participante_mre is None or len(self.participante_mre) == 0:
            self.participante_mre = False
        else:
            self.participante_mre = True if self.participante_mre == 'Sim' else False

        self.capacidade_usina = self._corrige_numerico(self.capacidade_usina, True)
        self.garantia_fisica = self._corrige_numerico(self.garantia_fisica, True)

        self.cod_parcela_usina = None \
            if self.cod_parcela_usina is None or len(self.cod_parcela_usina) == 0 \
            else int(self.cod_parcela_usina)

        self.geracao_centro_gravidade = self._corrige_numerico(self.geracao_centro_gravidade, True)
        self.geracao_teste_centro_gravidade = self._corrige_numerico(
            self.geracao_teste_centro_gravidade, True)
        self.geracao_ponto_conexao = self._corrige_numerico(self.geracao_ponto_conexao, True)
        self.geracao_teste_ponto_conexao = self._corrige_numerico(self.geracao_teste_ponto_conexao, True)
        self.geracao_manutencao_reserva_operativa = self._corrige_numerico(
            self.geracao_manutencao_reserva_operativa, True)
        self.geracao_restricao_operacao_constrained_on = self._corrige_numerico(
            self.geracao_restricao_operacao_constrained_on, True)
        self.geracao_seguranca_energetica = self._corrige_numerico(self.geracao_seguranca_energetica, True)
        self.garantia_fisica_centro_gravidade_apurada_lastro = self._corrige_numerico(
            self.garantia_fisica_centro_gravidade_apurada_lastro, True)
        self.garantia_fisica_centro_gravidade = self._corrige_numerico(
            self.garantia_fisica_centro_gravidade, True)
        self.garantia_fisica_modulada_ajustada_centro_gravidade = self._corrige_numerico(
            self.garantia_fisica_modulada_ajustada_centro_gravidade, True)
        self.energia_entregue_ao_mre = self._corrige_numerico(self.energia_entregue_ao_mre, True)
        self.energia_recebida_mre = self._corrige_numerico(self.energia_recebida_mre, True)
        self.pagamento_mre = self._corrige_numerico(self.pagamento_mre)
        self.recebimento_mre = self._corrige_numerico(self.recebimento_mre)


class BDGeracaoFonteEnergeticaMesUF:
    bd = dict()
    bd_fonte_energetica = dict()
    todos_registros = []

    def __init__(self):
        pass

    def exporta(self, cabecalho, linhas, nome_arquivo):
        """
        Salva os dados consolidados em arquivo CSV.

        :param cabecalho: Lista de vsalores de nomes de colunas para a primeira linha
                          do arquivo CSV.
        :type cabecalho: list

        :param linhas: Lista de registros (onde cada registro é uma lista de valores que
                       devem ser em mesma quantidade que os ítens do cabeçalho) a serem
                       gravados no arquivo CSV.
        :type linhas: list

        :param nome_arquivo: Caminho completo com o nome do arquivo a ser criado.
        :type nome_arquivo: str
        """
        contador_linha = 0
        with open(nome_arquivo, 'w') as arquivo:
            # Gravando o cabeçalho.
            linha_cabecalho = ';'.join(cabecalho)
            arquivo.write(linha_cabecalho + '\n')
            for linha in linhas:
                # Processando a linha antes
                contador_item = 0
                while contador_item < len(linha):
                    if linha[contador_item] is None:
                        # Se o dado é nulo, teremos 2 vírgulas seguidas no arquivo
                        linha[contador_item] = ''
                    elif isinstance(linha[contador_item], float):
                        linha[contador_item] = str(linha[contador_item])
                    elif isinstance(linha[contador_item], int):
                        linha[contador_item] = str(linha[contador_item])
                    elif isinstance(linha[contador_item], bool):
                        # Definimos que booleano será V ou F
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

    def add_record(self, record):
        """
        Adiciona 1 registro ao cômputo para análise. Este registro deverá ser adicionado
        à listagem de todos os registros e também contabilizarmos seus valores para os
        consolidados por estado, mês e fonte de energia.

        :param record: Registro a ser adicionado.
        :type record: list
        """
        # Mantendo uma lista com tudo só por via das dúvidas rs
        self.todos_registros.append(record)

        # Antes preciso verificar se os dados para aquele mês, UF e fonte existem
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
                'total_geracao_centro_gravidade': 0}

        if record.razao_social not in self.bd[record.ano][record.mes][record.uf][record.fonte_energia]['empresas_distintas']:
            self.bd[record.ano][record.mes][record.uf][record.fonte_energia]['empresas_distintas']\
                .append(record.razao_social)
        # Agora vamos às contas...
        self.bd[record.ano][record.mes][record.uf][record.fonte_energia]['total_pago'] += record.pagamento_mre
        self.bd[record.ano][record.mes][record.uf][record.fonte_energia]['total_recebido'] += record.recebimento_mre
        self.bd[record.ano][record.mes][record.uf][record.fonte_energia]['total_energia_entregue'] \
            += record.energia_entregue_ao_mre
        self.bd[record.ano][record.mes][record.uf][record.fonte_energia]['total_energia_recebida'] \
            += record.energia_recebida_mre
        self.bd[record.ano][record.mes][record.uf][record.fonte_energia]['total_capacidade'] += record.capacidade_usina
        self.bd[record.ano][record.mes][record.uf][record.fonte_energia]['total_geracao_centro_gravidade'] \
            += record.geracao_centro_gravidade

    def exporta_tudo(self):
        """
        Aqui faço a exportação, mas antes removo o arquivo anterior pra gerar um novo.
        """
        if os.path.exists(csv_final):
            os.remove(csv_final)
        self.exporta_ano_mes_uf_fonte_energia(csv_final)

    def exporta_ano_mes_uf_fonte_energia(self, nome_arquivo):
        registros = []
        cabecalho = ['mes', 'uf', 'fonte_energia', 'total_pago', 'total_recebido',
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
                                    info['total_capacidade'],
                                    int(info['total_geracao_centro_gravidade']) * 720]
                        registros.append(registro)
        self.exporta(cabecalho, registros, nome_arquivo)


class ProcessaDadosGeracaoCCEE:
    bd = None

    def __init__(self, args=None):
        self.args = args
        self.pasta_dados = self.args.pasta_dados \
            if self.args is not None and self.args.pasta_dados is not None \
            else f'..{os.sep}dados_ccee{os.sep}dados_consolidados'
        self.bd = BDGeracaoFonteEnergeticaMesUF()

    def get_lista_arquivos(self):
        """Monta a lista de arquivos a serem lidos e processados."""
        # A pasta com os CSVs foi passada como parâmetro na chamada do ingest
        lista_arquivos_raw = listdir(self.pasta_dados)
        lista_arquivos = list()
        for item in lista_arquivos_raw:
            # Na dúvida verifico se é CSV e se é pasta ou arquivo. Vai que, né?
            if isfile(join(self.pasta_dados, item)) and '.csv' in item:
                lista_arquivos.append(f'{self.pasta_dados}{os.sep}{item}')
        return lista_arquivos

    def _captura_somente_nome_arquivo(self, caminho_arquivo):
        """
        Fiz esta extensão só pra separar o nome do arquivo em si, sem a extensão
        nem as partes de caminho.

        :param caminho_arquivo: Nome do arquivo com o path junto.
        """
        partes_caminho_arquivo = caminho_arquivo.split(os.sep)
        nome_completo_arquivo = partes_caminho_arquivo[len(partes_caminho_arquivo) - 1]
        nome_arquivo = nome_completo_arquivo.split('.')[0]
        return nome_arquivo

    def _processa_arquivo(self, arquivo):
        """
        Leio o arquivo, faço ajustes nos dados lidos e salvo e memória.
        :param arquivo: Caminho para arquivo a ser lido e processado.
        :type arquivo: str
        """
        with open(arquivo, 'r', encoding='utf-16') as f:
            contador_linha = 0
            # Do nome do arquivo tiro o mês e ano dos dados
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
        '''
        Realizo a captura dos dados, calculo os totais e salvo em um arquivo CSV.
        '''
        if self.args is not None and self.args.version is not None and self.args.version is True:
            # Só para o caso de eu ter utilizado a opção -v ou --version
            print('Geração CCEE - Versão 1.0')
            return

        # Monto uma lista com arquivos de origem pra analisar
        arquivos_para_parsear = self.get_lista_arquivos()
        contador_arquivos = 0
        for arquivo in arquivos_para_parsear:
            print(f'Processando arquivo {arquivo}')
            # Para cada arquivo, leio seu conteúdo e salvo em memória
            self._processa_arquivo(arquivo)
            contador_arquivos += 1
        print(f'Foram processados {contador_arquivos} arquivos')
        print('\n\n')
        self.exporta()

    def exporta(self):
        self.bd.exporta_tudo()


if __name__ == '__main__':
    print('Iniciando.....')

    # Eu passo alguns argumentos por linha de comando. Aqui registro eles...
    parser = argparse.ArgumentParser('Ingest CCEE')
    parser.add_argument('-d', '--data-directory', dest='pasta_dados')
    parser.add_argument('-v', '--version', dest='version', action='store_true')
    args = parser.parse_args()

    # Criei uma classe só pra processar pra ficar tudo separado e bonitin...
    processador = ProcessaDadosGeracaoCCEE(args)
    try:
        # Mando executar
        processador.executa()
    except KeyboardInterrupt:
        print('Interrupção pelo teclado')
    except SystemExit:
        print('Encerrando por saída do sistema')
    except Exception as exc:
        print(f'Saindo pelo seguinte erro: {exc}')
