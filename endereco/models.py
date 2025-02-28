from django.db import models

class Address(models.Model):
    cep = models.CharField(max_length=9)
    logradouro = models.CharField(max_length=50)
    bairro = models.CharField(max_length=30)
    localidade = models.CharField(max_length=30)
    uf = models.CharField(max_length=2)


# Create your models here.
