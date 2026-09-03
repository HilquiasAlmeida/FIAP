# boot.py - Executado ao ligar ou reiniciar o ESP32
import network
import esp
import gc

# Desativa mensagens de debug do sistema para economizar recursos
esp.osdebug(None)

# Limpa a memória RAM do ESP32
gc.collect()

# Configurações da sua rede Wi-Fi
SSID = "SEU_WIFI"
PASSWORD = "SUA_SENHA"

def conectar_wifi():
    station = network.WLAN(network.STA_IF)
    station.active(True)
    
    if not station.isconnected():
        print("Conectando ao Wi-Fi...")
        station.connect(SSID, PASSWORD)
        
        # Aguarda a conexão ser estabelecida
        while not station.isconnected():
            pass
            
    print("✅ Conectado com sucesso! Endereço IP:", station.ifconfig()[0])

# Executa a função de conexão ao iniciar
conectar_wifi()
