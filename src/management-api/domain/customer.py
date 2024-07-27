class Customer:
    def __init__(self):
        self.id: int
        self.name: str
        self.birthday: str
        self.gender: str
        self.email: str
        self.phone: str
        self.adress: str
        self.vehicles: Vehicle


class Vehicle:
    def __init__(self):
        self.brand: str
        self.model: str
        self.year: int
        self.licensePlate: str