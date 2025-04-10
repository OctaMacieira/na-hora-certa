from api.Models.room import Room
from api.Repository.roomDb import *
from flask import jsonify


def create_new_room(data):
    new_room = Room(
    zip_code = data['zip_code'],
    address = data['address'],
    size = data['size'],
    documents_ok = data['documents_ok'],
    condominium_fee = data['condominium_fee'],
    iptu = data['iptu'],
    number_of_bathrooms = data['number_of_bathrooms'],
    has_parking_space = data['has_parking_space'],
    has_reception = data['has_reception'],
    doctors_office = data['doctors_office']
    )

    roomId = create_new_room_in_db(new_room)

    return roomId

def delete_room(data):
    delete_room = Room(id = data['id'])

    return delete_room_in_db(delete_room)

def get_last_10_rooms():

    rooms = get_last_10_rooms_in_db()

    rooms_data = [
        {
            "id": room.id,
            "zip_code": room.zip_code,
            "address": room.address,
            "size": room.size,
            "documents_ok": room.documents_ok,
            "condominium_fee": room.condominium_fee,
            "iptu": room.iptu,
            "number_of_bathrooms": room.number_of_bathrooms,
            "has_parking_space": room.has_parking_space,
            "has_reception": room.has_reception,
            "doctors_office": room.doctors_office,
        }
        for room in rooms
    ]
    
    return jsonify(rooms_data), 200