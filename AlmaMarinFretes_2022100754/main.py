from flask import Flask
from cliente import cliente_bp

app = Flask(__name__)
app.register_blueprint(cliente_bp)

@app.route('/', methods=['GET'])
def home():
    return 'hola unida'

if __name__ == '__main__':
    app.run(host='localhost', port=5003, debug=True)
