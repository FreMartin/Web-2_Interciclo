from django.shortcuts import render, redirect

from .models import Libros

from .forms import LibroForm

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def list(request):
    libros = Libros.objects.all()
    print(libros)
    return render(request, 'libros/lista_libros.html', {'libros': libros})

def detail(request, id):
    libro = Libros.objects.get(id=id)
    return render(request, 'libros/detalle_libro.html', {'libro': libro})

def new(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('lista')
    return render(request, 'libros/nuevo_libro.html',  {'formulario': formulario})