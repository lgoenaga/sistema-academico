from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def inicio(request):
    return render(request, "paginas/inicio.html")


def loginUser(request):
    return render(request, "paginas/login.html")

@login_required
def logoutUser(request):
    logout(request)
    return render(request, "paginas/logout.html")

def registro(request):
    return render(request, "paginas/registro.html")

def validarLogin_View(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("principal")
        else:
            return redirect("loginUser")
    else:
        return redirect("loginUser")
