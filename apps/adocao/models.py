from django.db import models
from ong.models import Ong
from pessoa.models import Pessoa
from animal.models import Animal

# Create your models here.

class Adocao (models.model) :
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    data_adocao = models.DateField('Data Adocao', auto_now=False, auto_now_add=False)
    dono = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    doador = models.ForeignKey(Ong, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Adocao'
        verbose_name_plural = 'Adocaos'
        ordering =['id']
        
    def __str__(self):
        return "%s" % (self.data_adocao) 