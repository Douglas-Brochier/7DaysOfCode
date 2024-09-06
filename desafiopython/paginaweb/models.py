from django.db import models

class Personagem(models.Model):
    id = models.AutoField(primary_key=True)
    nome_original = models.CharField(max_length=255)
    nome_traduzido = models.CharField(max_length=255)
    afiliacao_original = models.CharField(max_length=255)
    afiliacao_traduzida = models.CharField(max_length=255)

    def __str__(self):
        return self.nome_traduzido  # Isso faz com que o nome traduzido apareça como representação do objeto.
