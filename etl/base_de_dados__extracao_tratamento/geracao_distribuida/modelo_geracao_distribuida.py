"""
Dicionário de dados para as colunas do arquivo CSV:

    - DatGeracaoConjuntoDados
    - AnmPeriodoReferencia
    - NumCNPJDistribuidora
    - SigAgente
    - NomAgente
    - CodClasseConsumo
    - DscClasseConsumo
    - CodSubGrupoTarifario
    - DscSubGrupoTarifario
    - CodUFibge
    - SigUF
    - CodRegiao
    - NomRegiao
    - CodMunicipioIbge
    - NomMunicipio
    - SigTipoConsumidor
    - NumCpfCnpj
    - NomTitularEmpreendimento
    - CodEmpreendimento
    - DthAtualizaCadastralEmpreend
    - SigModalidadeEmpreendimento
    - DscModalidadeHabilitado
    - QtdUCRecebeCredito
    - SigTipoGeracao
    - DscFonteGeracao
    - DscPorte
    - NumCoordNEmpreendimento
    - NumCoordEEmpreendimento
    - MdaPotenciaInstaladakW
    - NomSubEstacao
    - NumCoordESub
    - NumCoordNSub
"""
from datetime import date, datetime
from enum import Enum
from locale import atof, setlocale, LC_ALL, LC_NUMERIC

import locale


class TipoGeracao(Enum):
    UTN = 'Usina Termonuclear'
    UTE = 'Usina Termoelétrica'
    UHE = 'Usina Hidrelétrica'
    UFV = 'Central Geradora Solar Fotovoltaica'
    PCH = 'Pequena Central Hidrelétrica'
    EOL = 'Central Geradora Eólica'
    CGU = 'Central Geradora Undi-Elétrica'
    CGH = 'Central Geradora Hidrelétrica'


class SubgrupoTarifario(Enum):
    A1 = 'Tensão >= 230 kV'
    A2 = 'Tensão entre 88 kV e 138 kV'
    A3 = 'Tensão de 69 kV'
    A3a = 'Tensão de 30 kV a 44 kV'
    A4 = 'Tensão de 2,3 kV a 25 kV'
    AS = 'Subterrâneo'
    B1 = 'Residencial'
    B2 = 'Rural'
    B3 = 'Demais classes'
    B4 = 'Iluminação Pública'


class TipoConsumidor(Enum):
    PF = 'Pessoa Física'
    PJ = 'Pessoa Jurídica'


class ModalidadeAgenteGerador(Enum):
    P = 'Com microgeração ou minigeração distribuída'
    R = 'Autoconsumo remoto'
    C = 'Geração Compartilhada'
    M = 'Empreendimento de Múltiplas UCs (Unidades Consumidoras)'



