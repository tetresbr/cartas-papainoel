import uuid
from django.db import models
from uuid import uuid4

class Cartas(models.Model):
    id_carta = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    titulo = models.CharField(max_length=255)
    remetente = models.CharField(max_length=255)
    mensagem = models.CharField(max_length=1000)
    enviado_em = models.DateField(auto_now_add=True)
