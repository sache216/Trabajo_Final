from django.http import HttpResponse
from django.shortcuts import render

def Bienvenida (request):
    Saludo = "Te damos la bienvenida a WEB_MOTORBOAT"
    respuesta_http = HttpResponse (saludo)
    return respuesta_http

def saludar_con_html(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='inicio.html',
        context=contexto,
    )
    return http_response