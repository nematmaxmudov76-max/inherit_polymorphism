class Appliance:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    def items():
        return(f"I have a lot of home items")
    

class WashingMachine(Appliance):
    def __init__(self, brand, price, capacity):
        self.capacity = capacity
        super().__init__(brand, price)
    def __str__(self):
        print(f"brend:{self.brand}, narxi:{self.price}, joy hajmi:{self.capacity}")
        return super().__str__()
    
washing = WashingMachine(
    brand= "artel",
    price= "299$",
    capacity= "1 metr kub"
)

print(washing)
print(Appliance.items())