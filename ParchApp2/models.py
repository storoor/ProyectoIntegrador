from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
Economy = [('Menor que 50k','Menor que 50k'), ('Entre 50k y 150k','Entre 50k y 150k'), ('Más de 150k','Más de 150k')]
Zone = [('Envigado','Envigado'), ('Itagui','Itagui'),('Comuna 1, Popular','Comuna 1, Popular'), ('Comuna 2, Santa cruz','Comuna 2, Santa cruz'),('Comuna 3, Manrique', 'Comuna 3, Manrique'),('Comuna 4, Aranjuez','Comuna 4, Aranjuez'), ('Comuna 5, Castilla','Comuna 5, Castilla'),('Comuna 9, Buenos aires','Comuna 9, Buenos aires'), ('Comuna 10 - La Candelaria', 'Comuna 10 - La Candelaria'),('Comuna 11, Laureles - Estadio','Comuna 11, Laureles - Estadio'),('Comuna 13 - San javier','Comuna 13 - San javier'),('Comuna 14, Poblado',' Comuna 14, Poblado'),('Jardin','Jardin'),('Guatapé','Guatapé'),('La estrella','La estrella'),('Sabaneta','Sabaneta')]
Category = [('Discoteca','Discoteca'),('Restaurante','Restaurante'),('Mirador','Mirador'),('Centro Comercial','Centro Comercial'), ('Parche al aire libre','Parche al aire libre'), ('Tour', 'Tour'),('Museo','Museo')]
Age = [('Menor de edad','Menor de edad'),('Mayor de edad','Mayor de edad'),('Todas las edades a partir de los 8 años','Todas las edades a partir de los 8 años')]


class lugar(models.Model):
    nombre = models.CharField(max_length = 50,default='x')
    foto = models.ImageField(upload_to='Parcha-App/images/')
    LvlEconomico = models.CharField(max_length=50, choices=Economy,default='')
    descripcion = models.CharField(max_length = 500,default='')
    Zona = models.CharField(max_length = 50, choices= Zone,default='')
    categoria = models.CharField(max_length= 50, choices= Category,default='')
    Edad = models.CharField(max_length=50, choices= Age,default='')
    urlMapa=models.URLField(default='') 
    edad = models.CharField(max_length=50, choices= Age,default='')
    urlubi=models.URLField(default='')

    
    def __str__(self):
        
        return self.nombre
    


