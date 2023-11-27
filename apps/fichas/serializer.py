from .models import Ficha
from rest_framework import serializers

class FichaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ficha
        fields = '__all__'
        
        

