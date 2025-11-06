from flask import Flask, jsonify
import logging
import time

app = Flask(__name__)

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

start_time = time.time()
request_count = 0

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
    logging.warning("Виклик ендпоїнту /error — буде помилка")
    x = 1 / 0
    return str(x)

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