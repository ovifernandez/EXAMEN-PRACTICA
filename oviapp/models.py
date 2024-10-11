from django.db import models

# Create your models here.
class Moto(models.Model):
    name = models.CharField(
        unique=True,
        max_length=50,
        null=False,
        blank=False,)
    slug = models.SlugField(
        unique=True,
        max_length=50,
        null=False,
        blank=False,)
    description = models.TextField(
        unique=True,
        max_length=50,
        null=False,
        blank=False,)
    
    precio = models.IntegerField()

class Marca(models.Model):
    name = models.CharField(
        unique=True,
        max_length=50,
        null=False,
        blank=False,)
    description = models.TextField(
        unique=True,
        max_length=50,
        null=False,
        blank=False,)
    slug = models.SlugField(
        unique=True,
        max_length=50,
        null=False,
        blank=False,)
    motos = models.ManyToManyField(
        Moto,
        related_name='marcas'
    )

