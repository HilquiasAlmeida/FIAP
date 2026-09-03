# 📍 SafeChild IoT - Sistema de Rastreamento Infantil

Sistema de rastreamento em tempo real desenvolvido para crianças. A solução integra hardware IoT (ESP32), um backend centralizador em Python (Flask + PostgreSQL) e interfaces dedicadas tanto para mobile quanto para web com as mesmas funcionalidades.

---

## 📁 Estrutura do Repositório

```text
parents-child-tracking-iot/
├── app/                  # Código e ferramentas do App Mobile (Smartphone)
│   ├── main.py
│   └── requirements.txt
├── web/                  # Código e arquivos da Versão Web (Computador)
│   └── index.html
├── server.py             # Backend em Flask + PostgreSQL (O "coração" do sistema)
├── esp32_tracker.py      # Código MicroPython para o ESP32 (Dispositivo IoT)
└── README.md             # Documentação completa do projeto
```

## 🛠️ Tecnologias Utilizadas
* Hardware (IoT): ESP32 com módulo GPS rodando MicroPython.

* Backend: Python 3.x, Flask, Psycopg2.

* Banco de Dados: PostgreSQL (tracking_db).

* Frontend (App Mobile & Web): Flet (Python puro compilado para Mobile e WebAssembly).

* Deploy / CI/CD: GitHub Pages via GitHub Actions (para a versão web).

## 🚀 Como Executar o Projeto
1. Backend e Banco de Dados
* Crie o banco de dados no PostgreSQL:
```
SQL
CREATE DATABASE tracking_db;
```

* Instale as dependências e execute o servidor Flask:
```
Bash
pip install -r requirements.txt
python server.py
```

2. Dispositivo IoT (ESP32)
* Configure suas credenciais de Wi-Fi e a URL do backend no arquivo esp32_tracker.py.

* Carregue e execute o script na placa ESP32.

3. Painel de Controle (Mobile & Web)
* Versão Web (Professores/Computador): Acessível diretamente pelo link do GitHub Pages configurado no repositório.

* Versão Mobile (Mãe/Celular): Compilada a partir do mesmo diretório app/ para uso em dispositivos móveis.

