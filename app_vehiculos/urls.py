from django.urls import path
from app_vehiculos.views import (
 listar_camioneta, listar_automovil, listar_motocicleta, crear_camioneta, crear_automovil, crear_motocicleta, buscar_camionetas, buscar_automoviles, buscar_motocicletas
)


urlpatterns = [
   path('camionetas/', listar_camioneta, name="listar_camionetas"),
   path('automoviles/', listar_automovil, name="listar_automoviles"),
   path('motocicletas/', listar_motocicleta, name="listar_motocicletas"),
   path("crear-camioneta/", crear_camioneta, name="crear_camioneta"),
   path("crear-automovil/", crear_automovil, name="crear_automovil"),
   path("crear-motocicleta/", crear_motocicleta, name="crear_motocicleta"),
   path("buscar-camionetas/", buscar_camionetas, name="buscar_camionetas"),
   path("buscar-autos/", buscar_automoviles, name="buscar_automoviles"),
   path("buscar-motos/", buscar_motocicletas, name="buscar_motocicletas"),



]

