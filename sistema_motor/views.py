from django.http import HttpResponse
from django.shortcuts import render

def Bienvenida (request):
    saludo = "Te damos la bienvenida a WEB_MOTORBOAT"
    respuesta_http = HttpResponse (saludo)
    return respuesta_http