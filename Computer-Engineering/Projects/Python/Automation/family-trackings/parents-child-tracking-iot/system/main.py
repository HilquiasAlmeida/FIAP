"""
Módulo Principal (Entrypoint) - Family Trackings System
Autor: Hilquias Almeida / FIAP
Descrição: Inicializa o servidor backend para recepção de telemetria IoT e gerenciamento de rotas.
"""

import uvicorn
from api.endpoints import app
from tools.diagnostic_logger import setup_logger

# Configuração do logger de diagnóstico do sistema
logger = setup_logger("SystemMain")

def main():
    """
    Função principal que gerencia a inicialização da aplicação backend.
    """
    logger.info("==================================================")
    logger.info("🚀 Inicializando o Core do Sistema: Family Trackings")
    logger.info("==================================================")
    
    try:
        # Executa o servidor ASGI Uvicorn apontando para o app FastAPI definido em api/endpoints.py
        uvicorn.run(
            "api.endpoints:app",
            host="0.0.0.0",
            port=8000,
            reload=True,
            log_level="info"
        )
    except Exception as e:
        logger.critical(f"Falha crítica ao iniciar o servidor: {e}")
        raise

if __name__ == "__main__":
    main()
