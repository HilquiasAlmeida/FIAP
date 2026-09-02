from flask import Flask, request, jsonify, render_template_string
from datetime import datetime
import psycopg2
import os

app = Flask(__name__)

# Configurações do PostgreSQL (Substitua pelos seus dados se necessário)
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "tracking_db")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "sua_senha")
DB_PORT = os.getenv("DB_PORT", "5432")

def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        port=DB_PORT
    )
    return conn

def init_db():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS locations (
                id SERIAL PRIMARY KEY,
                device_id VARCHAR(100),
                latitude DOUBLE PRECISION,
                longitude DOUBLE PRECISION,
                timestamp VARCHAR(50),
                status VARCHAR(50)
            )
        ''')
        conn.commit()
        cursor.close()
        conn.close()
        print("Banco de dados PostgreSQL conectado e tabela verificada com sucesso!")
    except Exception as e:
        print(f"Erro ao conectar ou inicializar o banco PostgreSQL: {e}")

init_db()

@app.route('/update', methods=['POST'])
def update_location():
    data = request.json
    if not data or 'latitude' not in data or 'longitude' not in data:
        return jsonify({"error": "Dados incompletos"}), 400
        
    device_id = data.get('device_id', 'crianca_01')
    latitude = data['latitude']
    longitude = data['longitude']
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status = "Ativo"
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO locations (device_id, latitude, longitude, timestamp, status)
            VALUES (%s, %s, %s, %s, %s)
        ''', (device_id, latitude, longitude, timestamp, status))
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    print(f"[{timestamp}] Posição salva para {device_id}: {latitude}, {longitude}")
    return jsonify({"status": "sucesso", "mensagem": "Localização salva no PostgreSQL"}), 200

@app.route('/location', methods=['GET'])
def get_location():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT device_id, latitude, longitude, timestamp, status FROM locations ORDER BY id DESC LIMIT 1')
        row = cursor.fetchone()
        cursor.close()
        conn.close()
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    if not row:
        return jsonify({"error": "Nenhuma localização encontrada"}), 404
        
    return jsonify({
        "device_id": row[0],
        "latitude": row[1],
        "longitude": row[2],
        "timestamp": row[3],
        "status": row[4]
    })

@app.route('/')
def index():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT device_id, latitude, longitude, timestamp, status FROM locations ORDER BY id DESC LIMIT 1')
        row = cursor.fetchone()
        cursor.close()
        conn.close()
    except Exception:
        row = None
    
    device = {
        "device_id": row[0], "latitude": row[1], "longitude": row[2], "timestamp": row[3], "status": row[4]
    } if row else {
        "device_id": "N/A", "latitude": 0.0, "longitude": 0.0, "timestamp": "-", "status": "Aguardando sinal"
    }

    html_template = """
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>Rastreamento Infantil IoT (PostgreSQL)</title>
        <meta http-equiv="refresh" content="5">
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f0f2f5; text-align: center; margin: 0; padding: 50px; }
            .card { background: white; padding: 30px; border-radius: 12px; display: inline-block; box-shadow: 0 4px 15px rgba(0,0,0,0.1); max-width: 400px; width: 100%; }
            h2 { color: #2c3e50; margin-bottom: 20px; }
            p { font-size: 16px; color: #555; text-align: left; margin: 10px 0; }
            .badge { color: white; background-color: #27ae60; padding: 3px 8px; border-radius: 4px; font-weight: bold; }
            .btn { display: inline-block; margin-top: 20px; padding: 12px 20px; font-size: 16px; background-color: #3498db; color: white; text-decoration: none; border-radius: 6px; transition: background 0.3s; }
            .btn:hover { background-color: #2980b9; }
        </style>
    </head>
    <body>
        <div class="card">
            <h2>Rastreador Infantil IoT</h2>
            <p><strong>Dispositivo:</strong> {{ device.device_id }}</p>
            <p><strong>Latitude:</strong> {{ device.latitude }}</p>
            <p><strong>Longitude:</strong> {{ device.longitude }}</p>
            <p><strong>Última Atualização:</strong> {{ device.timestamp }}</p>
            <p><strong>Status:</strong> <span class="badge">{{ device.status }}</span></p>
            <a class="btn" href="https://www.google.com/maps?q={{ device.latitude }},{{ device.longitude }}" target="_blank">Abrir no Google Maps</a>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_template, device=device)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
