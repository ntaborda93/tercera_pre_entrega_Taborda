from django.urls import path
from django.contrib import admin

from Portfolio.views import (Inicio, listar_gato, listar_transito,contacto,crear_transito, buscar_transito)


urlpatterns = [
    path('Inicio/', Inicio, name="saludo"),
    path('gatos/', listar_gato, name="listar_gatos"),
    path('transitos/', listar_transito, name="listar_transitos"),
    path('contactanos/', contacto, name="contacto"),
    path('admin/', admin.site.urls),
    path('form-transito/',crear_transito, name="crear_transitos"),
    path('buscar-transito/', buscar_transito, name="buscar_transito")
]