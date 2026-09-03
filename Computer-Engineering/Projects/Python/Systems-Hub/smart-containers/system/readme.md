# ⚙️ Sistema / Backend - Smart Containers

Este módulo é o cérebro do projeto **Smart Containers**, desenvolvido em **Python** utilizando o framework **Django** e o **Django REST Framework (DRF)**.

## 🚀 Funcionalidades
- Gerenciamento de containers cadastrados no sistema.
- API REST para recebimento de dados de telemetria enviados pelo ESP32 (estado da porta, GPS e temperatura).
- Painel Administrativo nativo do Django para controle de dados e usuários.

## 🛠️ Como Executar o Backend
1. Instale as dependências:
   ```bash
   pip install django djangorestframework
   ```

* Aplique as migrações do banco de dados:

  ```Bash
  python manage.py makemigrations
  python manage.py migrate
  ```

* Inicie o servidor local:

  ```Bash
  python manage.py runserver
  ```
  
