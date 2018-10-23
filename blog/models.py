from django.db import models
from django.shortcuts import render
from django.utils import timezone

class publicacion(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(
            default=timezone.now)
    fecha_publicacion = models.DateTimeField(
            blank=True, null=True)

#procedimiento almacenado pero en funcion
    def publish(self):
        self.fecha_publicacion = timezone.now()
        self.save()

#sirve para definir cual de todos los campos muestra en los resumenes.
def __str__(self):
        return self.titulo      #mostar el tituo solo el campo seleccioado
# Create your models here.
