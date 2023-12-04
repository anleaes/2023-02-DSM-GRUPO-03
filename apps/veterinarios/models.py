from django.db import models

# Create your models here.

class Veterinario(models.Model):
    name = models.CharField('Nome', max_length=50)
    telefone = models.CharField('Telefone', max_length=20)
    CRMV = models.CharField('CRMV', max_length=20)

    class Meta:
        verbose_name = 'Veterinario'
        verbose_name_plural = 'Veterinarios'
        ordering =['id']

    def __str__(self):
        return self.nome