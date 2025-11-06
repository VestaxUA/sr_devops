from flask import Flask, jsonify
import logging
import socket
import time

app = Flask(__name__)

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

start_time = time.time()
request_count = 0

STATSD_HOST = "127.0.0.1"
STATSD_PORT = 9999

def send_to_statsd(message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(message.encode(), (STATSD_HOST, STATSD_PORT))
    sock.close()

@app.before_request
def before_request():
    global request_count
    request_count += 1

@app.route('/')
def home():
    logging.info("Отримано запит до '/'")
    return "Сервіс працює"

@app.route('/error')
def error():
    try:
        logging.warning("Виклик ендпоїнту /error — буде помилка")
        x = 1 / 0
        return str(x)
    except Exception as e:
        logging.exception("Сталася помилка у /error")
        send_to_statsd(f"Помилка: {type(e).__name__} - {e}")
        return "Виникла помилка. Деталі записані у лог.", 500

@app.route('/status')
def status():
    uptime = round(time.time() - start_time, 2)
    info = {
        "uptime_seconds": uptime,
        "request_count": request_count
    }
    logging.info("Надано статус застосунку")
    return jsonify(info)

if __name__ == '__main__':
    app.run(debug=True)