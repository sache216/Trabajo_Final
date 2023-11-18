from django.contrib import admin

# Register your models here.

from app_vehiculos.models import Camioneta, Automovil, Motocicleta

admin.site.register(Camioneta)
admin.site.register(Automovil)
admin.site.register(Motocicleta)
