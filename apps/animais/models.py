from django.db import models
from especies.models import Especie
from fichas.models import Ficha
from veterinarios.models import Veterinario

# Create your models here.

class Animal(models.Model):
    nome = models.CharField('Nome', max_length=50)
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE)
    ficha = models.ForeignKey(Ficha, on_delete=models.CASCADE)
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animais'
        ordering =['id']

    def __str__(self):
        return self.nome
