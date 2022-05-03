from .consumidor import Consumidor
from .tarifa import Tarifa
from django.db import models


class Consumo(models.Model):
    consumo_id = models.AutoField(db_column='consumo_id', primary_key=True)
    consumidor = models.ForeignKey(
        Consumidor,
        db_column='consumidor_id',
        on_delete=models.DO_NOTHING,
        null=False)
    consumo = models.FloatField(db_column='consumo', null=False)
    tarifa_aplicada = models.ForeignKey(
        Tarifa,
        db_column='tarifa_id',
        on_delete=models.CASCADE,
        null=True)
    periodo_inicio = models.DateTimeField(db_column='periodo_inicio', null=True)
    periodo_fim = models.DateTimeField(db_column='periodo_fim', null=True)

    class Meta:
        db_table = 'consumo'
        managed = True
