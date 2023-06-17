from django import forms
from .models import Trabajador, Oficio, Contacto
from django.core.exceptions import ValidationError
from datetime import date
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

TYPE_CHOICES = [
    ("consulta", "Consulta"),
    ("reclamo","Reclamo"),
    ("sugerencia", "Sugerencia")
]

class TrabajadorForm(forms.ModelForm):
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    dni = forms.IntegerField(max_value=999999999,widget=forms.TextInput(attrs={'class': 'form-control','type': 'number'}))
    clave = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    oficio = forms.ModelChoiceField(queryset=Oficio.objects.all())
    usuario = UserCreationForm()

    
    class Meta:
        model = Trabajador
        fields = '__all__'
    
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control', 'type': 'number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'oficio': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-select', 'rows': 3, 'style': 'resize: none;'}),
            'usuario': forms.TextInput(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control-file'})

            # Agrega widgets y atributos de clase personalizados para los campos invisibles
        }
    def clean_fecha_nacimiento(self):
        fecha_nacimiento = self.cleaned_data.get('fecha_nacimiento')
        
        # Verificar si la fecha de nacimiento es válida
        if fecha_nacimiento:
            # Obtener la fecha actual
            fecha_actual = date.today()
            
            # Calcular la edad a partir de la fecha de nacimiento
            edad = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
            
            # Verificar si la edad es menor a 18 años (mayor de edad)
            if edad <18:
                raise forms.ValidationError("Debes ser mayor de edad para registrarte.")
        
        return fecha_nacimiento   
   
    

class ContactoForm(forms.ModelForm):
    tipo = forms.ChoiceField(choices= TYPE_CHOICES)
    fecha_consulta = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    mensaje = forms.CharField(label= "Mensaje", widget=forms.Textarea(attrs={'class':'area_texto'}))
    class Meta: 
        model = Contacto   
        fields = '__all__'

class OficioForm(forms.ModelForm):
    def clean_nombre(self):
        # Validación del campo nombre
        data = self.cleaned_data["nombre"]
        #TODO: Validar que el oficio no este registrado en la base de datos
        if Oficio.objects.filter(nombre=data):
            raise ValidationError('El oficio que esta ingresando, ya es esta registrado')
        return data   
    class Meta:
        model = Oficio
        fields = '__all__'
    
