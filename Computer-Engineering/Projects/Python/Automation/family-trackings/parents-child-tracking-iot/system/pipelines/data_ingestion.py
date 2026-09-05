class IngestionPipeline:
    @staticmethod
    def capture(payload: dict) -> dict:
        """
        Registra e valida a integridade estrutural do pacote de telemetria recebido.
        """
        if not payload.get("device_id"):
            raise ValueError("Payload inválido: device_id ausente.")
        
        # Adiciona metadados de recepção
        payload["ingestion_status"] = "received"
        return payload
