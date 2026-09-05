"""
Project: family-trackings
Module: Web Backend & Dashboard Server (web/main.py)
Description: Lightweight web server to host the project interface 
             and provide simulated API endpoints for the web simulator.
"""

import os
import random
from flask import Flask, jsonify, send_from_directory

# Configura o diretório base da web
WEB_DIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__, static_folder=WEB_DIR, static_url_path='')

@app.route('/')
def serve_index():
    """Serve a página inicial do projeto (index.html)."""
    return send_from_directory(WEB_DIR, 'index.html')

@app.route('/api/simulation-status', methods=['GET'])
def simulation_status():
    """API endpoint para alimentar o painel simulador web com dados em tempo real."""
    return jsonify({
        "system": "family-trackings Web Interface",
        "status": "Active",
        "satellite_link": "Connected (LEO Off-Grid)",
        "simulated_device": {
            "device_id": "DEVICE_CHILD_01",
            "battery": round(random.uniform(40.0, 98.5), 2),
            "lat": -23.550520 + random.uniform(-0.0005, 0.0005),
            "lng": -46.633308 + random.uniform(-0.0005, 0.0005),
            "panic_triggered": False
        }
    })

if __name__ == '__main__':
    print("==================================================")
    print("🌐 Servidor Web & Simulador - family-trackings")
    print("Acesse no navegador: http://127.0.0.1:5000")
    print("==================================================")
    app.run(host='0.0.0.0', port=5000, debug=True)
