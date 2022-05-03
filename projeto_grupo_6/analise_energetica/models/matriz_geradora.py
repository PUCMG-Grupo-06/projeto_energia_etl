from django.db import models


class MatrizGeradora(models.Model):
    matriz_geradora_id = models.AutoField(db_column='matriz_geradora_id', primary_key=True)
    nome = models.CharField(db_column='nome', max_length=120, blank=False, null=False)
    tipo_fonte = models.CharField(db_column='tipo_fonte', max_length=120, blank=False, null=False)

    def __str__(self):
        return f'({self.tipo_fonte}) {self.nome}'

    class Meta:
        db_table = 'matriz_geradora'
        managed = True
