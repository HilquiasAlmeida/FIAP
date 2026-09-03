## 🔌 Equipamento Embarcado - Smart Containers
Este módulo é responsável pela IoT (Internet das Coisas) do projeto Smart Containers. Ele roda diretamente no hardware instalado no container ou veículo de transporte para monitorar o estado da porta (aberta/fechada) e enviar os dados em tempo real.

## 🛠️ Componentes Utilizados
* Microcontrolador: ESP32 (com suporte a Wi-Fi)
* Linguagem: MicroPython
* Sensores:

   * Sensor Magnético de Abertura (Reed Switch)

    * Módulo GPS NEO-6M (para rastreamento de localização)
* Atuadores: LED indicador de status / Alerta visual

## 📂 Estrutura dos Arquivos
```Plaintext
equipamento-embarcado/
├── boot.py      # Script de inicialização (Conexão Wi-Fi automática)
└── main.py      # Lógica principal de monitoramento dos sensores
```


## ⚙️ Como Executar no ESP32
1. Certifique-se de que o seu ESP32 está com o MicroPython instalado.
2. Abra o software de sua preferência (como o Thonny IDE ou VS Code com extensões para MicroPython).
3. Edite as variáveis SSID e PASSWORD nos arquivos boot.py com os dados da sua rede Wi-Fi.
4. Faça o upload de ambos os arquivos (boot.py e main.py) para a memória interna do ESP32.
5. Reinicie a placa para ver a conexão Wi-Fi estabelecida e o monitoramento da porta funcionando no console serial.
