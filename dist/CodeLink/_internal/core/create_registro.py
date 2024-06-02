# meu_app/create_registro.py
import os
import django

# Configuração do ambiente Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

# Importando o modelo
from core.models import registro_movimentacao
from django.utils import timezone

def criar_registro():
    novo_registro = registro_movimentacao(
        data_hora=timezone.now(),
        alarme_id=2,
        raspberry_id=3,
        dispositivo_id='0338a66a-d0a4-4f17-b597-66966f91459e'
    )
    novo_registro.save()
    print("Novo registro criado e salvo!")

# Chamando a função para criar o registro
criar_registro()
