from dataclasses import dataclass

@dataclass
class Room:
    id: str
    zip_code: str
    address: str
    size: int
    documents_ok: bool
    condominium_fee: float
    iptu: float
    number_of_bathrooms: int
    has_parking_space: bool
    has_reception: bool
    doctors_office: bool
    