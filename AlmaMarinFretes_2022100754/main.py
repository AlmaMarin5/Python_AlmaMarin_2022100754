from flask import Flask, request, jsonify
import cliente  

app = Flask(__name__)

@app.route('/cliente', methods=['POST'])
def consultar_cliente():
    data = request.get_json()

    if not data or 'ci' not in data:
        return jsonify({
            "accion": "Entrada inválida",
            "codRes": "ERROR",
            "menRes": "CI no proporcionado",
            "ci": None
        }), 400

    ci = data['ci']
    resultado = cliente.verificar_cliente(ci)  
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(port=5003)
