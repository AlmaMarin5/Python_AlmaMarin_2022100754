#!/usr/bin/env python
#-*- Coding: utf-8 -*-
#linea shebang: permite ejecutar este sript directamente en sistemas Unix/linux
#codificacion utf-8 para permitir caracteres especiales

from flask import Flask, jsonify, request
#Importamos flask para crear la app web, jsonify para devolver respuestas en JSON
#y request para manejar datos entrantes (por ejemplo de formularios o json)


app = Flask(__name__)
#creamos la instancia de la aplicacion flask

@app.route('/', methods=['GET'])
def hello():
    #definimos una ruta para el endpoint raiz "/" que responde a solicitudes get
   return 'hola unida'
#al acceder a la raiz del sitio, se devuelve este mensaje
@app.route('/hola', methods=['GET'])
def hola():
    #definimos una ruta para el endpoint raiz "/" que responde a solicitudes get
   return 'hola 2 unida'
#al acceder a la raiz del sitio, se devuelve este mensaje

if __name__ == "__main__":
    #este bloque se ejecuta solo si el script se ejecuta directamente (no importado como modulo)
    ## app.run (host = '127.0.0.1', debug = True, port = 5000)
    #linea comentada: ejecutaria el servidor localmente solo accesible desde la misma maquina
    
    app.run(host = '0.0.0.0', debug = True, port = 5000)
    #ejecuta la app en el host 0.0.0.0, lo cual la hace accesible desde otras maquinas en la red
    #el modo debug permite ver errores detallados y reinicia el servidor al deterctar cambios
    
    
    #esta linea esta de mas, ya que 'app.run' ya fue llamado antes
    #en la practica, solo una llamada a 'app.run()' es necesaria
    
     