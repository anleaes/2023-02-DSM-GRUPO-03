from .models import Animaisadotado
from rest_framework import serializers

class AnimaisadotadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animaisadotado
        fields = '__all__'