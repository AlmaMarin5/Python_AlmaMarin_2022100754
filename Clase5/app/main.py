
from flask import Flask
from login  import login


app = Flask(__name__)
#registrar el blueprint de login
app.register_blueprint(login)

@app.route('/', methods=['GET'])
def hello():
   return 'hola unida'

if __name__ == "__main__":
    
    app.run(host = '0.0.0.0', port=5001, debug=True)
  
    
     