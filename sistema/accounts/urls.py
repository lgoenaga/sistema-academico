from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("login/", views.loginUser, name="loginUser"),
    path("logout/", views.logoutUser, name="logoutUser"),
    path("registro/", views.registro, name="registro"),
    path("validarLogin/", views.validarLogin_View, name="validarLogin"),
]
