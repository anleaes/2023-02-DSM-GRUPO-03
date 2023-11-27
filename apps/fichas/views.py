from django.shortcuts import render
from .models import Ficha
from rest_framework import viewsets
from .serializer import FichaSerializer

# Create your views here.

class FichaViewSet(viewsets.ModelViewSet):
    queryset = Ficha.objects.all()
    serializer_class = FichaSerializer  
    
    