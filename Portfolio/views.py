from datetime import datetime

from django.shortcuts import render, redirect
from django.urls import reverse
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

def crear_transito(request):
    if request.method=="POST":
        data=request.POST
        Transito=transito(nombre=data["nombre_transito"],apellido=data["apellido_transito"],email=data["email_transito"],provincia=data["provincia_transito"],localidad=data["localidad_transito"],codigo_postal=data["cp_transito"],posecion=data["posecion_transito"],bio=data["bio_transito"])
        Transito.save()
        return redirect(reverse("listar_transitos"))
    else:
        return render (
            request=request,   
            template_name='Portfolio/formulario_transito.html'
            )