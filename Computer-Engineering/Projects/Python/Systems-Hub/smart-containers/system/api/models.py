from django.db import models

class Container(models.Model):
    codigo = models.CharField(max_length=50, unique=True, verbose_name="Código do Container")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.codigo

class Telemetria(models.Model):
    container = models.ForeignKey(Container, on_delete=models.CASCADE, related_name='telemetrias')
    status_porta = models.CharField(max_length=20, verbose_name="Status da Porta") # 'ABERTA' ou 'FECHADA'
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    temperatura = models.FloatField(blank=True, null=True)
    data_hora = models.DateTimeField(auto_now_add=True, verbose_name="Data/Hora do Registro")

    def __str__(self):
        return f"Container {self.container.codigo} - {self.status_porta} em {self.data_hora}"
