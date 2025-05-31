# cliente.py

from flask import Blueprint, request, jsonify

cliente_bp = Blueprint('cliente_bp', __name__)

# Lista de clientes válidos
clientes_validos = ["5593006"]

@cliente_bp.route('/cliente', methods=['POST'])
def verificar_cliente():
    data = request.get_json()

    if not data or 'ci' not in data:
        return jsonify({
            "accion": "Solicitud incorrecta",
            "codRes": "ERROR",
            "menRes": "Falta el campo 'ci'",
            "ci": None
        }), 400

    ci = data['ci']

    if ci in clientes_validos:
        return jsonify({
            "accion": "Success",
            "codRes": "SIN_ERROR",
            "menRes": "OK",
            "ci": ci
        }), 200
    else:
        return jsonify({
            "accion": "Cliente no está en el sistema",
            "codRes": "ERROR",
            "menRes": "Error cliente",
            "ci": ci
        }), 404
