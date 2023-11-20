from django.shortcuts import render, redirect
from django.urls import reverse
from app_vehiculos.models import Camioneta, Automovil, Motocicleta
from app_vehiculos.forms import MotocicletaFormulario, CamionetaFormulario, AutomovilFormulario

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
       formulario = CamionetaFormulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data  # es un diccionario
           marca = data["marca"]
           modelo = data["modelo"]
           fabricacion = data["fabricacion"]
           cv = data["cv"]
           peso = data["peso"]
           camioneta = Camioneta(marca=data['marca'], modelo=data['modelo'],fabricacion=data['fabricacion'], cv=data['cv'], peso=data['peso'])
           camioneta.save()  # Lo guardan en la Base de datos

           # Redirecciono al usuario a la lista de cursos
           url_exitosa = reverse('listar_camionetas')  
           return redirect(url_exitosa)
   else:  # GET
       formulario = CamionetaFormulario()
   http_response = render(
       request=request,
       template_name='app_vehiculos/formulario_camioneta.html',
       context={'formulario': formulario}
   )
   return http_response

def crear_automovil(request):
   if request.method == "POST":
       formulario = AutomovilFormulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data  # es un diccionario
           marca = data["marca"]
           modelo = data["modelo"]
           fabricacion = data["fabricacion"]
           cv = data["cv"]
           peso = data["peso"]
           automovil = Automovil(marca=data['marca'], modelo=data['modelo'],fabricacion=data['fabricacion'], cv=data['cv'], peso=data['peso'])
           automovil.save()  # Lo guardan en la Base de datos

           # Redirecciono al usuario a la lista de cursos
           url_exitosa = reverse('listar_automoviles')  
           return redirect(url_exitosa)
   else:  # GET
       formulario = AutomovilFormulario()
   http_response = render(
       request=request,
       template_name='app_vehiculos/formulario_automovil.html',
       context={'formulario': formulario}
   )
   return http_response

def crear_motocicleta(request):
   if request.method == "POST":
       formulario = MotocicletaFormulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data  # es un diccionario
           marca = data["marca"]
           modelo = data["modelo"]
           fabricacion = data["fabricacion"]
           cv = data["cv"]
           peso = data["peso"]
           motocicleta = Motocicleta(marca=data['marca'], modelo=data['modelo'],fabricacion=data['fabricacion'], cv=data['cv'], peso=data['peso'])
           motocicleta.save()  # Lo guardan en la Base de datos

           # Redirecciono al usuario a la lista de cursos
           url_exitosa = reverse('listar_motocicletas')  
           return redirect(url_exitosa)
   else:  # GET
       formulario = MotocicletaFormulario()
   http_response = render(
       request=request,
       template_name='app_vehiculos/formulario_motocicleta.html',
       context={'formulario': formulario}
   )
   return http_response