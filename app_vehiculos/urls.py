from django.urls import path
from app_vehiculos.views import listar_vehiculos


urlpatterns = [
   path('vehiculos/', listar_vehiculos),
]