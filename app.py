# File: app.py
from flask import Flask, request, jsonify

app = Flask(__name__)
data = {}

@app.route('/send', methods=['POST'])
def send():
    global data
    data = request.json
    return jsonify(success=True)

@app.route('/receive', methods=['GET'])
def receive():
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
