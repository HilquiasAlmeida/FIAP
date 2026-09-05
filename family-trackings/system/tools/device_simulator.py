import time
import requests
from datetime import datetime
from tools.diagnostic_logger import setup_logger

logger = setup_logger("DeviceSimulator")

API_URL = "http://localhost:8000/api/v1/telemetry"

def simulate_device():
    payload = {
        "device_id": "tracker_child_01",
        "latitude": -23.550520,
        "longitude": -46.633308,
        "battery_level": 88,
        "timestamp": datetime.utcnow().isoformat()
    }
    
    try:
        logger.info(f"Enviando telemetria simulada para o dispositivo {payload['device_id']}...")
        response = requests.post(API_URL, json=payload)
        logger.info(f"Resposta da API: {response.status_code} - {response.json()}")
    except requests.exceptions.ConnectionError:
        logger.error("Erro de conexão: Certifique-se de que a API está em execução na porta 8000.")

if __name__ == "__main__":
    logger.info("Iniciando simulador de hardware IoT...")
    while True:
        simulate_device()
        time.sleep(10)
