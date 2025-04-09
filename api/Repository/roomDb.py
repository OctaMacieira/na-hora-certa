from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from api.Models.room import Room

# Define the SQLAlchemy base and engine
Base = declarative_base()
engine = create_engine('sqlite:///na-hora-certa.db')
Session = sessionmaker(bind=engine)

# Define the Room model using SQLAlchemy
class Room(Base):
    __tablename__ = 'rooms'
    id = Column(Integer, primary_key=True, autoincrement=True)
    zip_code = Column(String, nullable=False)
    address = Column(String, nullable=False)
    size = Column(Integer, nullable=False)
    documents_ok = Column(Boolean, nullable=False)
    condominium_fee = Column(Float, nullable=False)
    iptu = Column(Float, nullable=False)
    number_of_bathrooms = Column(Integer, nullable=False)
    has_parking_space = Column(Boolean, nullable=False)
    has_reception = Column(Boolean, nullable=False)
    doctors_office = Column(Boolean, nullable=False)

def initialize_database():
    # Create the tables in the database
    Base.metadata.create_all(engine)

def create_new_room_in_db(room):
    session = Session()
    session.add(room)
    session.commit()
    room_id = room.id
    session.close()
    return room_id

def update_room_in_db(room):
    session = Session()
    existing_room = session.query(Room).filter_by(id=room.id).first()
    if existing_room:
        existing_room.zip_code = room.zip_code
        existing_room.address = room.address
        existing_room.size = room.size
        existing_room.documents_ok = room.documents_ok
        existing_room.condominium_fee = room.condominium_fee
        existing_room.iptu = room.iptu
        existing_room.number_of_bathrooms = room.number_of_bathrooms
        existing_room.has_parking_space = room.has_parking_space
        existing_room.has_reception = room.has_reception
        existing_room.doctors_office = room.doctors_office
        session.commit()
        rowcount = 1
    else:
        rowcount = 0
    session.close()
    return rowcount

def delete_room_in_db(room):
    session = Session()
    rowcount = session.query(Room).filter_by(id=room.id).delete()
    session.commit()
    session.close()
    return rowcount

# Initialize the database when the module is run
if __name__ == "__main__":
    initialize_database()