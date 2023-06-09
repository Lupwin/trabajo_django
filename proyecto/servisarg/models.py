from django.db import models




class Persona(models.Model):
    nombre = models.CharField(max_length=130, verbose_name = "Nombre")
    apellido = models.CharField(max_length=130, verbose_name = "Apellido")
    fecha_nacimiento = models.DateField(verbose_name = "Fecha de Nacimiento")
    dni = models.IntegerField(verbose_name = "DNI",unique=True)
    direccion = models.CharField(max_length =250 , verbose_name="Dirección")
    telefono = models.IntegerField( verbose_name = "Telefono",unique=True )
    email =models.EmailField(verbose_name = "Email", unique=True)
    clave = models.CharField(max_length= 20 ,verbose_name = "Contraseña")
    
    class Meta:
        abstract = True
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} - DNI {self.dni} Oficio {self.oficio}"
    
    
class Oficio(models.Model):
    nombre = models.CharField(max_length=130, verbose_name="Nombre del Oficio")

    def __str__(self):
        return self.nombre



class Trabajador(Persona):
    usuario = models.CharField(max_length= 100, verbose_name= "Usuario", unique = True)
    oficio = models.ForeignKey(Oficio, on_delete=models.SET_NULL, null=True, related_name='trabajadores')
    foto = models.ImageField(upload_to='trabajador_photos/', blank=True, null=True)
    descripcion = models.TextField(max_length=700, verbose_name="Descripción")

   
class Contacto(models.Model):
    nombre = models.CharField(max_length = 100, verbose_name= "Nombre")
    apellido = models.CharField(max_length = 100, verbose_name="Apellido")    
    email =models.EmailField(verbose_name="Email")
    fecha_consulta = models.DateField(verbose_name = "Fecha de consulta")
    tipo = models.CharField(max_length = 100,verbose_name= "tipo de contacto")
    mensaje = models.CharField(max_length = 100,verbose_name ="Mensaje")
    



    

