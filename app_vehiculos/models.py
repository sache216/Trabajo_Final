from django.db import models

# Create your models here.

class Camioneta(models.Model):
    #atributos de clases
    marca = models.CharField(max_length=256)
    modelo = models.CharField(max_length=256)
    fabricacion = models.IntegerField()
    cv= models.IntegerField(blank=True)
    peso = models.IntegerField(blank=True)
    
    def __str__(self):
        return f"{self.marca} ({self.modelo})"

class Automovil(models.Model):
    marca = models.CharField(max_length=256)
    modelo = models.CharField(max_length=256)
    fabricacion = models.IntegerField()
    cv = models.IntegerField(blank=True)
    peso = models.IntegerField(blank=True)
    
    def __str__(self):
        return f"{self.marca} ({self.modelo})"


class Motocicleta(models.Model):
    marca = models.CharField(max_length=256)
    modelo = models.CharField(max_length=256)
    fabricacion = models.IntegerField()
    cv = models.IntegerField(blank=True, null=True)
    peso = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.marca} ({self.modelo})"