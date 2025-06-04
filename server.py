from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route('/ping')
def ping():
    server_time = int(time.time() * 1000)  # время в миллисекундах
    return jsonify({'serverTime': server_time})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
