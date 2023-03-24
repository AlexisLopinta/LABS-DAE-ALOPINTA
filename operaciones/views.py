from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def sumar(request, n1, n2):
    resultado = int(n1) + int(n2)
    return HttpResponse(f"La suma de {n1} + {n2} = {resultado}")

def restar(request, n1, n2):
    resultado = int(n1) - int(n2)
    return HttpResponse(f"La resta de {n1} - {n2} = {resultado}")

def multiplicar(request, n1, n2):
    resultado = int(n1) * int(n2)
    return HttpResponse(f"La multiplicación de {n1} x {n2} = {resultado}")