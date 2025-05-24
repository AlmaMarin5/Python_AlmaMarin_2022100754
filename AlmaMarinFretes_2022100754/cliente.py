# cliente/cliente.py

def verificar_cliente(ci):
    
    clientes_en_sistema = ["5593006"]

    if ci in clientes_en_sistema:
        return {
            "accion": "Success",
            "codRes": "SIN_ERROR",
            "menRes": "OK",
            "ci": 5593006
        }
    else:
        return {
            "accion": "Cliente no está en el sistema",
            "codRes": "ERROR",
            "menRes": "Error cliente",
            "ci": 5593006
        }
