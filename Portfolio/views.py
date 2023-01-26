from datetime import datetime

from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse

from Portfolio.models import Gato, transito, adopcion

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

def ver_gato(request,id):
    gatito=Gato.objects.get(id=id)
    contexto = {
        'gatito': gatito
    }
    return render(
        request=request,
        template_name='Portfolio/detalle_gato.html',
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
def ver_transito(request,id):
    transitos=transito.objects.get(id=id)
    contexto = {
        'transitos': transitos
    }
    return render(
        request=request,
        template_name='Portfolio/detalle_transito.html',
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

def editar_transito(request, id):
       if request.method=="POST":
        data=request.POST
        Transito=transito(nombre=data["nombre_transito"],apellido=data["apellido_transito"],email=data["email_transito"],provincia=data["provincia_transito"],localidad=data["localidad_transito"],codigo_postal=data["cp_transito"],posecion=data["posecion_transito"],bio=data["bio_transito"])
        Transito.save()
        return redirect(reverse("listar_transitos"))
       else:
            inicial={
                "nombre_transito":transito.nombre,
                "apellido_transito":transito.apellido,
                "email_transito":transito.email,
                "provincia_transito":transito.provincia,
                "localidad_transito":transito.localidad,
                "cp_transito":transito.codigo_postal,
                "posecion_transito":transito.posecion,
                "bio_transito":transito.bio,
            }
            formulario=Transito.id(initial=inicial)
            return render (
            request=request,   
            template_name='Portfolio/formulario_transito.html',
            context={"formulario":formulario,"es_update":True},
            )

def buscar_transito(request):
    if request.method == "POST":
        data = request.POST
        Transitos = transito.objects.filter(nombre__contains=data['busqueda'])
        contexto = {
            'transito': Transitos
        }
        return render(
            request=request,
            template_name='Portfolio/lista_transito.html',
            context=contexto,
        )

def crear_gato(request):
    if request.method=="POST":
        data=request.POST
        gato=Gato(nombre=data["nombre_gato"],color_de_ojos=data["color_de_ojos_gato"],color_pelaje=data["color_pelaje_gato"],genero=data["genero_gato"])
        gato.save()
        return redirect(reverse("listar_gatos"))
    else:
        return render (
            request=request,   
            template_name='Portfolio/formulario_gato.html'
            )

def crear_adopcion(request):
    if request.method=="POST":
        data=request.POST
        adop=adopcion(nombre=data["nombre_adopta"],apellido=data["apellido_adopta"],email=data["email_adopta"],provincia=data["provincia_adopta"],localidad=data["localidad_adopta"],tipo_vivienda=data["vivienda_adopta"])
        adop.save()
        return redirect(reverse("gracias"))
    else:
        return render (
            request=request,   
            template_name='Portfolio/formulario_adopta.html'
            )

def Gracias(request):
    return render(
        request=request,
        template_name='Portfolio/Gracias.html',
    )