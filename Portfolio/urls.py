from django.urls import path
from django.contrib import admin

from Portfolio.views import Inicio, listar_gato, listar_transito


urlpatterns = [
    path('Inicio/', Inicio, name="saludo"),
    path('gatos/', listar_gato, name="listar_gatos"),
    path('transitos/', listar_transito, name="listar_transitos"),
    path('admin/', admin.site.urls),
]