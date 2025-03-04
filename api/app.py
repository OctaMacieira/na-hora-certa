from flask import Flask, request, jsonify
from flask_restful import Api
from flasgger import Swagger
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
    Create a new room in the Database
    ---
    responses:
      200:
        description: Room created successfully
    """
    if request.is_json:
      data = request.get_json()
    else:
      print("Request is not JSON")

    room_register = create_new_room(data)
    return room_register


@app.route("/update-room", methods=["PUT"])
def update_room():
    """
     Update an existing room in the Database
    ---
    responses:
      200:
        description: Room successfully updated
    """
    if request.is_json:
      data = request.get_json()
    else:
      print("Request is not JSON")

    room_update = update_room(data)
    return room_update


@app.route("/delete-room", methods=["DELETE"])
def delete_room():
    """
      Delete an existing room in the Database
    ---
    responses:
      200:
        description: Room successfully deleted
    """
    if request.is_json:
      data = request.get_json()
    else:
      print("Request is not JSON")
    
    room_delete = delete_room(data)
    return room_delete


if __name__ == "__main__":
    # Escolha um endereço e porta apropriados
    app.run(host="0.0.0.0", port=5000, debug=True)
