from .models import Adocao
from rest_framework import serializers

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adocao
        fields = '__all__'
