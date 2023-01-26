from django.db import models

class Gato(models.Model):
    nombre = models.CharField(max_length=64)
    color_de_ojos = models.CharField(max_length=64)
    color_pelaje =  models.CharField(max_length=64)
    genero = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.nombre}"


class transito(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    email = models.EmailField()
    provincia = models.CharField(max_length=256)
    localidad = models.CharField(max_length=256)
    codigo_postal = models.IntegerField()
    posecion = models.BooleanField()
    bio = models.TextField(null=True)
    

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

class adopcion(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    email = models.EmailField()
    provincia = models.CharField(max_length=256)
    localidad = models.CharField(max_length=256)
    tipo_vivienda = models.CharField(max_length=256)
    
