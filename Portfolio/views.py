from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

from Portfolio.models import Gato, transito


def Inicio(request):
    return render(
        request=request,
        template_name='Portfolio/inicio.html',
    )


def listar_gato(request):
    contexto = {
        'gatos': Gato.objects.all()
    }
    return render(
        request=request,
        template_name='Portfolio/lista_gatito.html',
        context=contexto,
    )


def listar_transito(request):
    contexto = {
        'transito': transito.objects.all()
    }
    return render(
        request=request,
        template_name='Portfolio/lista_transito.html',
        context=contexto,
    )

def contacto(request):
    return render(
        request=request,
        template_name='Portfolio/contacto.html',
    )

def transitoFormulario (request):
    return render (request, "Portfolio/Formulario_transito.html")