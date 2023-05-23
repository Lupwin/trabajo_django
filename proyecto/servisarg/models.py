from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=130, verbose_name = "Nombre")
    apellido = models.CharField(max_length=130, verbose_name = "Apellido")
    fecha_nacimiento = models.DateField(verbose_name = "Fecha de Nacimiento")
    dni = models.IntegerField(verbose_name = "DNI",unique=True)
    direccion = models.CharField(max_length =250 , verbose_name="Dirección")
    telefono = models.IntegerField(verbose_name = "Telefono",unique=True )
    email =models.EmailField(verbose_name = "Email", unique=True)
    clave = models.CharField(verbose_name = "Contraseña")
    
    class Meta:
        abstract = True
    
class Oficio(models.Model):
    nombre = models.CharField(max_length=130, verbose_name="Nombre del Oficio")

    def __str__(self):
        return self.nombre

class Trabajador(Persona):
    oficio = models.ForeignKey(
        Oficio, on_delete=models.SET_NULL, null=True, related_name='trabajadores'
    )
    descripcion = models.TextField(max_length=700, verbose_name="Descripción")

class Contacto(models.Model):
    nombre = models.CharField(verbose_name= "Nombre")
    apellido = models.CharField(verbose_name="Apellido")    
    email =models.EmailField(verbose_name="Email")
    fecha_consulta = models.DateField(verbose_name = "Fecha de consulta")
    tipo = models.CharField(verbose_name= "tipo de contacto")
    mensaje = models.CharField(verbose_name ="Mensaje")
    
    


    

