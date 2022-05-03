from .regiao_administrativa import RegiaoAdministrativa
from .unidade_federativa import UnidadeFederativa
from django.db import models


class Tarifa(models.Model):
    tarifa_id = models.AutoField(db_column='tarifa_id', primary_key=True)
    periodo_inicio = models.DateTimeField(db_column='periodo_inicio', null=True)
    periodo_fim = models.DateTimeField(db_column='periodo_fim', null=True)
    unidade_federativa = models.ForeignKey(
        UnidadeFederativa,
        db_column='unidade_federativa_id',
        on_delete=models.DO_NOTHING,
        null=True)
    regiao = models.ForeignKey(
        RegiaoAdministrativa,
        db_column='regiao_administrativa_id',
        on_delete=models.DO_NOTHING,
        null=True)
    valor = models.DecimalField(max_digits=6, decimal_places=2, null=False)

    class Meta:
        db_table = 'tarifa'
        managed = True
