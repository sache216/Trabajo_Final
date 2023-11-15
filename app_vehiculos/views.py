from django.shortcuts import render

# Create your views here.

def listar_vehiculos(request):
    contexto = {
        "vehiculos": [
            {"Marca": "Audi", "Modelo": "A8", "fabricacion":2023,"CV": 286},
            {"Marca": "BMW", "Modelo": "X7", "fabricacion":2022,"CV": 352},
            {"Marca": "Mazda", "Modelo": "RX7", "fabricacion":1999,"CV": 265},
            {"Marca": "Toyota", "Modelo": "Corola", "fabricacion":2003,"CV": 131},
        ]
    }
    http_response = render(
        request=request,
        template_name='base.html',
        context=contexto,
    )
    return http_response


