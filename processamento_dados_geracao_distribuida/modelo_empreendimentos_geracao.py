"""
Empreendimento de geração de energia elétrica do parque gerador nacional.
Contém usinas nas diversas fases, desde etapas anteriores à outorgas até a revogação.

Dicionário de dados para as colunas do arquivo CSV:

    - DatGeracaoConjuntoDados
    - NomEmpreendimento
    - IdeNucleoCEG
    - CodCEG
    - SigUFPrincipal
    - SigTipoGeracao
    - DscFaseUsina
    - DscOrigemCombustivel
    - DscFonteCombustivel
    - DscTipoOutorga
    - NomFonteCombustivel
    - DatEntradaOperacao
    - MdaPotenciaOutorgadaKw
    - MdaPotenciaFinalizadaKw
    - MdaGarantiaFisicaKw
    - IdcGeracaoQualificada
    - NumCoordNEmpreendimento
    - NumCoordEEmpreendimento
    - DatInicioVigencia
    - DatFimVigencia
    - DscPropriRegimePariticipacao
    - DscSubBacia
    - DscMuninicpios
"""

from datetime import date, datetime
from enum import Enum
from locale import atof, setlocale, LC_ALL, LC_NUMERIC

import csv
import locale


class ProducaoMensal:
    def __init__(self, mes, ano, uf, tipo_combustivel, energia_produzida):
        self.mes = mes
        self.ano = ano
        self.uf = uf
        self.tipo_combustivel = tipo_combustivel
        self.energia_produzida = energia_produzida

    def to_csv(self):
        return [self.ano, self.mes, self.uf, self.tipo_combustivel, self.energia_produzida]

    def to_pandas(self):
        return {
            'ano': self.ano,
            'mes': self.mes,
            'uf': self.uf,
            'tipo_combustivel': self.tipo_combustivel,
            'energia_produzida': self.energia_produzida}


class ModeloEmpreendimentosGeracao:
    data_geracao_dados = None
    data_base_inicio_contagem = None

    def __init__(self, data_geracao_dados_str, nome_agente_gerador, nucleo_codigo_unico_agente_gerador,
                 codigo_unico_agente_gerador, uf_principal, tipo_geracao, fase_atual_agente_gerador,
                 origem_combustivel, tipo_combustivel, tipo_atuacao_agente_gerador, nome_combustivel,
                 data_comeco_operacao, potencia_total_outorgada, potencia_operacao, garantia_fisica,
                 geracao_qualificada, latitude_agente_gerador, longitude_agente_gerador,
                 inicio_vigencia_outorga, fim_vigencia_outorga,
                 percentual_participacao_propriedade_regime, sub_bacia_hidreletrica, municipio_estado):
        self.data_geracao_dados_str = data_geracao_dados_str
        self.nome_agente_gerador = nome_agente_gerador
        self.nucleo_codigo_unico_agente_gerador = nucleo_codigo_unico_agente_gerador
        self.codigo_unico_agente_gerador = codigo_unico_agente_gerador
        self.uf_principal = uf_principal
        self.tipo_geracao = tipo_geracao
        self.fase_atual_agente_gerador = fase_atual_agente_gerador
        self.origem_combustivel = origem_combustivel
        self.tipo_combustivel = tipo_combustivel
        self.tipo_atuacao_agente_gerador = tipo_atuacao_agente_gerador
        self.nome_combustivel = nome_combustivel
        self.data_comeco_operacao = data_comeco_operacao
        self.potencia_total_outorgada = potencia_total_outorgada
        self.potencia_operacao = potencia_operacao
        self.garantia_fisica = garantia_fisica
        self.geracao_qualificada = geracao_qualificada
        self.latitude_agente_gerador = latitude_agente_gerador
        self.longitude_agente_gerador = longitude_agente_gerador
        self.inicio_vigencia_outorga = inicio_vigencia_outorga
        self.fim_vigencia_outorga = fim_vigencia_outorga
        self.percentual_participacao_propriedade_regime = percentual_participacao_propriedade_regime
        self.sub_bacia_hidreletrica = sub_bacia_hidreletrica
        self.municipio_estado = municipio_estado

    @classmethod
    def from_linha_csv(cls, linha):
        setlocale(LC_ALL, 'pt_BR.UTF-8')
        return ModeloEmpreendimentosGeracao(
            data_geracao_dados_str=linha[0],
            nome_agente_gerador=linha[1],
            nucleo_codigo_unico_agente_gerador=linha[2],
            codigo_unico_agente_gerador=linha[3],
            uf_principal=linha[4],
            tipo_geracao=linha[5],
            fase_atual_agente_gerador=linha[6],
            origem_combustivel=linha[7],
            tipo_combustivel=linha[8],
            tipo_atuacao_agente_gerador=linha[9],
            nome_combustivel=linha[10],
            data_comeco_operacao=linha[11],
            potencia_total_outorgada=linha[12],
            potencia_operacao=linha[13],
            garantia_fisica=linha[14],
            geracao_qualificada=linha[15],
            latitude_agente_gerador=linha[16],
            longitude_agente_gerador=linha[17],
            inicio_vigencia_outorga=linha[18],
            fim_vigencia_outorga=linha[19],
            percentual_participacao_propriedade_regime=linha[20],
            sub_bacia_hidreletrica=linha[21],
            municipio_estado=linha[22])

    def _processa_data(self, data_str):
        lst_data = data_str.split('-')
        return datetime(year=int(lst_data[0]),
            month=int(lst_data[1]),
            day=int(lst_data[2]),
            hour=0,
            minute=0,
            second=0)

    def processa(self):
        data_base_inicio = datetime(1960, 1, 1, 0, 0, 0)
        lst_data_geracao_dados = self.data_geracao_dados_str.split('-')
        self.data_geracao_dados = self._processa_data(self.data_geracao_dados_str)

        # Aqui começa o processamento das datas
        if self.inicio_vigencia_outorga == '':
            self.inicio_vigencia_outorga = None
        if self.fim_vigencia_outorga == '':
            self.fim_vigencia_outorga == None
        if self.data_comeco_operacao  == '':
            self.data_comeco_operacao = None

        if self.inicio_vigencia_outorga is not None:
            self.inicio_vigencia_outorga = self._processa_data(self.inicio_vigencia_outorga)
        if self.fim_vigencia_outorga is not None:
            self.fim_vigencia_outorga = self._processa_data(self.fim_vigencia_outorga)

        if self.data_comeco_operacao is not None:
            self.data_comeco_operacao = self._processa_data(self.data_comeco_operacao)
        elif self.data_comeco_operacao is None and self.inicio_vigencia_outorga is not None:
            self.data_comeco_operacao = self.inicio_vigencia_outorga
        else:
            self.data_comeco_operacao = data_base_inicio

        if self.data_comeco_operacao < data_base_inicio and self.inicio_vigencia_outorga is not None:
            if self.inicio_vigencia_outorga < data_base_inicio:
                self.data_base_inicio_contagem = data_base_inicio
            if self.inicio_vigencia_outorga > data_base_inicio:
                self.data_base_inicio_contagem = self.inicio_vigencia_outorga
        elif self.data_comeco_operacao < data_base_inicio and self.inicio_vigencia_outorga is None:
            self.data_base_comeco_operacao = data_base_inicio
