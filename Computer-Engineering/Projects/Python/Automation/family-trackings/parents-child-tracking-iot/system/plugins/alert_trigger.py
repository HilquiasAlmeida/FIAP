class AlertTrigger:
    @staticmethod
    def evaluate_battery_threshold(battery_level: int) -> bool:
        """
        Verifica se o nível de bateria está crítico (< 15%).
        """
        CRITICAL_LEVEL = 15
        if battery_level <= CRITICAL_LEVEL:
            return True
        return False
