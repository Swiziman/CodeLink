from django.db import models
import uuid

class registro_movimentacao(models.Model):
    ALARM_CHOICES = [

    (1, 'Área não autorizada'),

    (2, 'Pareamento não autorizado'),

]
    alarme_id = models.IntegerField(choices=ALARM_CHOICES)
    RASPBERRY_CHOICES = [

    (1, 'Pediatria'),
    (2, 'Recepção'),
    (3, 'Quarto 1'),
    (4, 'Quarto 2'),
    (5, 'Quarto 3'),
    (6, 'Quarto 4'),
    (7, 'Sala de Raio-X'),
    (8, 'Ortopedia'),
    #(6, 'Quarto 4'),

]
    raspberry_id = models.IntegerField(choices=RASPBERRY_CHOICES)
    OPÇÃO_1_UUID = uuid.UUID('0338a66a-d0a4-4f17-b597-66966f91459e')
    OPÇÃO_2_UUID = uuid.UUID('94c36e91-be9a-4df2-9537-a6e4ea889428')
    OPÇÃO_3_UUID = uuid.UUID('ccf69731-7e47-4b1d-b08c-53ba75f10da7')
    OPÇÃO_4_UUID = uuid.UUID('40230a85-c78e-43b1-b6d7-dc4831f401c3')
   # OPÇÃO_5_UUID = uuid.UUID('94c36e91-be9a-4df2-9537-a6e4ea889428')
   # OPÇÃO_6_UUID = uuid.UUID('94c36e91-be9a-4df2-9537-a6e4ea889428')
   # OPÇÃO_7_UUID = uuid.UUID('94c36e91-be9a-4df2-9537-a6e4ea889428')
    
    OPCOES = (
        (OPÇÃO_1_UUID, 'Raquel'),
        (OPÇÃO_2_UUID, 'Marlene'),  
        (OPÇÃO_3_UUID, 'Renato'),  
        (OPÇÃO_4_UUID, 'Ezequiel'),  
        #(OPÇÃO_5_UUID, '5'),  
        #(OPÇÃO_6_UUID, '6'),  
        #(OPÇÃO_7_UUID, '7'),  
    )
    dispositivo_id = models.UUIDField(choices=OPCOES)
    closed = models.BooleanField(null=True, default=True)
  