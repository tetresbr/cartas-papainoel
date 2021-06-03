from rest_framework import serializers
from cartas import models

class CartasSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Cartas
        fields = '__all__'