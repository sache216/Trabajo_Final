from django.urls import path
from app_vehiculos.views import listar_camioneta, listar_automovil, listar_motocicleta, crear_camioneta, crear_automovil, crear_motocicleta



urlpatterns = [
   path('camionetas/', listar_camioneta, name="listar_camionetas"),
   path('automoviles/', listar_automovil, name="listar_automoviles"),
   path('motocicletas/', listar_motocicleta, name="listar_motocicletas"),
   path("crear-camioneta/", crear_camioneta, name="crear-camioneta"),
   path("crear-automovil/", crear_automovil, name="crear-automovil"),
   path("crear-motocicleta/", crear_motocicleta, name="crear-motocicleta"),



]

