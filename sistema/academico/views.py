from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
def inicio(request):
    return render(request, "paginas/inicio.html")

@login_required
def principal(request):
    return render(request, 'paginas/principal.html')

@login_required
def academico(request):
    return render(request, 'paginas/academico.html')

@login_required
def contacto(request):
    return render(request, 'paginas/contacto.html')

@login_required
def estudiantes(request):
    return render(request, 'paginas/estudiantes.html')

@login_required
def profesores(request):
    return render(request, 'paginas/profesores.html')
