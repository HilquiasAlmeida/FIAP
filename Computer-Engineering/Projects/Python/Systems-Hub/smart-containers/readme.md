# Smart Containers: Sistema Inteligente de Rastreamento e Monitoramento de Cargas 📦🛰️
Bem-vindo ao repositório oficial do Smart Containers. Este projeto consiste em uma solução completa de IoT (Internet das Coisas) e desenvolvimento de software voltada para o rastreamento em tempo real de cargas transportadas em containers e o monitoramento remoto de abertura de portas.

Desenvolvido majoritariamente em Python utilizando o framework Django, o ecossistema integra hardware embarcado, backend robusto, painel web completo e aplicativo móvel.

## 🏗️ Arquitetura do Sistema
O ecossistema do projeto está dividido em quatro módulos principais localizados na estrutura de pastas:
```
Plaintext
Smart-Containers/
├── equipamento-embarcado/   # Dispositivo IoT (ESP32/GPS/Sensores de porta)
├── sistema/                 # Backend central e APIs (Django / DRF)
├── website/                 # Painel Web / Dashboard (Desenvolvido em Django + HTML/CSS/JS)
└── app-mobile/              # Aplicativo para motoristas e equipes de campo
```

## 🔧 Detalhes dos Módulos
1. 🔌 Equipamento Embarcado (/equipamento-embarcado)
* Função: Instalado diretamente no container ou veículo de transporte.
* Tecnologias: MicroPython / C++, ESP32, Módulo GPS (NEO-6M), Sensor Magnético de Abertura de Porta (Reed Switch) e Sensor de Temperatura.
* Comunicação: Envio de telemetria via protocolo MQTT ou HTTP para o servidor central em tempo real.


2. ⚙️ Sistema / Backend (/sistema)
* Função: O cérebro da operação. Gerencia o banco de dados, o painel administrativo nativo, o processamento dos dados dos containers, as regras de segurança e os endpoints de comunicação com o hardware e os apps.
* Tecnologias: Python, Django e Django REST Framework (DRF).


3. 💻 Website / Dashboard (/website)
* Função: Painel de controle web para gestores logísticos visualizarem a frota em mapas interativos, acompanharem rotas e checar alertas de violação/abertura da porta do container em tempo real.
* Tecnologias: Django (Django Templates / Views), HTML5, CSS3, JavaScript e Leaflet.js (Mapas).


4. 📱 App Mobile (/app-mobile)
* Função: Ferramenta voltada para o motorista ou equipe de operação acompanharem o status do transporte e receberem notificações de emergência.
* Tecnologias: Python / Frameworks Mobile integrados diretamente com a API Django.

## 🚀 Como Visualizar no GitHub Pages
Este repositório está configurado para exibir a documentação e os arquivos estáticos do projeto através do GitHub Pages.
Para acessar a página, navegue até a aba Settings do seu repositório no GitHub, clique em Pages e certifique-se de que a branch principal está selecionada como fonte (Build and deployment).

## 🛠️ Tecnologias Utilizadas
* Linguagem Principal: Python 🐍
* Framework Web & Sistema: Django / Django REST Framework 🌐
* IoT / Hardware: MicroPython / C++
* Frontend Web: HTML5, CSS3, JavaScript, Leaflet.js
* Controle de Versão: Git & GitHub

## 📄 Licença
Este projeto é desenvolvido para fins educacionais e profissionais sob a licença MIT. Sinta-se à vontade para utilizar e contribuir!
