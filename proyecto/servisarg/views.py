from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TrabajadorForm, ContactoForm, OficioForm
from .models import Trabajador, Oficio
from django.contrib.auth import login
# Create your views here.

def index(request):
        
    contex = {}
    
    lista_categorias = Oficio.objects.all().order_by("nombre")
    
    contex["lista_categorias"] = lista_categorias

    return render(request,'servisarg/index.html', contex)

def trabajadores_categoria(request, categoria_id):
    context = {}
    
    categoria = Oficio.objects.get(id=categoria_id)
    trabajadores = Trabajador.objects.filter(oficio=categoria)
    
    context["categoria"] = categoria
    context["trabajadores"] = trabajadores
    
    return render(request, 'servisarg/trabajadores_categoria.html', context)

def acerca(request):
    return render(request,'servisarg/acerca.html')

def alta_trabajador(request):
    if request.method == "POST":
        alta_trabajador_form = TrabajadorForm(request.POST, user=request.user) 
        if alta_trabajador_form.is_valid:
            trabajador=alta_trabajador_form.save()  #  guarda automáticamente el trabajador
            # print(trabajador)
            messages.success(request, 'Usuario dado de alta exitosamente') 
            return redirect("lista_trabajadores")
    else:
        alta_trabajador_form = TrabajadorForm(user=request.session)
    contex = {'form': alta_trabajador_form}
    return render(request, 'servisarg/alta_trabajador.html', contex)

def lista_trabajadores(request):
    context = {}
    
    listado_trabajadores = Trabajador.objects.all().order_by("oficio")
    context["listado_trabajadores"] = listado_trabajadores
    
    return render(request, 'servisarg/lista_trabajadores.html',context)




def contacto(request):
    if request.method == "POST":
        contacto_form = ContactoForm(request.POST) 
        if contacto_form.is_valid():
            contacto_form.save() 
            messages.success(request, 'Consulta enviada exitosamente')
            return redirect("index")
    else:
        contacto_form = ContactoForm()
    contex = {'form': contacto_form}
    return render(request, 'servisarg/contacto.html', contex)


def alta_oficio(request):
    if request.method == "POST":
        alta_oficio_form = OficioForm(request.POST) 
        if alta_oficio_form.is_valid():
            alta_oficio_form.save()  #  guarda automáticamente el trabajador
            messages.success(request, 'Usuario dado de alta exitosamente') 
            return redirect("categorias")
    else:
        alta_oficio_form = OficioForm()
    contex = {'form': alta_oficio_form}
    return render(request, 'servisarg/alta_oficio.html', contex)

def trabajador_detalle(request, id):
    # Obtener el trabajador correspondiente al ID
    trabajador = Trabajador.objects.get(id=id)
    print(Trabajador)
    # Pasar el trabajador a la plantilla para mostrar la información
    context = {'trabajador': trabajador}
    return render(request, 'servisarg/trabajador_detalle.html', context)

def categorias(request):
    
    context = {}
    
    lista_categorias = Oficio.objects.all().order_by("nombre")
    
    context["lista_categorias"] = lista_categorias
    
    return render(request, 'servisarg/categorias.html',context)
from django.contrib.auth.forms import UserCreationForm
def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            return redirect('contacto')  # Redirige al usuario a la página de inicio de sesión
    else:
        form = UserCreationForm()
    return render(request, 'servisarg/register.html', {'form': form})

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def user_login(request):
    mensaje_error=""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirige al usuario a la página de inicio
        else:
            mensaje_error='Por favor, introduzca un nombre de usuario y clave correctos. Observe que ambos campos pueden ser sensibles a mayúsculas.'

    else:
        print("sdf")
        form = AuthenticationForm()
        mensaje_error=''

    context = {
        'form': form,
        'mensa':mensaje_error
    }
    return render(request, 'servisarg/login.html', context)