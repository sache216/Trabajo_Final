from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Camioneta(models.Model):
    #atributos de clases
    marca = models.CharField(max_length=256)
    modelo = models.CharField(max_length=256)
    fabricacion = models.IntegerField()
    cv= models.IntegerField(blank=True)
    peso = models.IntegerField(blank=True)
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.fabricacion})({self.cv})({self.peso})"

class Automovil(models.Model):
    marca = models.CharField(max_length=256)
    modelo = models.CharField(max_length=256)
    fabricacion = models.IntegerField()
    cv = models.IntegerField(blank=True)
    peso = models.IntegerField(blank=True)
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.fabricacion})({self.cv})({self.peso})"


class Motocicleta(models.Model):
    marca = models.CharField(max_length=256)
    modelo = models.CharField(max_length=256)
    fabricacion = models.IntegerField()
    cv = models.IntegerField(blank=True, null=True)
    peso = models.IntegerField(blank=True, null=True)
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.fabricacion})({self.cv})({self.peso})"