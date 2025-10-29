from flask import Flask, request, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# ------------------------------------------------
# 🔧 Database Connection Helper
# ------------------------------------------------
def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),port=os.getenv("DB_PORT")
    )


# ------------------------------------------------
# 👋 Test Route
# ------------------------------------------------
@app.route('/hello', methods=['GET'])
def hello():
    return jsonify(message="Hello from Agriportance!")

# ------------------------------------------------
# ➕ Add Two Numbers (Simple JSON Example)
# ------------------------------------------------
@app.route('/api/sum', methods=['GET', 'POST'])
def calculate_sum():
    if request.method == 'POST':
        data = request.get_json()
        total = data['a'] + data['b']
        return jsonify({'sum': total})
    else:
        # Simple demo response for GET requests
        return jsonify({'message': 'Send a POST request with JSON {"a": <num>, "b": <num>} to get their sum.'})

# ------------------------------------------------
# 🌿 Get All Plants
# ------------------------------------------------
@app.route('/api/plants', methods=['GET'])
def get_plants():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT id, name, region, capacity FROM plants;')
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([
        {'id': r[0], 'name': r[1], 'region': r[2], 'capacity': r[3]} 
        for r in rows
    ])

# ------------------------------------------------
# 📊 Average Capacity by Region
# ------------------------------------------------
@app.route('/api/avg_capacity', methods=['GET'])
def get_avg_capacity():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT region, AVG(capacity) FROM plants GROUP BY region;')
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([
        {'region': r[0], 'avg_capacity': float(r[1])} for r in rows
    ])

# ------------------------------------------------
# 🚜 In-Memory Farms Example (for quick testing)
# ------------------------------------------------
farms = [
    {"id": 1, "name": "SolarField", "region": "East"},
    {"id": 2, "name": "WindGrove", "region": "West"},
    {"id": 3, "name": "HydroVale", "region": "North"}
]

@app.route('/api/farms', methods=['GET'])
def get_farms():
    return jsonify(farms)

@app.route('/api/farms', methods=['POST'])
def add_farm():
    new_farm = request.get_json()
    farms.append(new_farm)
    return jsonify(farms), 201

# ------------------------------------------------
# 🔬 Readings Table (Create + Fetch)
# ------------------------------------------------
@app.route('/api/readings/setup', methods=['POST'])
def create_readings_table():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS readings (
            id SERIAL PRIMARY KEY,
            plant_id INT,
            pressure FLOAT,
            recorded TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Readings table created successfully.'}), 201

@app.route('/api/readings', methods=['GET'])
def get_readings():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("""
        SELECT plant_id, MAX(recorded) AS last_recorded, AVG(pressure) AS avg_pressure
        FROM readings
        GROUP BY plant_id
        ORDER BY plant_id;
    """)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(data)

# ------------------------------------------------
# 🚀 Run Flask App
# ------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)


