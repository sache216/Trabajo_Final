from django.urls import path
from app_vehiculos.views import listar_camioneta, listar_automovil, listar_motocicleta


urlpatterns = [
   #path('vehiculos/', listar_vehiculos, name="listar_vehiculos"),
   path('camionetas/', listar_camioneta, name="listar_vehiculos"),
   path('automoviles/', listar_automovil, name="listar_vehiculos_2"),
   path('motocicletas/', listar_motocicleta, name="listar_vehiculos_3"),
   
]