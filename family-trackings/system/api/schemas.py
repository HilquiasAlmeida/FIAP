from pydantic import BaseModel, Field
from typing import Optional

class TelemetryPayload(BaseModel):
    device_id: str = Field(..., description="Identificador único do dispositivo IoT do membro da família")
    latitude: float = Field(..., ge=-90.0, le=90.0, description="Coordenada geográfica de latitude")
    longitude: float = Field(..., ge=-180.0, le=180.0, description="Coordenada geográfica de longitude")
    battery_level: int = Field(..., ge=0, le=100, description="Nível percentual da bateria do dispositivo")
    timestamp: str = Field(..., description="Momento da captura do dado em formato ISO-8601")
  
