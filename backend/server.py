from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_frontend(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

# Rutas y puntos finales de tu API
@app.route('/api/v1.0/mensaje', methods=['GET'])
def mensaje():
    return jsonify({'mensaje': 'Nuevo mensaje desde un servidor Flask'})

if __name__ == '__main__':
    app.run(debug=True)
