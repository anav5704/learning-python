# Parent class

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def moves(self):
        print(f"{self.brand} Moves away")

    def get(self):
        print(f"This is a {self.brand} {self.model}")

myVehicle = Vehicle("Konigsegg", "Jesko")
print(myVehicle.brand, myVehicle.model)
myVehicle.get()
myVehicle.moves()


# Children classes

class Plane(Vehicle):
    def moves(self):
        print(f"{self.brand} Flies away")

class Truck(Vehicle):
    def moves(self):
        print(f"{self.brand} Drives away")

cessna = Plane("Cessna", "Skyhawk")
mack = Truck("Mack", "PInnacle")

print(cessna.moves(), mack.moves())