from django.shortcuts import render
from .models import Animaisadotado
from rest_framework import viewsets
from .serializer import AnimaisadotadoSerializer

# Create your views here.

class AdocaoViewSet(viewsets.ModelViewSet):
    queryset = Animaisadotado.objects.all()
    serializer_class = AnimaisadotadoSerializer