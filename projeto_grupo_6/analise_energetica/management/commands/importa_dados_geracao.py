# -*- coding:utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from analise_energetica.models import (
    Consumidor,
    Consumo,
    MatrizGeradora,
    ProducaoEnergia,
    RegiaoAdministrativa,
    Tarifa,
    TipoConsumidor,
    UnidadeFederativa)


class ModeloGeracaoCsv:
    def __init__(self):
        pass


class Command(BaseCommand):
    help = 'Importa dados da base de origem para base de tratamento'

    def add_arguments(self, parser):
        parser.add_argument('--directory', nargs='+', type='str')

    def handle(self, *args, **kwargs):
        pass
