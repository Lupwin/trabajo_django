from django.db.models import Max
from django.conf import settings
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import TrabajadorForm, ConsultaReclamoSugerenciaForm, OficioForm, CustomUserCreationForm
from .models import Trabajador, Oficio,ConsultaReclamoSugerencia
from chat.models import Conversation, Message
from django.db.models import Count
from django.templatetags.static import static
from django.core.cache import cache

from django.contrib.auth import login
# Create your views here.

def is_trabajador(user):
    autorizado=Trabajador.objects.filter(username=user).exists() 
    return autorizado

def is_trabajador_or_not_staff(user):
    if not user.is_authenticated:
        return False
    is_trabajador = Trabajador.objects.filter(username=user).exists()
    no_es_staff = not user.is_staff
    return is_trabajador or no_es_staff


def index(request):

    contex = {}

    lista_categorias = Oficio.objects.annotate(num_trabajadores=Count('trabajadores')).order_by("nombre")

    contex["lista_categorias"] = lista_categorias

    return render(request, 'servisarg/index.html', contex)


def trabajadores_categoria(request, categoria_id):
    context = {}
    categoria = Oficio.objects.get(id=categoria_id)
    trabajadores = Trabajador.objects.filter(oficio=categoria)
    context["categoria"] = categoria
    context["trabajadores"] = trabajadores
    return render(request, 'servisarg/trabajadores_categoria.html', context)


def acerca(request):
    return render(request, 'servisarg/acerca.html')




@user_passes_test(lambda user: user.is_authenticated, login_url='login')
def alta_trabajador(request):
    if request.method == "POST":
        alta_trabajador_form = TrabajadorForm(request.POST, user=request.user)
        if alta_trabajador_form.is_valid():
            # guarda automáticamente el trabajador
            trabajador = alta_trabajador_form.save(request=request)
            messages.success(request, 'Usuario dado de alta exitosamente')
            return redirect("lista_trabajadores")
    else:
        alta_trabajador_form = TrabajadorForm(user=request.session)
    contex = {'form': alta_trabajador_form}
    return render(request, 'servisarg/alta_trabajador.html', contex)

@user_passes_test(is_trabajador_or_not_staff, login_url='login')
def lista_trabajadores(request):
    context = {}
    listado_trabajadores = Trabajador.objects.all().order_by("oficio")
    context["listado_trabajadores"] = listado_trabajadores
    context['media_url'] = settings.MEDIA_URL
    return render(request, 'servisarg/lista_trabajadores.html', context)


def contacto(request):
    if request.method == "POST":
        contacto_form = ConsultaReclamoSugerenciaForm(request.POST)
        print("validacion: ",contacto_form.is_valid())
        if contacto_form.is_valid():
            contacto_form.save()
            messages.success(request, 'Consulta enviada exitosamente')
            return redirect("index")
    else:
        contacto_form = ConsultaReclamoSugerenciaForm()
    contex = {'form': contacto_form}
    return render(request, 'servisarg/contacto.html', contex)

@user_passes_test(lambda user: user.is_authenticated, login_url='login')
def trabajador_detalle(request, id):
    # Obtener el trabajador correspondiente al ID
    trabajador = Trabajador.objects.get(id=id)
    receptor = trabajador.id
    # ** El formato para el acceso de la sala sera= id.cliente-id-trabajador
    # todo se tiene que determinar de acuerdo el type user
    emisor = User.objects.get(id=request.user.id)
    room_name = ''

    if not trabajador:
        room_name = f"{str(receptor)}_{str(emisor.id)}"
    else:
        room_name = f"{str(emisor.id)}_{str(receptor)}"
    # Pasar el trabajador a la plantilla para mostrar la información
    context = {'trabajador': trabajador,
               'room_name': room_name}
    return render(request, 'servisarg/trabajador_detalle.html', context)


def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'servisarg/register.html', {'form': form})

