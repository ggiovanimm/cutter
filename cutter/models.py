from django.db import models

class Cutter(models.Model):
    autoria = models.CharField(max_length=100)  # Ajuste conforme necessário
    titulo = models.CharField(max_length=100, null=True, blank=True)  # Ajuste conforme necessário

    def __str__(self):
        return f"{self.autoria} - {self.titulo}"  # Corrigido para usar 'titulo'

    class Meta:
        ordering = ['autoria']
