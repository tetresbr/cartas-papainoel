from rest_framework import viewsets
from cartas.api import serializers
from cartas import models

class CartasViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CartasSerializers
    queryset = models.Cartas.objects.all()