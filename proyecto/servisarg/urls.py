from django.urls import include, path
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="index"),
    path('admin/', admin.site.urls),
    path('trabajadores_categoria/<int:categoria_id>/', views.trabajadores_categoria, name='trabajadores_categoria'),
    path('acerca',views.acerca, name= "acerca"),
    path('alta_trabajador',views.alta_trabajador, name ="alta_trabajador"),
    path('lista_trabajadores',views.lista_trabajadores, name="lista_trabajadores"),
    path('contacto',views.contacto, name="contacto"),
    path('alta_oficio',views.alta_oficio, name ="oficios"),
    path('trabajador/<int:id>/', views.trabajador_detalle, name='trabajador_detalle'),
    path('categorias',views.categorias, name="categorias"),
    path('register/',views.register_user, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('listar_oficios/', views.listar_oficios, name='listar_oficios'),
    path('crear/', views.alta_oficio, name='crear_oficio'),
    path('modificar/<int:oficio_id>/', views.modificar_oficio, name='modificar_oficio'),
    path('eliminar/<int:oficio_id>/', views.eliminar_oficio, name='eliminar_oficio'),
    path('chat/', include(('chat.urls', 'chat'), namespace='chat')),
    path('mensajes/',  views.room, name='room'),
    path('modificar-usuario/<int:pk>/', views.modificar_user, name='modificar_usuario'),
    path('lista_consultas/', views.lista_consultas, name='lista_consultas'),
    path('consulta/<int:consulta_id>/', views.detalle_consulta, name='detalle_consulta'),
	path('verificar_mensajes_nuevos/', views.verificar_mensajes_nuevos, name='verificar_mensajes_nuevos'),


] 