class ModeloGeracaoDistribuida:
    def __init__(self, data_geracao_conjunto_dados, ano_mes_referencia_dados, cnpj_agente_gerador,
                 sigla_agente_gerador, nome_agente_gerador, codigo_classe_consumo_consumidores,
                 descricao_consumo_consumidores, codigo_subgrupo_tarifario, descricao_subgrupo_tarifario,
                 codigo_unidade_federativa, sigla_unidade_federativa, codigo_meso_regiao, nome_meso_regiao,
                 codigo_municipio, nome_municipio, tipo_consumidor, cpf_cnpj_proprietario_agente_gerador,
                 nome_titular_agente_gerador, codigo_empreendimento_gerador, ultima_atualizacao_agente_cadastral,
                 sigla_modalidade_empreendimento_gerador, descricao_modalidade_empreendimento_gerador,
                 contador_ucs, tipo_geracao, combustivel_utilizado, porte_agente_gerador,
                 latitude_agente_gerador, longitude_agente_gerador, potencia_instalada, nome_subestacao,
                 latitude_subestacao, longitude_subestacao):
        setlocale(LC_ALL, 'pt-BR.UTF-8')
        self.data_geracao_conjunto_dados = data_geracao_conjunto_dados
        self.ano_mes_referencia_dados = ano_mes_referencia_dados
        self.cnpj_agente_gerador = cnpj_agente_gerador
        self.sigla_agente_gerador = sigla_agente_gerador
        self.nome_agente_gerador = nome_agente_gerador
        self.codigo_classe_consumo_consumidores = codigo_classe_consumo_consumidores
        self.descricao_consumo_consumidores = descricao_consumo_consumidores
        self.codigo_subgrupo_tarifario = codigo_subgrupo_tarifario
        self.descricao_subgrupo_tarifario = descricao_subgrupo_tarifario
        self.codigo_unidade_federativa = codigo_unidade_federativa
        self.sigla_unidade_federativa = sigla_unidade_federativa
        self.codigo_meso_regiao = codigo_meso_regiao
        self.nome_meso_regiao = nome_meso_regiao
        self.codigo_municipio = codigo_municipio
        self.nome_municipio = nome_municipio
        self.tipo_consumidor = tipo_consumidor
        self.cpf_cnpj_proprietario_agente_gerador = cpf_cnpj_proprietario_agente_gerador
        self.nome_titular_agente_gerador = nome_titular_agente_gerador
        self.codigo_empreendimento_gerador = codigo_empreendimento_gerador
        self.ultima_atualizacao_agente_cadastral = ultima_atualizacao_agente_cadastral
        self.sigla_modalidade_empreendimento_gerador = sigla_modalidade_empreendimento_gerador
        self.descricao_modalidade_empreendimento_gerador = descricao_modalidade_empreendimento_gerador
        self.contador_ucs = contador_ucs
        self.tipo_geracao = tipo_geracao
        self.combustivel_utilizado = combustivel_utilizado
        self.porte_agente_gerador = porte_agente_gerador
        self.latitude_agente_gerador = latitude_agente_gerador
        self.longitude_agente_gerador = longitude_agente_gerador
        self.potencia_instalada = potencia_instalada
        self.nome_subestacao = nome_subestacao
        self.latitude_subestacao = latitude_subestacao
        self.longitude_subestacao = longitude_subestacao

    @staticmethod
    def coluna_valida(self, valor_coluna):
        return valor_coluna is not None and len(valor_coluna) > 0

    @classmethod
    def from_linha_csv(cls, linha: []):
        setlocale(LC_ALL, 'pt-BR.UTF-8')
        return ModeloGeracaoDistribuida(
            data_geracao_conjunto_dados=linha[0],
            ano_mes_referencia_dados=linha[1],
            cnpj_agente_gerador=linha[2],
            sigla_agente_gerador=linha[3],
            nome_agente_gerador=linha[4],
            codigo_classe_consumo_consumidores=linha[5],
            descricao_consumo_consumidores=linha[6],
            codigo_subgrupo_tarifario=linha[7],
            descricao_subgrupo_tarifario=linha[8],
            codigo_unidade_federativa=linha[9],
            sigla_unidade_federativa=linha[10],
            codigo_meso_regiao=linha[11],
            nome_meso_regiao=linha[12],
            codigo_municipio=linha[13],
            nome_municipio=linha[14],
            tipo_consumidor=linha[15],
            cpf_cnpj_proprietario_agente_gerador=linha[16],
            nome_titular_agente_gerador=linha[17],
            codigo_empreendimento_gerador=linha[18],
            ultima_atualizacao_agente_cadastral=linha[19],
            sigla_modalidade_empreendimento_gerador=linha[20],
            descricao_modalidade_empreendimento_gerador=linha[21],
            contador_ucs=linha[22],
            tipo_geracao=linha[23],
            combustivel_utilizado=linha[24],
            porte_agente_gerador=linha[25],
            latitude_agente_gerador=linha[26],
            longitude_agente_gerador=linha[27],
            potencia_instalada=linha[28],
            nome_subestacao=linha[29],
            latitude_subestacao=linha[30],
            longitude_subestacao=linha[31])

    def processa(self):
        pass
