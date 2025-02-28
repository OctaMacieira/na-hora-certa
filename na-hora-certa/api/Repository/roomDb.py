import sqlite3
from ..Models.room import Room

def initialize_database():
    # Connect to the database (it will be created if it doesn't exist)
    conn = sqlite3.connect('rooms.db')
    
    # Create a cursor object
    cursor = conn.cursor()
    
    # Create the rooms table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rooms (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            zip_code TEXT NOT NULL,
            address TEXT NOT NULL,
            size INTEGER NOT NULL,
            documents_ok BOOLEAN NOT NULL,
            condominium_fee FLOAT NOT NULL,
            iptu FLOAT NOT NULL,
            number_of_bathrooms INTEGER NOT NULL,
            has_parking_space BOOLEAN NOT NULL,
            has_reception BOOLEAN NOT NULL,
            doctors_office BOOLEAN NOT NULL
        )
    ''')
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()

def create_new_room_in_db(room):
    conn = sqlite3.connect('rooms.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO rooms (zip_code, address, size, documents_ok, condominium_fee, iptu, number_of_bathrooms, has_parking_space, has_reception, doctors_office) VALUES (?, ?)", 
                   (room.zip_code, 
                    room.address, 
                    room.size, 
                    room.documents_ok, 
                    room.condominium_fee, 
                    room.iptu, 
                    room.number_of_bathrooms, 
                    room.has_parking_space, 
                    room.has_reception, 
                    room.doctors_office))
    conn.commit()
    conn.close()
    return cursor.lastrowid

def update_room_in_db(room):
    conn = sqlite3.connect('rooms.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE rooms SET zip_code = ?, address = ?, size = ?, documents_ok = ?, condominium_fee = ?, iptu = ?, number_of_bathrooms = ?, has_parking_space = ?, has_reception = ?, doctors_office = ? WHERE id = ?", 
                    (room.zip_code, 
                    room.address, 
                    room.size, 
                    room.documents_ok, 
                    room.condominium_fee, 
                    room.iptu, 
                    room.number_of_bathrooms, 
                    room.has_parking_space, 
                    room.has_reception, 
                    room.doctors_office,
                    room.id))
    conn.commit()
    conn.close()
    return cursor.rowcount

def delete_room_in_db(room):
    conn = sqlite3.connect('rooms.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM rooms WHERE id = ?", (room.id,))
    conn.commit()
    conn.close()
    return cursor.rowcount

# Initialize the database when the module is run
if __name__ == "__main__":
    initialize_database()