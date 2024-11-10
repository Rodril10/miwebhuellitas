from django.db import models


class Eventos(models.Model):
    NOMBRE_EVENTO = models.CharField(max_length=200)
    FECHA = models.DateField()
    DESCRIPCION = models.CharField(max_length=500)
    IMAGEN = models.ImageField(upload_to='Eventos', null=True)
    def __str__(self):
        return f"{self.NOMBRE_EVENTO} "    
    
    
class Testimonios(models.Model):
    NOMBRE_APELLIDO = models.CharField(max_length=200)
    ACCION = models.CharField(max_length=200)
    TESTIMONIO = models.TextField(blank=False, null=False)
    def __str__(self):
        return f"{self.ACCION} -  {self.NOMBRE_APELLIDO}"    
    
class Adopta(models.Model):
    NOMBRE = models.CharField(max_length=200)
    ESPECIE = models.CharField(max_length=200)
    IMAGEN = models.ImageField(upload_to='ADOPTA', null=True)
    def __str__(self):
        return f"{self.NOMBRE}"
    
class Dona(models.Model):
    NOMBRE = models.CharField(max_length=200)
    VALOR = models.IntegerField()
    FECHA_DONACION = models.DateTimeField(auto_now_add=True)
    METODO_PAGO = models.CharField(max_length=50)
    COMENTARIOS = models.TextField(blank=True, null=True)
    USER = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    

    def __str__(self):
        return f"{self.NOMBRE} - {self.VALOR}"

    
    
        

# Create your models here.
