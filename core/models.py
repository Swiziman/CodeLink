from django.db import models

class registro_movimentacao(models.Model):
    #data_hora = models.DateTimeField(auto_now_add=False)
    alarme_id = models.IntegerField()
    raspberry_id = models.IntegerField()
    dispositivo_id = models.CharField(max_length=36)
    closed = models.BooleanField(null=True, default=True)

#class registro_movimentacao(models.Model):
    #campo_exemplo = models.CharField(max_length=255, help_text="Dica: Este é um campo de exemplo. Insira as informações conforme necessário.")
    # outros campos

   # def __str__(self):
   #     return self.campo_exemplo