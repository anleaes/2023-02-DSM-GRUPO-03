from django.db import models
from adocaos.models import Adocao
from pessoas.models import Pessoa
from animais.models import Animal

# Create your models here.

class Animaisadotado (models.model) :
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    data_adocao = models.ForeignKey(Adocao, on_delete=models.CASCADE)
    dono = models.ForeignKey(Pessoa, on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Animaisadotado'
        verbose_name_plural = 'Animaisadoados'
        ordering =['id']

    def __str__(self):
        return self.animal