class Animals:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("general animals sound")
    
class Cat(Animals):
    def speak(self):
        print("MIAUU")

class Dog(Animals):
    def speak(self):
        print("WOOF")

print(Cat)
print(Dog)
