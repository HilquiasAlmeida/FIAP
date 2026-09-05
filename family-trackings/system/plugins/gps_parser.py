class GPSParser:
    @staticmethod
    def parse_nmea_sentence(sentence: str) -> dict:
        """
        Simulador de parser para sentenças NMEA padrão de módulos GPS.
        """
        if not sentence.startswith("$GPGGA"):
            return {"error": "Sentença NMEA não suportada ou corrompida."}
        
        parts = sentence.split(",")
        return {
            "fix_quality": parts[6] if len(parts) > 6 else "0",
            "satellites": parts[7] if len(parts) > 7 else "0"
        }
