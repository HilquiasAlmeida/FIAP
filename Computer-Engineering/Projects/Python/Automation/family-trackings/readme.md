# 🧭 Family Trackings System

Sistema integrado de monitoramento e rastreamento familiar utilizando tecnologias IoT (Internet das Coisas) com ESP32 e aplicativos desenvolvidos em Python (Flet).

---

## 📂 Estrutura do Repositório

```text
family-trackings/
├── child-tracking-iot/              # Módulo de rastreamento (Hardware / ESP32)
│   ├── esp32_tracker.py             # Código embarcado/microPython para o ESP32
│   ├── server.py                    # Servidor backend para recepção dos dados IoT
│   ├── requirements.txt             # Dependências do servidor IoT
│   └── readme.md                    # Documentação específica do rastreador IoT
│
└── parents-child-tracking-iot/      # Módulo de acompanhamento pelos pais
    ├── app/                         # Aplicação principal (Flet Web/Wasm)
    │   ├── main.py                  # Código fonte da interface dos pais
    │   ├── requirements.txt         # Dependências do aplicativo Flet
    │   └── readme.md                # Documentação do app dos pais
    └── web/                         # Arquivos estáticos e recursos web adicionais
        └── readme.md                # Documentação da interface web
```

## 🚀 Módulos do Sistema
1. Child Tracking IoT (child-tracking-iot/)
Responsável pela coleta de dados de localização e envio de telemetria através de hardware ESP32.

    * esp32_tracker.py: Script executado no microcontrolador para monitoramento e envio de coordenadas.
    * server.py: Servidor intermediário para gerenciar e processar as requisições enviadas pelos dispositivos.
    * requirements.txt: Bibliotecas necessárias para rodar o backend do rastreador.

2. Parents Child Tracking IoT (parents-child-tracking-iot/)
Interface gráfica desenvolvida em Flet (Python) que permite aos responsáveis acompanharem em tempo real a localização dos dispositivos vinculados.

    * app/main.py: Aplicação principal com telas de login, dashboard de dispositivos conectados, cadastro de novos hardwares e rastreamento via Google Maps.
    * app/requirements.txt: Contém as dependências essenciais (flet, requests).

## 🔗 Links de Acesso (GitHub Pages)

Você pode acessar as versões web dos sistemas diretamente pelos links abaixo:

* 🌐 **Aplicação Web dos Pais (Flet Web):**
  <br>
    Acessar Parents-Child Tracking Web

* 📱 **Versão Mobile / Web App:**
  <br>
  <a href="https://hilquiasalmeida.github.io/FIAP/family-trackings/app-mobile/" target="_blank">
    Acessar Parents-Child Tracking Web
  </a>
  <br>
  (Disponível através do mesmo ambiente progressivo compilado via WebAssembly)
