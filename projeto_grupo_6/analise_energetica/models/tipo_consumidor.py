from django.db import models


class TipoConsumidor(models.Model):
    tipo_consumidor_id = models.AutoField(db_column='tipo_consumidor_id', primary_key=True)
    nome = models.CharField(db_column='nome', max_length=100, blank=False, null=False)
    residencial = models.BooleanField(db_column='residencial', null=False, default=True)

    class Meta:
        db_table = 'tipo_consumidor'
        managed = True
