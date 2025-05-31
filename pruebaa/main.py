# main.py

from flask import Flask
from cliente import cliente_bp

app = Flask(__name__)

# Registrar el blueprint
app.register_blueprint(cliente_bp)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5010, debug=True)  # Puerto 5010
