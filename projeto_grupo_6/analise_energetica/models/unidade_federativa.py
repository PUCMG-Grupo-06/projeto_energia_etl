from .regiao_administrativa import RegiaoAdministrativa
from django.db import models


class UnidadeFederativa(models.Model):
    uf_id = models.AutoField(db_column='unidade_federativa_id', primary_key=True)
    nome = models.CharField(db_column='nome', max_length=100, blank=False, null=False)
    sigla = models.CharField(db_column='sigla', max_length=3, blank=True, null=True)
    regiao = models.ForeignKey(
        RegiaoAdministrativa,
        db_column='regiao_administrativa_id',
        on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f'{self.nome} - {self.sigla}' if self.sigla is not None else self.nome

    class Meta:
        db_table = 'unidade_federativa'
        managed = True
