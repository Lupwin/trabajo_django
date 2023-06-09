from django.contrib import admin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import Trabajador, Oficio

# class TrabajadorAdmin(admin.ModelAdmin):
#     list_display = ('nombre', 'apellido', 'fecha_nacimiento', 'dni', 'direccion', 'telefono', 'email')
#     list_filter = ('nombre', 'apellido', 'fecha_nacimiento', 'dni', 'direccion', 'telefono', 'email')
#     search_fields = ('nombre', 'apellido', 'dni', 'email')
#     ordering = ('apellido', 'nombre')

admin.site.register(Trabajador)
admin.site.register(Oficio)
