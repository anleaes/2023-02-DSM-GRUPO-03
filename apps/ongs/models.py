from django.db import models

# Create your models here.

class Ong(models.Model):
    nome = models.CharField('Nome', max_length=50)
    endereco = models.TextField('Endereco', max_length=100)
    telefone = models.CharField('Telefone', max_length=15)
    email = models.CharField('Email', max_length=50)
    cnpj = models.CharField('CNPJ', max_length=11)
   
    class Meta:
        verbose_name = 'Ong'
        verbose_name_plural = 'Ongs'
        ordering =['id']

    def __str__(self):
        return self.nome
