from flask import Blueprint, request, jsonify

cliente_bp = Blueprint('cliente_bp', __name__)

@cliente_bp.route('/cliente', methods=['POST'])
def verificar_cliente():
    ci = request.json.get('ci')
    
    codRes, menRes, accion = procesar_cliente(ci)
    
    salida = {
        'accion': accion,
        'codRes': codRes,
        'menRes': menRes,
        'ci': ci
    }
    
    
    return jsonify(salida)


def procesar_cliente(ci):
    ciLocal = "5593006"
    codRes = 'SIN_ERROR'
    menRes = 'OK'
    
    try:
        if ci == ciLocal:
            print("Cliente válido")
            accion = "Success"
        else:
            print("Cliente no está en el sistema")
            accion = "Cliente no está en el sistema"
            codRes = 'ERROR'
            menRes = 'Error cliente'
    except Exception as e:
        print("ERROR:", str(e))
        codRes = 'ERROR'
        menRes = 'Msg: ' + str(e)
        accion = "Error interno"
    
    return codRes, menRes, accion
