from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from sistema import metodos as cd

# Create your views here.
def inicio(request):
    return render(request, "paginas/inicio.html")

@login_required
def crear_user_view(request):
    if request.method == "POST":
        continuar = cd.mbox()
        if continuar:
            username = request.POST.get("username")
            password = request.POST.get("password")

            if username and password:
                User.objects.create_user(username=username, password=password, is_superuser=0, is_staff=0, is_active=1, date_joined=timezone.now())
                cd.mboxsuccess()
        else:
            cd.mboxcancel()
    return render(request, "paginas/users/crear.html")


def modificar_user_view(request, username=None):   
    user = User.objects.filter(username=username).first()
    if request.method == "POST":
        if user is None:
            cd.mboxvacio()
            return render(request, "paginas/users/modificar.html", {"user": None})
        password = request.POST.get("password")
        email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")

        if password:
            user.set_password(password)
        if email:
            user.email = email
        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name
        continuar = cd.mbox()
        if continuar:
            user.save()
            cd.mboxsuccess()
            return render(request, "paginas/users/buscar.html")
        else:
            cd.mboxcancel()
    if user is None:
        return render(request, "paginas/users/modificar.html")
    else:
        return render(request, "paginas/users/modificar.html", {"user": user})

def buscar_user_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        user = User.objects.filter(username=username).first()
        if user is None:
            cd.mboxvacio()
            return render(request, "paginas/users/buscar.html", {"user": None})
        else:
            return render(request, "paginas/users/buscar.html", {"user": user})          
    return render(request, "paginas/users/buscar.html", {"user": None})

def eliminar_user_view(request, username=None):
    user = User.objects.filter(username=username).first()
    print("entro a eliminar")
    if request.method == "GET":
        print("entro a GET")
        continuar = cd.mbox()
        if continuar:
            user.delete()
            cd.mboxsuccess()
            return render(request, "paginas/users/buscar.html")
        else:
            cd.mboxcancel()
    if user is None:
        print("entro a POST none")
        return render(request, "paginas/users/buscar.html")
    else:
        print("entro a POST")
        return render(request, "paginas/users/buscar.html", {"user": user})

def success_url_view(request):
    return render(request, "paginas/success-url.html")
