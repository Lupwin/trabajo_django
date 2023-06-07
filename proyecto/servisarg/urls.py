from django.urls import path
from . import views
from django.contrib import admin

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
    path('categorias',views.categorias, name="categorias")

]
