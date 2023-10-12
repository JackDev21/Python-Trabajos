from django.urls import path
from . import views
from .views import detalle_nomina

app_name = "nominas"

urlpatterns = [
    path('', views.nominas, name='home'),
    path('nominas/', views.nominas, name='nominas'),
    path("inicio/", views.inicio),
    path("crear/", views.crear_nomina, name="crear_nomina"),
    path('lista/', views.lista, name='lista'),
    path("detalle/<int:id_nomina>/", views.detalle_nomina, name="detalle_nomina"),
    # otras rutas aquí
]
