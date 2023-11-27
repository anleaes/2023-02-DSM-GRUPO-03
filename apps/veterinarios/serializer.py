from .models import Veterinario
from rest_framework import serializers

class VeterinarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veterinario
        fields = '__all__'
        
        