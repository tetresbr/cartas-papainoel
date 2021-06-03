# Generated by Django 3.2.4 on 2021-06-02 23:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cartas',
            fields=[
                ('id_carta', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=255)),
                ('remetente', models.CharField(max_length=255)),
                ('mensagem', models.CharField(max_length=1000)),
                ('enviado_em', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
