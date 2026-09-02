import time
import unetwork
import urequests
from machine import UART, Pin

WIFI_SSID = "SEU_SSID_WIFI"
WIFI_PASS = "SUA_SENHA_WIFI"
SERVER_URL = "http://IP_DO_SEU_SERVIDOR:5000/update"
DEVICE_ID = "crianca_01"

def conecta_wifi():
    wlan = unetwork.WLAN(unetwork.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Conectando ao Wi-Fi...")
        wlan.connect(WIFI_SSID, WIFI_PASS)
        while not wlan.isconnected():
            time.sleep(1)
    print("Conectado! IP:", wlan.ifconfig()[0])

conecta_wifi()

while True:
    try:
        # Exemplo simulando coordenadas (substitua pela leitura real do módulo GPS se conectado)
        latitude = -23.561684
        longitude = -46.655981
        
        payload = {
            "device_id": DEVICE_ID,
            "latitude": latitude,
            "longitude": longitude
        }
        
        print("Enviando dados:", payload)
        response = urequests.post(SERVER_URL, json=payload)
        print("Resposta do servidor:", response.text)
        response.close()
        
    except Exception as e:
        print("Erro ao enviar dados:", e)
        
    time.sleep(15)

