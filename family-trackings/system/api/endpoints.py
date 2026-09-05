from fastapi import FastAPI, HTTPException, status
from api.schemas import TelemetryPayload
from pipelines.data_ingestion import IngestionPipeline
from pipelines.telemetry_processor import TelemetryProcessor

app = FastAPI(
    title="Family Trackings - Core API",
    version="1.0.0",
    description="API de recepção e processamento de telemetria IoT para monitoramento familiar."
)

@app.post("/api/v1/telemetry", status_code=status.HTTP_201_CREATED)
def receive_telemetry(payload: TelemetryPayload):
    try:
        # Etapa de Ingestão de Dados Brutos
        raw_data = IngestionPipeline.capture(payload.dict())
        
        # Etapa de Processamento e Filtragem
        processed_data = TelemetryProcessor.process(raw_data)
        
        return {
            "status": "success",
            "message": "Telemetria processada e armazenada com sucesso.",
            "data": processed_data
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    return {"status": "online", "system": "Family Trackings Engine"}
