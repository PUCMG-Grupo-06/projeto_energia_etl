from django.db import models


class RegiaoAdministrativa(models.Model):
    regiao_id = models.AutoField(db_column='regiao_administrativa_id', primary_key=True)
    nome = models.CharField(db_column='nome', max_length=120, blank=False, null=False)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'regiao_administrativa'
        managed = True
