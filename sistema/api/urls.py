from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("crear-user/", views.crear_user_view, name="crearUser"),
    path("success-url/", views.success_url_view, name="successUrl"),
    path("modificar-user/", views.modificar_user_view, name="modificarUser"),
    path("buscar-user/", views.buscar_user_view, name="buscarUser"),
    path("modificar-user/<str:username>/", views.modificar_user_view, name="modificarUserParam"),
    path("buscar-user/<str:username>", views.eliminar_user_view, name="eliminarUserParam"),
]
