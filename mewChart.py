# mewChart.py (Backend)

from flask import Flask, render_template, jsonify
import psycopg2
import os

app = Flask(__name__)

# Database connection parameters
db_params = {
    'dbname': os.environ.get('DB_NAME', 'mmmaaa'),
    'user': os.environ.get('DB_USER', 'mmmaaa'),
    'password': os.environ.get('DB_PASSWORD', 'Maal97900'),
    'host': os.environ.get('DB_HOST', 'localhost'),
    'port': os.environ.get('DB_PORT', 5432),
}

def get_data_from_db():
    conn = psycopg2.connect(**db_params)
    cur = conn.cursor()
    cur.execute("SELECT * FROM ryb")
    data = cur.fetchall()
    conn.close()
    return data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    data = get_data_from_db()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

