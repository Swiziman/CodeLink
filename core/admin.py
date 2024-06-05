from django.contrib import admin
from .models import registro_movimentacao
from django.db import models

admin.site.register(registro_movimentacao)
#class registro_movimentacao(models.Model):
 #   campo_exemplo = models.CharField(max_length=255, help_text="Dica: Este é um campo de exemplo. Insira as informações conforme necessário.")
    # outros campos