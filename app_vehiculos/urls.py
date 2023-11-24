from django.urls import path
from app_vehiculos.views import (
 listar_camioneta, listar_automovil, listar_motocicleta, crear_camioneta, crear_automovil,
 crear_motocicleta, buscar_camionetas, buscar_automoviles, buscar_motocicletas, eliminar_motocicleta,
 eliminar_camioneta, eliminar_automovil, editar_camioneta, editar_automovil, editar_motocicleta, CamionetaDetailView, AutomovilDetailView, MotocicletaDetailView,
 CamionetaDeleteView, AutomovilDeleteView, MotocicletaDeleteView
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
   
   path('eliminar-motocicleta/<int:id>/', eliminar_motocicleta, name="eliminar_motocicleta"),
   path('eliminar-camioneta/<int:id>/', eliminar_camioneta, name="eliminar_camioneta"),
   path('eliminar-automovil/<int:id>/', eliminar_automovil, name="eliminar_automovil"),
   
   path('editar-camioneta/<int:id>/', editar_camioneta, name="editar_camioneta"),
   path('editar-automovil/<int:id>/', editar_automovil, name="editar_automovil"),
   path('editar-motocicleta/<int:id>/', editar_motocicleta, name="editar_motocicleta"),
   
   path("camionetas/<int:pk>/", CamionetaDetailView.as_view(), name="ver_camioneta"),
   path("automovil/<int:pk>/", AutomovilDetailView.as_view(), name="ver_automovil"),
   path("motocicleta/<int:pk>/", MotocicletaDetailView.as_view(), name="ver_motocicleta"),
   
   path("eliminar-camioneta/<int:pk>/", CamionetaDeleteView.as_view(), name="eliminar_camioneta"),
   path("eliminar-automovil/<int:pk>/", AutomovilDeleteView.as_view(), name="eliminar_automovil"),
   path("eliminar-motocicleta/<int:pk>/", MotocicletaDeleteView.as_view(), name="eliminar_motocicleta"),
   


]

