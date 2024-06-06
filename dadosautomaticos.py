import time
import random
from django.utils import timezone
from core.models import registro_movimentacao

def gerar_dados():
    while True:
        # Gere dados aleatórios
        alarme_id = random.choice([1, 2])
        raspberry_id = random.choice([1, 2, 3, 4])
        dispositivo_id = random.choice(['0338a66a-d0a4-4f17-b597-66966f91459e', '94c36e91-be9a-4df2-9537-a6e4ea889428', 'ccf69731-7e47-4b1d-b08c-53ba75f10da7', '40230a85-c78e-43b1-b6d7-dc4831f401c3'])

        # Insira os dados no banco de dados
        registro_movimentacao.objects.create(
            alarme_id=alarme_id,
            raspberry_id=raspberry_id,
            dispositivo_id=dispositivo_id,
            closed=True,
        )

        # Espere 20 segundos
        time.sleep(20)

if __name__ == "__main__":
    gerar_dados()
