from django.shortcuts import render, redirect
from django.urls import reverse
from app_vehiculos.models import Camioneta, Automovil, Motocicleta
from app_vehiculos.forms import VehiculosFormulario

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

def crear_camioneta(request):
    if request.method == "POST":
       data = request.POST
       camioneta = Camioneta(marca=data['marca'], modelo=data['modelo'],fabricacion=data['fabricacion'], cv=data['cv'], peso=data['peso'])
       camioneta.save()
       url_exitosa = reverse('listar_camionetas')
       return redirect(url_exitosa)
    else:
        http_response = render(
            request=request,
            template_name='app_vehiculos/formulario_camioneta.html',   
        )
        return http_response

def crear_automovil(request):
    if request.method == "POST":
       data = request.POST
       automovil = Automovil(marca=data['marca'], modelo=data['modelo'],fabricacion=data['fabricacion'], cv=data['cv'], peso=data['peso'])
       automovil.save()
       url_exitosa = reverse('listar_automoviles')
       return redirect(url_exitosa)
    else:
        http_response = render(
            request=request,
            template_name='app_vehiculos/formulario_automovil.html',
        )
        return http_response



def crear_motocicleta(request):
    if request.method == "POST":
       data = request.POST
       motocicleta = Motocicleta(marca=data['marca'], modelo=data['modelo'],fabricacion=data['fabricacion'], cv=data['cv'], peso=data['peso'])
       motocicleta.save()
       url_exitosa = reverse('listar_motocicletas')
       return redirect(url_exitosa)
    else:
        http_response = render(
            request=request,
            template_name='app_vehiculos/formulario_motocicleta.html',
        )
        return http_response
