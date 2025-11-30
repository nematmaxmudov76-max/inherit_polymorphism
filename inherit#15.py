class Animal:
    pass

class Mammal(Animal):
    pass

class Dog(Mammal):
    pass

dog = Dog()

print(isinstance(dog, Dog))
print(isinstance(dog, Mammal))
print(isinstance(dog, Animal))