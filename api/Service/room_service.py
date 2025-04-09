from api.Models.room import Room
from api.Repository.roomDb import *


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

def update_room(data):
    update_room = Room(
    id = data['id'],
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

    roomId = update_room_in_db(update_room)

    return roomId

def delete_room(data):
    delete_room = Room(id = data['id'])

    return delete_room_in_db(delete_room)