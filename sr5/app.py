from flask import Flask
import logging

app = Flask(__name__)

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

@app.route('/')
def home():
    logging.info("Отримано запит до '/'")
    return "Сервіс працює"

if __name__ == '__main__':
    app.run(debug=True)