@user_passes_test(lambda user: user.is_authenticated, login_url='login')
def modificar_user(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == 'POST':
        form = CustomUserCreationForm(
            request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            # Autenticar y volver a iniciar sesión al usuario
            user = authenticate(request, username=user.username,
                                password=form.cleaned_data['password1'])
            login(request, user)
            return render(request, 'servisarg/index.html')
    else:
        form = CustomUserCreationForm(instance=user)
    context = {'form': form}
    return render(request, 'servisarg/register.html', context)


def user_login(request):
    mensaje_error = ""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirige al usuario a la página de inicio
                return redirect('index')
        else:
            mensaje_error = 'Por favor, introduzca un nombre de usuario y clave correctos. Observe que ambos campos pueden ser sensibles a mayúsculas.'

    else:
        form = AuthenticationForm()
        mensaje_error = ''

    context = {
        'form': form,
        'mensa': mensaje_error
    }
    return render(request, 'servisarg/login.html', context)


# alta oficio
@user_passes_test(lambda user: user.is_staff, login_url='login')
def alta_oficio(request):
    if request.method == "POST":
        alta_oficio_form = OficioForm(request.POST)
        if alta_oficio_form.is_valid():
            alta_oficio_form.save()  # guarda automáticamente el trabajador
            messages.success(request, 'Usuario dado de alta exitosamente')
            return redirect('listar_oficios')
    else:
        alta_oficio_form = OficioForm()
    contex = {'form': alta_oficio_form}
    return render(request, 'servisarg/alta_oficio.html', contex)


# listar todos las categorias
@user_passes_test(lambda user: user.is_staff, login_url='login')
def categorias(request):
    lista_categorias = Oficio.objects.all().order_by("nombre")
    context = {"lista_categorias": lista_categorias}
    return render(request, 'servisarg/categorias.html', context)

@user_passes_test(lambda user: user.is_staff, login_url='login')
def listar_oficios(request):
    oficios = Oficio.objects.all()
    return render(request, 'servisarg/categoria/listar.html', {'oficios': oficios})

@user_passes_test(lambda user: user.is_staff, login_url='login')
def modificar_oficio(request, oficio_id):
    oficio = Oficio.objects.get(id=oficio_id)
    if request.method == 'POST':
        form = OficioForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            oficio.nombre = nombre
            oficio.save()
            return redirect('listar_oficios')
    else:
        form = OficioForm(initial={'nombre': oficio.nombre})
        # Agregar placeholder
        form.fields['nombre'].widget.attrs['placeholder'] = oficio.nombre
    return render(request, 'servisarg/alta_oficio.html', {'form': form, 'oficio': oficio})

@user_passes_test(lambda user: user.is_staff, login_url='login')
def eliminar_oficio(request, oficio_id):
    oficio = Oficio.objects.get(id=oficio_id)
    oficio.delete()
    return redirect('listar_oficios')


# ! no permitir que otros usuarios externos e internos ingresen a salas que no le coorresponde en chat, esta el user
@user_passes_test(is_trabajador_or_not_staff, login_url='login')
def room(request):
    room_name = Conversation.objects.filter(user2=request.user.username)
    # *preguntar si es user o trabajar
    isClient=Trabajador.objects.filter(username=request.user.username).exists()
    print(isClient)
    if not isClient:
        # si es true, voy a traer las salas de user 1, que corresponden a clientes
        room_name = Conversation.objects.filter(user1=request.user.username)
    for conversation in room_name:
        # Accede a los campos existentes de la conversación
        user1 = conversation.user1
        user_client = User.objects.get(username=user1)
        if not isClient:
            # si es true, voy a traer la informacion de Trabajador(user_2), por que corresponden a clientes
            user2 = conversation.user2
            user_client = User.objects.get(username=user2)
        conversation.last_name = user_client.last_name
        conversation.first_name = user_client.first_name
        conversation.is_photo_default = False
        if user_client.photo:
            conversation.foto = user_client.photo
        else:
            conversation.is_photo_default = True

        # print("nani",conversation.foto)
        conversation.ultima_fecha = Message.objects.filter(
        conversation_id=conversation.id).aggregate(Max('timestamp'))['timestamp__max']
    context = {
        'room_name': room_name,
        # Agrega cualquier otro dato necesario para el template
    }
    return render(request, 'servisarg/lista_mensajes.html', context)


# todo hacer que solo puedan ingresar el admin
@user_passes_test(lambda user: user.is_staff, login_url='login')
def lista_consultas(request):
    consultas = ConsultaReclamoSugerencia.objects.order_by('-fecha_creacion')
    return render(request, 'servisarg/contacto/lista_consulta.html', {'consultas': consultas})

@user_passes_test(lambda user: user.is_staff, login_url='login')
def detalle_consulta(request, consulta_id):
    consulta = ConsultaReclamoSugerencia.objects.get(pk=consulta_id)
    consulta.leido = True
    ConsultaReclamoSugerencia.objects.filter(pk=consulta_id).update(leido=True)
    return render(request, 'servisarg/contacto/detalle_consulta.html', {'consulta': consulta})


from django.http import JsonResponse

def verificar_mensajes_nuevos(request):
    # Verificar si hay mensajes nuevos para el usuario actual
    # es T?
    # request.user.username
    # es C?
    # Id para buscar en la sala 
    total_mensajes_antes = cache.get('total_mensajes_antes')
    trabajador=Trabajador.objects.filter(usuario_id=request.user.id)
    if trabajador:
        conversaciones= Conversation.objects.filter(user2=request.user.username)
    else:
        conversaciones= Conversation.objects.filter(user1=request.user.username)
    # [1,3,5]
    total_mensajes=0
    for conversation_db in conversaciones:
        num_messages = Message.objects.filter(conversation=conversation_db.id).count()
        total_mensajes=total_mensajes+num_messages

    msj_nuevos=False
    if total_mensajes_antes is None or total_mensajes_antes == total_mensajes:
        if cache.get('accedio'):
            # no se enviarion nungun mensaje
            # cache.set('total_mensajes_antes', total_mensajes)
            cache.set('acedio',False)
        msj_nuevos=True    
    # Actualizar el valor anterior del caché
    cache.set('total_mensajes_antes', total_mensajes)       
    data = {
           'tiene_mensajes_nuevos': msj_nuevos,
        }
    print(data)
    # Devolver la respuesta JSON
    return JsonResponse({'data': data})