from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("principal/", views.principal, name="principal"),
    path("academico/", views.academico, name="academico"),
    path("contacto/", views.contacto, name="contacto"),
    path("estudiantes/", views.estudiantes, name="estudiantes"),
    path("profesores/", views.profesores, name="profesores"),
]
