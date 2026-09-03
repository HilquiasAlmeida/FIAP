# main.py - Smart Containers (Equipamento Embarcado)
import machine
import time
import network

# Configuração do Wi-Fi para conectar o ESP32 à internet
SSID = "SEU_WIFI"
PASSWORD = "SUA_SENHA"

def conectar_wifi():
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(SSID, PASSWORD)
    while not station.isconnected():
        print("Conectando ao Wi-Fi...")
        time.sleep(1)
    print("Conectado! IP:", station.ifconfig()[0])

conectar_wifi()

# Configuração do Sensor Magnético (Reed Switch) na GPIO 4
# GPIO 4 configurada com resistor interno de pull-up
reed_switch = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)

# LED integrado do ESP32 (GPIO 2) para simular alerta visual
led = machine.Pin(2, machine.Pin.OUT)

print("Sistema de monitoramento de porta iniciado...")

while True:
    # Lê o estado da porta do container
    # Dependendo de como o sensor está ligado, 1 ou 0 indica aberto
    estado_porta = reed_switch.value()
    
    if estado_porta == 1:
        print("⚠️ ALERTA: A porta do container foi ABERTA!")
        led.value(1) # Acende o LED
        # Aqui você faria uma requisição HTTP POST para a sua API Django enviando o alerta
    else:
        print("🔒 Container seguro. Porta fechada.")
        led.value(0) # Apaga o LED
        
    time.sleep(3)  # Aguarda 3 segundos para a próxima leitura
