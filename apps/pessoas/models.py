from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=50)
    endereco = models.TextField('Endereco', max_length=100)
    telefone = models.CharField('Telefone', max_length=15)
    email = models.CharField('Email', max_length=50)
    cpf = models.CharField('CPF', max_length=11)

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        ordering =['id']

    def __str__(self):
        return self.nome