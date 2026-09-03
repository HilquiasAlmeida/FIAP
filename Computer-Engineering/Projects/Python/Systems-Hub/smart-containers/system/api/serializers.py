from rest_framework import serializers
from .models import Container, Telemetria

class TelemetriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telemetria
        fields = ['id', 'container', 'status_porta', 'latitude', 'longitude', 'temperatura', 'data_hora']
