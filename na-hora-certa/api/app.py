from flask import Flask, request
from flask_restful import Api
from flasgger import Swagger
from json import json
from Service.room_service import *



app = Flask(__name__)
api = Api(app)

app.config['SWAGGER'] = {
    'title': 'Na Hora Certa API',
    'uiversion': 3,
    'specs_route': '/swagger'
}
swagger = Swagger(app)



@app.route("/create-new-room", methods=["POST"])
def create_new_room():
    """
    Retorna o status da Pool
    ---
    responses:
      200:
        description: Status da pool de mineracao
    """
    if request.is_json:
      data = request.get_json()
    else:
      print("Request is not JSON")

    room_register = create_new_room(data)
    return True


@app.route("/update-room", methods=["UPDATE"])
def update_room():
    """
     Retorna o Saldo da Conta
    ---
    responses:
      200:
        description: Saldo da Conta
    """
    if request.is_json:
      data = request.get_json()
    else:
      print("Request is not JSON")

    room_update = update_room(data)
    return True


@app.route("/delete-room", methods=["DELETE"])
def delete_room():
    """
      Retorna a taxa de hash total da conta
    ---
    responses:
      200:
        description: Taxa de hash total da conta
    """
    if request.is_json:
      data = request.get_json()
    else:
      print("Request is not JSON")
    
    room_delete = delete_room(data)
    return True


if __name__ == "__main__":
    # Escolha um endereço e porta apropriados
    app.run(host="0.0.0.0", port=5000, debug=True)
