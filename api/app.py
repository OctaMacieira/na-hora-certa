from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_restful import Api
from flasgger import Swagger
from Service.room_service import *



app = Flask(__name__)
CORS(app)
api = Api(app)

app.config['SWAGGER'] = {
    'title': 'Na Hora Certa API',
    'uiversion': 3,
    'specs_route': '/swagger'
}
swagger = Swagger(app)



@app.route("/create-new-room", methods=["POST"])
def cadastrar_nova_sala():
    """
    Cria uma nova sala no banco de dados
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: Room
          required:
            - id
            - zip_code
            - address
            - size
            - documents_ok
            - condominium_fee
            - iptu
            - number_of_bathrooms
            - has_parking_space
            - has_reception
            - doctors_office
          properties:
            id:
              type: integer
              description: ID da Sala criado automaticamente pelo banco de dados
              example: 1
            zip_code:
              type: string
              description: CEP da Sala
              example: "12345-678"
            address:
              type: string
              description: Endereço da Sala
              example: "Rua Exemplo, 123"
            size:
              type: integer
              description: Tamanho da Sala em m²
              example: 50
            documents_ok:
              type: boolean
              description: Documentação em ordem
              example: true
            condominium_fee:
              type: number
              description: Taxa de condomínio
              example: 200.50
            iptu:
              type: number
              description: Valor do IPTU
              example: 1500.00
            number_of_bathrooms:
              type: integer
              description: Número de banheiros
              example: 2
            has_parking_space:
              type: boolean
              description: Possui vaga de estacionamento
              example: true
            has_reception:
              type: boolean
              description: Possui recepção
              example: true
            doctors_office:
              type: boolean
              description: É elegível para consultório médico
              example: true
    responses:
      200:
        description: Sala criada com sucesso
    """
    if request.is_json:
      data = request.get_json()
    else:
      print("Request is not JSON")

    result = create_new_room(data)

    if isinstance(result, int):
        return jsonify({"message": "Room created successfully", "room_id": result}), 200
    else:
        return jsonify({"error": "Failed to create room"}), 500


@app.route("/delete-room", methods=["DELETE"])
def deletar_sala():
    """
      Deleta uma sala existente no banco de dados
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: Room
          required:
            - id
    properties:
            id:
              type: integer
              description: ID da Sala criado automaticamente pelo banco de dados
              example: 1
    responses:
      200:
        description: Sala deletada com sucesso
    """
    if request.is_json:
      data = request.get_json()
    else:
      print("Request is not JSON")
    
    result = delete_room(data)

    if isinstance(result, int):
        return jsonify({"message": "Room deleted successfully", "room_id": result}), 200
    else:
        return jsonify({"error": "Failed to delete room"}), 500

@app.route("/get-last-10-rooms", methods=["GET"])
def get_last_10_rooms_route():
    """
    Retorna os últimos 10 registros da tabela de salas
    ---
    responses:
      200:
        description: Lista dos últimos 10 registros
    """
    return get_last_10_rooms()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
