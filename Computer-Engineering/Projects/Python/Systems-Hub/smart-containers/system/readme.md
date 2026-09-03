# ⚙️ System / Backend - Smart Containers
Este diretório contém o núcleo de processamento e o backend do projeto Smart Containers, desenvolvido em Python utilizando o framework Django e o Django REST Framework (DRF).

O sistema atua como o cérebro da operação, sendo responsável por receber, processar e armazenar os dados de telemetria enviados pelo hardware embarcado no container, além de gerenciar o painel administrativo.

## 🏗️ Estrutura de Arquivos do Sistema
   ```Plaintext
   system/
   ├── manage.py            # Utilitário de linha de comando do Django
   ├── db.sqlite3           # Banco de dados local padrão
   ├── core/                # Configurações principais do projeto
   │   ├── __init__.py
   │   ├── settings.py      # Configurações globais e apps instalados
   │   ├── urls.py          # Rotas principais da aplicação
   │   └── wsgi.py          # Configuração de deploy WSGI
   └── api/                 # Aplicativo de Telemetria e Gestão de Containers
       ├── models.py        # Modelos do Banco de Dados
       ├── serializers.py   # Conversão de dados para formato JSON (API)
       ├── views.py         # Lógica de recebimento dos dados da API
       └── urls.py          # Rotas específicas dos endpoints de telemetria
   ```
## 🗄️ Modelos de Dados (models.py)
O sistema gerencia duas entidades principais no banco de dados:

1. Container: Armazena as informações cadastrais de cada container rastreado.
   * codigo: Identificador único do container.
   * descricao: Informações adicionais sobre a carga.
   * criado_em: Data e hora de cadastro.

2. Telemetria: Registra os dados enviados em tempo real pelo dispositivo IoT (ESP32).
   * container: Chave estrangeira ligada ao container correspondente.
   * status_porta: Estado atual da porta (ABERTA ou FECHADA).
   * latitude / longitude: Coordenadas de rastreamento GPS.
   * temperatura: Temperatura interna registrada na carga.
   * data_hora: Momento exato em que a telemetria foi gerada.

## 🔌 Endpoints da API REST
A API foi construída para receber requisições HTTP POST vindas do equipamento embarcado no container:
   * Endpoint de Telemetria: ```POST /api/telemetria/```
      * Função: Recebe os dados de abertura de porta e GPS enviados pelo ESP32 e os salva no banco de dados central.


## 🚀 Como Configurar e Executar
1. Instale as dependências necessárias:
   ```Bash
   pip install django djangorestframework
   ```

2. Aplique as migrações para criar o banco de dados:
   ```Bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. Inicie o servidor de desenvolvimento:
   ```Bash
   python manage.py runserver
   ```
4. Acesse o Painel Administrativo:
   Abra o navegador em http://127.0.0.1:8000/admin/ OU http://localhost:8000/admin/
   para gerenciar os containers e visualizar os registros de telemetria em tempo real através da interface nativa do Django.

## 🛠️ Tecnologias Utilizadas
   * Linguagem: Python 🐍
   * Framework Principal: Django 🌐
   * API: Django REST Framework (DRF)
   * Banco de Dados: PosgreSQL
