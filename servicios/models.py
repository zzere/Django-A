from django.db import models

# Create your models here.

class Servicio(models.Model):
    titulo      = models.CharField(max_length=50)
    contenido   = models.CharField(max_length=50)
    imagen      = models.ImageField(upload_to='servicios') #cap 34
    created     = models.DateTimeField(auto_now_add=True) #crea la fecha de forma automatica, la fecha en que es creado
    updated     = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'

    def __str__(self):
        return self.titulo
