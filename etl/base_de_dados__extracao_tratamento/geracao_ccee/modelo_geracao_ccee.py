from datetime import date, datetime
from enum import Enum


class RegiaoBrasil:
    def __init__(self, regiao_id: int, nome: str):
        self.regiao_id = regiao_id
        self.nome = nome


class UnidadeFederativa:
    def __init__(self, uf_id: int, nome: str, regiao: RegiaoBrasil):
        self.uf_id = uf_id
        self.nome = nome
        self.regiao = regiao


class GeracaoMesUF:
    data = None

    def __init__(self, mes: int, ano: int, uf: str):
        self.mes = mes
        self.ano = ano
        self.uf = uf
        self.data = datetime(ano, mes, 1, 0, 0, 0).date()


class GeracaoFonteEnergeticaMesUF:
    data = None

    def __init__(self, fonte: str, mes: int, ano: int, uf: str):
        self.fonte = fonte
        self.mes = mes
        self.ano = ano
        self.uf = uf
        self.data = datetime(ano, mes, 1, 0, 0, 0).date()


class GeracaoEmpresaMes:
    data = None

    def __init__(self, empresa: str, mes: int, ano: int):
        self.empresa = empresa
        self.mes = mes
        self.ano = ano
        self.data = datetime(ano, mes, 1, 0, 0, 0)


class GeracaoEmpresaMesUF:
    data = None

    def __init__(self, empresa: str, mes: int, ano: int, uf: str):
        self.empresa = empresa
        self.mes = mes
        self.ano = ano
        self.uf = uf
        self.data = datetime(ano, mes, 1, 0, 0, 0)


class TipoRegimeConcessao(Enum):
    ParticipanteRateioCotas = 1
    NaoParticipanteRateioCotas = 2


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

    def para_pandas(self):
        return {
            'data_dados': self.data_dados,
            'ano': self.ano,
            'mes': self.mes,
            'cod_usina': self.cod_usina,
            'razao_social': self.razao_social,
            'ceg_empreendimento': self.ceg_empreendimento,
            'sigla_ativo': self.sigla_ativo,
            'fonte_energia': self.fonte_energia,
            'participante_mre': self.participante_mre,
            'submercado': self.submercado,
            'uf': self.uf,
            'tipo_despacho_usina': self.tipo_despacho_usina,
            'tipo_registro_concessao': self.tipo_registro_concessao,
            'capacidade_usina': self.capacidade_usina,
            'garantia_fisica': self.garantia_fisica,
            'cod_parcela_usina': self.cod_parcela_usina,
            'sigla_parcela_usina': self.sigla_parcela_usina,
            'ano_mes_evento': self.ano_mes_evento,
            'data_evento': self.data_evento,
            'geracao_centro_gravidade': self.geracao_centro_gravidade,
            'geracao_teste_centro_gravidade': self.geracao_teste_centro_gravidade,
            'geracao_ponto_conexao': self.geracao_ponto_conexao,
            'geracao_teste_ponto_conexao': self.geracao_teste_ponto_conexao,
            'geracao_manutencao_reserva_operativa': self.geracao_manutencao_reserva_operativa,
            'geracao_restricao_operacao_constrained_on': self.geracao_restricao_operacao_constrained_on,
            'geracao_seguranca_energetica': self.geracao_seguranca_energetica,
            'garantia_fisica_centro_gravidade_apurada_lastro': self.garantia_fisica_centro_gravidade_apurada_lastro,
            'garantia_fisica_centro_gravidade': self.garantia_fisica_centro_gravidade,
            'garantia_fisica_modulada_ajustada_centro_gravidade': self.garantia_fisica_modulada_ajustada_centro_gravidade,
            'energia_entregue_ao_mre': self.energia_entregue_ao_mre,
            'energia_recebida_mre': self.energia_recebida_mre,
            'pagamento_mre': self.pagamento_mre,
            'recebimento_mre': self.recebimento_mre
        }
