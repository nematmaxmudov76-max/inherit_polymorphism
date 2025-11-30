class Person:
    def __init__(self,name,age, kasb):
        self.name = name
        self.age = age
        self.kasb = kasb

    def hobbiy(self):
        print("har kuni kitob o'qidi")
        
class dectination(Person):
    def __init__(self, name, age, kasb, manzil):
        self.manzil = manzil
        super().__init__(name, age, kasb)

class Employee(dectination):
   def __init__(self, name, age, kasb, manzil, salary):
    self.salary = salary
    super().__init__(name, age, kasb, manzil) 

    def __str__(self):
        print(f"name:{self.name}, age;{self.age},kasb:{self.kasb}, maoshi:{self.salary}, manzili:{self.manzil}")
        return super().__str__()
    
ishchi = Employee(
    name= "eshmat",
    age= 21,
    kasb= 'Backend',
    manzil= "toshkent",
    salary= "500$",
)
print(Person.hobbiy)
print(ishchi)