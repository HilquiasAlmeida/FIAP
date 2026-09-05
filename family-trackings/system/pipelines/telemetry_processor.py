class TelemetryProcessor:
    @staticmethod
    def process(data: dict) -> dict:
        """
        Executa o tratamento numérico e normalização das coordenadas de GPS.
        """
        lat = round(data.get("latitude", 0.0), 6)
        lon = round(data.get("longitude", 0.0), 6)
        
        data["latitude"] = lat
        data["longitude"] = lon
        data["processed"] = True
        
        return data
