# main.py - Smart Containers (Equipamento Embarcado)
import machine
import time

# Configuração do Sensor Magnético (Reed Switch) na GPIO 4
reed_switch = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)

# LED integrado do ESP32 (GPIO 2) para simular alerta visual
led = machine.Pin(2, machine.Pin.OUT)

print("🚀 Sistema de monitoramento de porta iniciado...")

while True:
    # Lê o estado da porta do container
    estado_porta = reed_switch.value()
    
    if estado_porta == 1:
        print("⚠️ ALERTA: A porta do container foi ABERTA!")
        led.value(1) # Acende o LED
    else:
        print("🔒 Container seguro. Porta fechada.")
        led.value(0) # Apaga o LED
        
    time.sleep(3)  # Aguarda 3 segundos para a próxima leitura
