from django.db import models
import uuid

class registro_movimentacao(models.Model):
    ALARM_CHOICES = [

    (1, 'Área não autorizada'),

    (2, 'Pareamento não autorizado'),

]
    alarme_id = models.IntegerField(choices=ALARM_CHOICES)
    RASPBERRY_CHOICES = [

    (1, 'Recepção'),
    (2, 'Pediatria'),
    (3, 'Quarto 1'),
    (4, 'Quarto 2'),
    (5, 'Quarto 3'),
    (6, 'Quarto 4'),
    (7, 'Sala de Raio-X'),
    (8, 'Ortopedia'),
    (9, 'Laboratório 1'),
    (10, 'Emergência'),
    (11, 'Neurologia'),
    (12, 'Cardiologia'),
    (13, 'Laboratório 02'),
    (14, 'Corredor Principal'),
    (15, 'Banheiros'),

]
    raspberry_id = models.IntegerField(choices=RASPBERRY_CHOICES)
    OPÇÃO_1_UUID = uuid.UUID('0338a66a-d0a4-4f17-b597-66966f91459e')
    OPÇÃO_2_UUID = uuid.UUID('94c36e91-be9a-4df2-9537-a6e4ea889428')
    OPÇÃO_3_UUID = uuid.UUID('ccf69731-7e47-4b1d-b08c-53ba75f10da7')
    OPÇÃO_4_UUID = uuid.UUID('40230a85-c78e-43b1-b6d7-dc4831f401c3')
    OPÇÃO_5_UUID = uuid.UUID('a6ff4bb9-f145-48cd-8d50-058f6e70c76c')
    OPÇÃO_6_UUID = uuid.UUID('0d24aac7-8959-4f37-b4f2-0f4e8d96803a')
    OPÇÃO_7_UUID = uuid.UUID('a8c46414-bc95-4466-8853-5ca6d74ee4ba')
    OPÇÃO_8_UUID = uuid.UUID('5606bc86-3093-48a8-8d04-01bfae84b1c4')
    #OPÇÃO_9_UUID = uuid.UUID('85375a57-309f-45db-9337-61144cb18e7a')
    OPÇÃO_10_UUID = uuid.UUID('047e6009-bece-47bc-8574-b0922c157c58')
    #OPÇÃO_11_UUID = uuid.UUID('d99a2c83-7b18-429d-bc59-bfd6f19fe535')
    
    OPCOES = (
        (OPÇÃO_1_UUID, 'Raquel'),
        (OPÇÃO_2_UUID, 'Marlene'),  
        (OPÇÃO_3_UUID, 'Renato'),  
        (OPÇÃO_4_UUID, 'Ezequiel'),  
        (OPÇÃO_5_UUID, 'Alana'),  
        (OPÇÃO_6_UUID, 'Cauã'),  
        (OPÇÃO_7_UUID, 'Maia'),  
        (OPÇÃO_8_UUID, 'Camila'),  
        #(OPÇÃO_9_UUID, '9'),  
        (OPÇÃO_10_UUID, 'Juliana'),  
        #(OPÇÃO_1_UUID, '11'),  
    )
    dispositivo_id = models.UUIDField(choices=OPCOES)
    closed = models.BooleanField(null=True, default=True)
  