from django.urls import path
from django.contrib import admin

from Portfolio.views import (Inicio, listar_gato, listar_transito,contacto,crear_transito, buscar_transito,crear_gato,crear_adopcion,Gracias)


urlpatterns = [
    path('Inicio/', Inicio, name="saludo"),
    path('gatos/', listar_gato, name="listar_gatos"),
    path('transitos/', listar_transito, name="listar_transitos"),
    path('contactanos/', contacto, name="contacto"),
    path('admin/', admin.site.urls),
    path('form-transito/',crear_transito, name="crear_transitos"),
    path('buscar-transito/', buscar_transito, name="buscar_transito"),
    path('form-gato/',crear_gato, name="crear_gatos"),
    path('form-adopcion/',crear_adopcion, name="crear_adopta"),
    path('Agradecimiento/', Gracias, name="gracias"),
]