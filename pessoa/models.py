from django.db import models


class Pessoa(models.Model):
    nome_completo = models.CharField(max_length=256)
    data_nascimento = models.DateField(null=False)
    ativa = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.nome_completo