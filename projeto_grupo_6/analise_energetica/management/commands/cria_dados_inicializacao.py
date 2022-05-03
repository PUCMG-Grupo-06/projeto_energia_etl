# -*- coding:utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from analise_energetica.models import RegiaoAdministrativa, UnidadeFederativa


class Command(BaseCommand):
    help = 'Inicializa banco com dados de regiões e unidades federativas'

    def handle(self, *args, **kwargs):
        print('Inicializando base')
