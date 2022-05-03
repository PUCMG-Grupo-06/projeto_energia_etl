from .models import (
    MatrizGeradora,
    RegiaoAdministrativa,
    Tarifa,
    TipoConsumidor,
    UnidadeFederativa)
from django.contrib import admin


admin.site.register(MatrizGeradora)
admin.site.register(RegiaoAdministrativa)
admin.site.register(Tarifa)
admin.site.register(TipoConsumidor)
admin.site.register(UnidadeFederativa)
