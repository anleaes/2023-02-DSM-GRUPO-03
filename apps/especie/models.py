from django.db import models

# Create your models here.

class Especie(models.Model):
    tipo = models.CharField('Tipo', max_length=15)
    raca = models.TextField('Raça', max_length=50)
    porte = models.CharField('Porte', max_length=20)

    class Meta:
        verbose_name = 'especie'
        verbose_name_plural = 'especies'
        ordering =['id']

    def __str__(self):
        return self.name
