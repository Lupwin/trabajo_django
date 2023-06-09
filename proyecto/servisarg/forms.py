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
class MockUser(AbstractUser):
    class Meta:
        abstract = True

class TrabajadorForm(forms.ModelForm):
    print(forms.ModelForm)
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    dni = forms.IntegerField(max_value=999999999,widget=forms.TextInput(attrs={'class': 'form-control','type': 'number'}))
    # clave = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    oficio = oficio = forms.ModelChoiceField(queryset=Oficio.objects.all())

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')  # Obtener el usuario logeado
        super().__init__(*args, **kwargs)
        self.fields['oficio'].widget.attrs.update({'class': 'form-control'})
        self.user = user  # Asignar el usuario a un atributo de la instancia del formulario
        # Agrega otros campos y estilos personalizados si es necesario
    def save(self, commit=True):
            print("antes de guardar")
            instance = super().save(commit=False)
            # instance.usuario = self.cleaned_data['user']  # Establecer el usuario logeado en el campo 'usuario'
            user=User.objects.get(username=self.user)

            print("Username:", user.username)
            print("Email:", user.email)
            print("Nombre completo:", user.get_full_name())
            print("Es staff:", user.is_staff)
            print("Es superusuario:", user.is_superuser)
            # y otros atributos del objeto User

            # También puedes acceder a relaciones como grupos y permisos
            print("Grupos:")
            for group in user.groups.all():
                print(group.name)

            print("Permisos:")
            for permission in user.user_permissions.all():
                print(permission.codename)
            instance.username = self.user  # Establecer el usuario logeado en el campo 'usuario'
            # instance.username = user.username
            instance.email = user.email
            instance.first_name = user.first_name
            instance.last_name = user.last_name
            instance.last_login = user.last_login
            instance.usuario_id = user.id
            instance.password =user.last_login

            # print("nani",instance)
            if commit:
                instance.save()
            return instance
    class Meta:
        exclude = ('usuario','user_permissions','groups','is_active','date_joined','is_staff','password','last_login','is_superuser','first_name','first_name','last_name','username','email')
        # Resto de tus opciones de configuración del formulario
        model = Trabajador
        fields = '__all__'
        widgets = {
            # 'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            # 'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control', 'type': 'number'}),
            # 'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'oficio': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-select', 'rows': 3, 'style': 'resize: none;'}),
            # 'usuario': forms.TextInput(attrs={'class': 'form-control'})

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
            if False:
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
    # fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    # dni = forms.IntegerField(max_value=999999999)
    # clave = forms.CharField(widget=forms.PasswordInput)
    # oficio = oficio = forms.ModelChoiceField(queryset=Oficio.objects.all())
    
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
    
# class CustomUserCreationForm(UserCreationForm):
#     email = forms.EmailField(required=True)

#     class Meta(UserCreationForm.Meta):
#         fields = ['username', 'email']

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.is_staff = False  # No es superusuario
#         if commit:
#             user.save()
#         return user