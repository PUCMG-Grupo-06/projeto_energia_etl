from .regiao_administrativa import RegiaoAdministrativa
from .tipo_consumidor import TipoConsumidor
from .unidade_federativa import UnidadeFederativa
from django.db import models


class Consumidor(models.Model):
    consumidor_id = models.AutoField(db_column='consumidor_id', primary_key=True)
    nome = models.CharField(db_column='nome', max_length=120, blank=False, null=False)
    tipo_do_consumidor = models.ForeignKey(
        TipoConsumidor,
        db_column='tipo_consumidor_id',
        on_delete=models.CASCADE, null=False)
    unidade_federativa = models.ForeignKey(
        UnidadeFederativa,
        db_column='unidade_federativa_id',
        on_delete=models.DO_NOTHING, null=True)
    regiao = models.ForeignKey(
        RegiaoAdministrativa,
        db_column='regiao_administrativa_id',
        on_delete=models.DO_NOTHING, null=True)
    total = models.IntegerField(db_column='total', default=0, null=False)

    def __str__(self):
        return f'({self.tipo_do_consumidor.nome}) {self.nome}'

    class Meta:
        db_table = 'consumidor'
        managed = True
