# 📍 Sistema de Rastreamento Infantil IoT (Sem Smartphone)

Este projeto consiste em um sistema de rastreamento em tempo real para crianças que não utilizam smartphone. O sistema é composto por um dispositivo IoT dedicado (como uma placa ESP32 equipada com módulo GPS) que envia coordenadas geográficas via requisições HTTP POST para um servidor backend em **Python (Flask)**, o qual armazena os dados em um banco de dados **PostgreSQL** e disponibiliza um painel web com link direto para o Google Maps.

---

## 🛠️ Tecnologias Utilizadas

- **Backend:** Python 3.x, Flask, Psycopg2
- **Banco de Dados:** PostgreSQL
- **Hardware (Dispositivo IoT):** ESP32 com MicroPython (ou C++/Arduino)
- **Frontend / Painel:** HTML5 / CSS3 (Embutido no Flask com atualização automática)

---

## 📁 Estrutura do Repositório

```text
child tracking/
├── server.py             # Servidor backend Flask + Conexão PostgreSQL
├── requirements.txt      # Dependências do Python
├── esp32_tracker.py      # Código para o microcontrolador ESP32 (MicroPython)
└── README.md             # Documentação do projeto
```

## ⚙️ Pré-requisitos
Antes de iniciar, certifique-se de ter instalado em sua máquina:

* Python (versão 3.8 ou superior)

* PostgreSQL instalado e em execução (localmente ou via nuvem)

* Uma IDE para o ESP32 (como Thonny ou PyCharm com suporte a MicroPython)

##  🗄️ Configuração do Banco de Dados (PostgreSQL)
 1. Abra o seu cliente PostgreSQL (pgAdmin, DBeaver ou terminal psql) e crie um banco de dados para o projeto:
```
SQL
CREATE DATABASE tracking_db;
```
2. O script do servidor (server.py) criará automaticamente a tabela necessária (locations) ao ser iniciado.

## 🚀 Como Executar o Servidor Backend
1. Clone este repositório ou baixe os arquivos para o seu computador:
```
Bash
git clone https://github.com/HilquiasAlmeida/child tracking.git
cd child tracking
```

2. Instale as dependências do Python listadas no arquivo requirements.txt:
```
Bash
pip install -r requirements.txt
```

3. Configure as credenciais do seu banco de dados PostgreSQL. Por padrão, o arquivo #server.py# utiliza:

* DB_HOST: localhost

* DB_NAME: tracking_db

* DB_USER: postgres

* DB_PASS: sua_senha (substitua pela sua senha real ou defina via variáveis de ambiente)

4. Execute o servidor Flask:
```
Bash
python server.py
```
5. Acesse o painel web no seu navegador:
## 👉 http://localhost:5000

## 🔌 Como Configurar o Hardware (ESP32)
1. Certifique-se de que a sua placa ESP32 possui o MicroPython instalado.
2. Abra o arquivo esp32_tracker.py em uma IDE compatível (como o Thonny).
3. Altere as credenciais da sua rede Wi-Fi e o endereço IP do servidor onde o Flask está rodando:

```
Python
WIFI_SSID = "NOME_DA_SUA_REDE_WIFI"
WIFI_PASS = "SENHA_DA_SUA_REDE_WIFI"
SERVER_URL = "http://IP_DO_SEU_SERVIDOR:5000/update"
```

4. Conecte o código ao seu ESP32 e execute-o. O dispositivo começará a enviar as coordenadas periodicamente para o banco PostgreSQL.

## 📄 Licença
Este projeto está sob a licença MIT. Sinta-se à vontade para utilizar, modificar e contribuir!
