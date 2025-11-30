class Vehicle:
    def __init__(self, name, brand, color ):
        self.name = name
        self.brand = brand
        self.color = color

    def move(self):
        print("vehicle moving..")
    
class Car(Vehicle):   

    def move(self):
        print("vmmmm")

class Plane(Vehicle):

    def move(self):
        print("flying..")

class Aircraft(Plane):

    def __init__(self, name, brand, color, weapon_capacity, target_capacity):
        self.weapon_capacity = weapon_capacity
        self.target_capacity = target_capacity
        super().__init__(name, brand, color)

    def bomb(self):
        print("boooooom")

    def __str__(self):
        print(f"name:{self.name}, brand:{self.brand}, color:{self.color}, weapon:{self.weapon_capacity},target:{self.target_capacity}")
        return super().__str__()

f16 = Aircraft(
    name= "F16",
    brand= "",
    color="black",
    weapon_capacity=20000,
    target_capacity="86%"
)
class PasssangerCraft(Plane):
    def __init__(self, name, brand, color, passanger_capacity, is_comfort):
        self.passanger_capacity = passanger_capacity
        self.is_comfort = is_comfort
        super().__init__(name, brand, color)

boing = PasssangerCraft(
    name='boing 777',
    brand="BOING",
    color="white",
    passanger_capacity=True,
    is_comfort=True
)
print(Car)
print(Plane)
print(Aircraft)
print(Aircraft.__mro__)
print(PasssangerCraft)

