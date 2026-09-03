from rest_framework import generics
from .models import Telemetria
from .serializers import TelemetriaSerializer

class TelemetriaCreateView(generics.CreateAPIView):
    queryset = Telemetria.objects.all()
    serializer_class = TelemetriaSerializer
