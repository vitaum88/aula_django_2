from django.db import models


class Cidade(models.Model):
    nome = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    pais = models.CharField(max_length=255)
    lat = models.FloatField()
    long = models.FloatField()

    def __str__(self):
        return f"{self.nome} - {self.estado} - {self.pais}"


class Previsao(models.Model):
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    data = models.DateField()
    temp_max = models.FloatField()
    temp_min = models.FloatField()

    def __str__(self):
        return f"{self.cidade} - {self.data}"
