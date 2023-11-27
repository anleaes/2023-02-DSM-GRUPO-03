from django.db import models

# Create your models here.

class Ficha(models.Model):
    vacinas = models.TextField('Vacinas', max_length=100)
    remedios = models.TextField('Remedios', max_length=100)
    castracao = models.CharField('Castrado', max_length=15)
    
    class Meta:
        verbose_name = 'Ficha Medica'
        verbose_name_plural = 'Fichas Medicas'
        ordering =['id']

    def __str__(self):
        return self.name

