from .matriz_geradora import MatrizGeradora
from .unidade_federativa import UnidadeFederativa
from django.db import models


class ProducaoEnergia(models.Model):
    producao_id = models.AutoField(db_column='producao_energia_id', primary_key=True)
    matriz = models.ForeignKey(
        MatrizGeradora,
        db_column='matriz_geradora_id',
        on_delete=models.DO_NOTHING,
        null=False)
    periodo_inicio = models.DateTimeField(db_column='periodo_inicio', null=True)
    periodo_fim = models.DateTimeField(db_column='periodo_fim', null=True)
    energia_produzida = models.FloatField(db_column='energia_produzida', null=False)
    unidade_federativa = models.ForeignKey(
        UnidadeFederativa,
        db_column='unidade_federativa_id',
        on_delete=models.DO_NOTHING,
        null=False)

    class Meta:
        db_table = 'producao_energia'
        managed = True
