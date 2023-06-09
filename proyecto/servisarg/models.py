from datetime import datetime
from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import AbstractUser

# Create your models here.
# Recuerda ejecutar las migraciones después de agregar estos cambios a tus modelos:
# py manage.py makemigrations
# py manage.py migrate


# class Persona(AbstractUser):
#     nombre = models.CharField(max_length=130, verbose_name = "Nombre")
#     apellido = models.CharField(max_length=130, verbose_name = "Apellido")
#     fecha_nacimiento = models.DateField(verbose_name = "Fecha de Nacimiento")
#     dni = models.IntegerField(verbose_name = "DNI",unique=True)
#     direccion = models.CharField(max_length =250 , verbose_name="Dirección")
#     telefono = models.IntegerField( verbose_name = "Telefono",unique=True, validators=[MaxValueValidator(9999999999)])
#     email =models.EmailField(verbose_name = "Email", unique=True)
#     clave = models.CharField(max_length= 20 ,verbose_name = "Contraseña")
    
#     class Meta:
#         abstract = True
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} - DNI {self.dni} Oficio {self.oficio}"
    
    
class Oficio(models.Model):
    nombre = models.CharField(max_length=130, verbose_name="Nombre del Oficio")

    def __str__(self):
        return self.nombre

from django.contrib.auth.models import User, Group, Permission

class Trabajador(AbstractUser):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='trabajador')
    # nombre = models.CharField(max_length=130, verbose_name = "Nombre")
    # username = models.CharField(max_length=130, verbose_name = "UserName")
    # apellido = models.CharField(max_length=130, verbose_name = "Apellido")
    fecha_nacimiento = models.DateField(verbose_name = "Fecha de Nacimiento")
    dni = models.IntegerField(verbose_name = "DNI",unique=True)
    direccion = models.CharField(max_length =250 , verbose_name="Dirección")
    telefono = models.IntegerField( verbose_name = "Telefono",unique=True, validators=[MaxValueValidator(9999999999)])
    # email =models.EmailField(verbose_name = "Email", unique=True)
    # clave = models.CharField(max_length= 20 ,verbose_name = "Contraseña")
    oficio = models.ForeignKey(
        Oficio, on_delete=models.SET_NULL, null=True, related_name='trabajadores'
    )
    descripcion = models.TextField(max_length=700, verbose_name="Descripción")
    # password = models.DateField(default=datetime.now)
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='trabajador_groups'  # Cambia el nombre del acceso inverso
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='trabajador_user_permissions'  # Cambia el nombre del acceso inverso
    )
class Contacto(models.Model):
    nombre = models.CharField(max_length = 100, verbose_name= "Nombre")
    apellido = models.CharField(max_length = 100, verbose_name="Apellido")    
    email =models.EmailField(verbose_name="Email")
    fecha_consulta = models.DateField(verbose_name = "Fecha de consulta")
    tipo = models.CharField(max_length = 100,verbose_name= "tipo de contacto")
    mensaje = models.CharField(max_length = 100,verbose_name ="Mensaje")
    
    



class Mensaje(models.Model):
    emisor = models.ForeignKey(Trabajador, on_delete=models.CASCADE, related_name='mensajes_enviados')
    receptor = models.ForeignKey('Cliente', on_delete=models.CASCADE, related_name='mensajes_recibidos')
    contenido = models.ManyToManyField('ContenidoMensaje', related_name='mensajes')
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensaje de {self.emisor} a {self.receptor}"

class Cliente(models.Model):
    trabajador = models.ForeignKey(
        Trabajador, on_delete=models.CASCADE, related_name='clientes'
    )

    def __str__(self):
        return f"Cliente de {self.trabajador.nombre} {self.trabajador.apellido}"

class ContenidoMensaje(models.Model):
    contenido = models.TextField(verbose_name="Contenido del mensaje")

    def __str__(self):
        return self.contenido

    

#     # Resto de los campos del modelo Trabajador

# class CustomGroup(Group):
#     # Agrega campos personalizados si es necesario

#     class Meta:
#         proxy = True
#         verbose_name = 'Custom Group'
#         verbose_name_plural = 'Custom Groups'

# class CustomPermission(Permission):
#     # Agrega campos personalizados si es necesario

#     class Meta:
#         proxy = True
#         verbose_name = 'Custom Permission'
#         verbose_name_plural = 'Custom Permissions'



# ----------------------------------------------------------
# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, Group, Permission,PermissionsMixin

# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('El email debe ser proporcionado')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(email, password, **extra_fields)
# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     groups = models.ManyToManyField(Group, related_name='custom_users', blank=True)
#     user_permissions = models.ManyToManyField(Permission, related_name='custom_users', blank=True)

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'email'
#     # Otros campos requeridos

#     class Meta:
#         verbose_name = 'Usuario personalizado'
#         verbose_name_plural = 'Usuarios personalizados'

#     def __str__(self):
#         return self.email

# class CustomGroup(Group):
#     class Meta:
#         proxy = True

# class CustomPermission(Permission):
#     class Meta:
#         proxy = True
