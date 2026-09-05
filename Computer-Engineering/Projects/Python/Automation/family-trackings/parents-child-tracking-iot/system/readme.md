# Family Trackings - System Core & Automation

Este módulo contém a infraestrutura de backend, APIs, pipelines de dados e plugins de integração IoT do projeto **Family Trackings**.

## 🚀 Executando o Sistema Localmente (Via Docker)
Para testar a ação completa do sistema em sua máquina, certifique-se de ter o Docker instalado e execute:

\`\`\`bash
git clone https://github.com/<seu-usuario>/<seu-repositorio>.git
cd <seu-repositorio>/Computer-Engineering/Projects/Python/Automation/family-trackings/parents-child-tracking-iot/system
docker-compose up --build
\`\`\`

## 📦 Componentes Disponíveis para Download
* **API (`/api`)**: Endpoints para sincronização de localização e status dos dispositivos.
* **Pipelines (`/pipelines`)**: Rotinas de processamento assíncrono de telemetria.
* **Plugins (`/plugins`)**: Módulos desacoplados para tratamento de pacotes de hardware.
* **Tools (`/tools`)**: Simuladores de rastreadores físicos para testes de estresse e validação.
