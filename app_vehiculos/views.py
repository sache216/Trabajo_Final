from django.shortcuts import render
from app_vehiculos.models import Camioneta, Automovil, Motocicleta

# Create your views here.

def listar_camioneta(request):
    contexto = {
        "vehiculos": Camioneta.objects.all()
    }
    http_response = render(
        request=request,
        template_name='app_vehiculos/lista_vehiculos.html',
        context=contexto,
    )
    return http_response


def listar_automovil(request):
    contexto = {
        "vehiculos": Automovil.objects.all()
    }
    http_response = render(
        request=request,
        template_name='app_vehiculos/lista_vehiculos.html',
        context=contexto,
    )
    return http_response

def listar_motocicleta(request):
    contexto = {
        "vehiculos": Motocicleta.objects.all()
    }
    http_response = render(
        request=request,
        template_name='app_vehiculos/lista_vehiculos.html',
        context=contexto,
    )
    return http_response
