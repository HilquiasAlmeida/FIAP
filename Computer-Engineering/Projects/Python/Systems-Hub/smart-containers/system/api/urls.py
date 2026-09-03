from django.urls import path
from .views import TelemetriaCreateView

urlpatterns = [
    path('telemetria/', TelemetriaCreateView.as_view(), name='api-telemetria'),
]
