from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q
from app_vehiculos.models import Camioneta, Automovil, Motocicleta
from app_vehiculos.forms import MotocicletaFormulario, CamionetaFormulario, AutomovilFormulario

# Create your views here.

def listar_camioneta(request):
    contexto = {
        "vehiculos": Camioneta.objects.all()
    }
    http_response = render(
        request=request,
        template_name='app_vehiculos/listar_camioneta.html',
        context=contexto,
    )
    return http_response

def listar_automovil(request):
    contexto = {
        "vehiculos": Automovil.objects.all()
    }
    http_response = render(
        request=request,
        template_name='app_vehiculos/listar_auto.html',
        context=contexto,
    )
    return http_response

def listar_motocicleta(request):
    contexto = {
        "vehiculos": Motocicleta.objects.all()
    }
    http_response = render(
        request=request,
        template_name='app_vehiculos/listar_motos.html',
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

def buscar_camionetas(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        camionetas = Camioneta.objects.filter(
            Q(marca__icontains=busqueda) | Q(modelo__contains=busqueda)
        )
        contexto = {
            "vehiculos": camionetas,
        }
        http_response = render(
            request=request,
            template_name='app_vehiculos/listar_camioneta.html',
            context=contexto,
        )
        return http_response
    
def buscar_automoviles(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        autos = Automovil.objects.filter(
            Q(marca__icontains=busqueda) | Q(modelo__contains=busqueda)
        )
        contexto = {
            "vehiculos": autos,
        }
        http_response = render(
            request=request,
            template_name='app_vehiculos/listar_auto.html',
            context=contexto,
        )
        return http_response
    
def buscar_motocicletas(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        motos = Motocicleta.objects.filter(
            Q(marca__icontains=busqueda) | Q(modelo__contains=busqueda)
        )
        contexto = {
            "vehiculos": motos, 
        }
        http_response = render(
            request=request,
            template_name='app_vehiculos/listar_motos.html',
            context=contexto,
        )
        return http_response
    
def eliminar_motocicleta(request, id): #borra sin confirmacion
   motocicleta = Motocicleta.objects.get(id=id)
   if request.method == "POST":
       motocicleta.delete()
       url_exitosa = reverse('listar_motocicletas')
       return redirect(url_exitosa)
   
def eliminar_camioneta(request, id): #borra sin confirmacion
   camioneta = Camioneta.objects.get(id=id)
   if request.method == "POST":
       camioneta.delete()
       url_exitosa = reverse('listar_camionetas')
       return redirect(url_exitosa)
   
def eliminar_automovil(request, id): #borra sin confirmacion
   automovil = Automovil.objects.get(id=id)
   if request.method == "POST":
       automovil.delete()
       url_exitosa = reverse('listar_automoviles')
       return redirect(url_exitosa)


def editar_camioneta(request, id):
    # Obtener la instancia de la camioneta con el ID proporcionado
    camioneta = Camioneta.objects.get(id=id)

    if request.method == "POST":
        # Si la solicitud es de tipo POST, procesar el formulario
        formulario = CamionetaFormulario(request.POST)

        if formulario.is_valid():
            # Si el formulario es válido, obtener los datos y actualizar la instancia de la camioneta
            data = formulario.cleaned_data
            camioneta.marca = data["marca"]
            camioneta.modelo = data["modelo"]
            camioneta.fabricacion = data["fabricacion"]
            camioneta.cv = data["cv"]
            camioneta.peso = data["peso"]
            camioneta.save()

            # Redirigir a la URL exitosa después de la edición
            url_exitosa = reverse('listar_camionetas')
            return redirect(url_exitosa)
    else:  # Si la solicitud es GET, inicializar el formulario con los datos actuales de la camioneta
        inicial = {
            'marca': camioneta.marca,
            'modelo': camioneta.modelo,
            'fabricacion': camioneta.fabricacion,
            'cv': camioneta.cv,
            'peso': camioneta.peso,
        }
        formulario = CamionetaFormulario(initial=inicial)

    # Renderizar el formulario para la edición
    return render(
        request=request,
        template_name='app_vehiculos/formulario_camioneta.html',
        context={'formulario': formulario},
    )
    
def editar_automovil(request, id):
    # Obtener la instancia de la automovil con el ID proporcionado
    automovil = Automovil.objects.get(id=id)

    if request.method == "POST":
        # Si la solicitud es de tipo POST, procesar el formulario
        formulario = AutomovilFormulario(request.POST)

        if formulario.is_valid():
            # Si el formulario es válido, obtener los datos y actualizar la instancia de la automovil
            data = formulario.cleaned_data
            automovil.marca = data["marca"]
            automovil.modelo = data["modelo"]
            automovil.fabricacion = data["fabricacion"]
            automovil.cv = data["cv"]
            automovil.peso = data["peso"]
            automovil.save()

            # Redirigir a la URL exitosa después de la edición
            url_exitosa = reverse('listar_automoviles')
            return redirect(url_exitosa)
    else:  # Si la solicitud es GET, inicializar el formulario con los datos actuales de la automovil
        inicial = {
            'marca': automovil.marca,
            'modelo': automovil.modelo,
            'fabricacion': automovil.fabricacion,
            'cv': automovil.cv,
            'peso': automovil.peso,
        }
        formulario = AutomovilFormulario(initial=inicial)

    # Renderizar el formulario para la edición
    return render(
        request=request,
        template_name='app_vehiculos/formulario_automovil.html',
        context={'formulario': formulario},
    )
    
def editar_motocicleta(request, id):
    # Obtener la instancia de la motocicleta con el ID proporcionado
    motocicleta = Motocicleta.objects.get(id=id)

    if request.method == "POST":
        # Si la solicitud es de tipo POST, procesar el formulario
        formulario = MotocicletaFormulario(request.POST)

        if formulario.is_valid():
            # Si el formulario es válido, obtener los datos y actualizar la instancia de la motocicleta
            data = formulario.cleaned_data
            motocicleta.marca = data["marca"]
            motocicleta.modelo = data["modelo"]
            motocicleta.fabricacion = data["fabricacion"]
            motocicleta.cv = data["cv"]
            motocicleta.peso = data["peso"]
            motocicleta.save()

            # Redirigir a la URL exitosa después de la edición
            url_exitosa = reverse('listar_motocicletas')
            return redirect(url_exitosa)
    else:  # Si la solicitud es GET, inicializar el formulario con los datos actuales de la motocicleta
        inicial = {
            'marca': motocicleta.marca,
            'modelo': motocicleta.modelo,
            'fabricacion': motocicleta.fabricacion,
            'cv': motocicleta.cv,
            'peso': motocicleta.peso,
        }
        formulario = MotocicletaFormulario(initial=inicial)

    # Renderizar el formulario para la edición
    return render(
        request=request,
        template_name='app_vehiculos/formulario_motocicleta.html',
        context={'formulario': formulario},
    )