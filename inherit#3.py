class Person:
    def __init__(self,name,age, kasb):
        self.name = name
        self.age = age
        self.kasb = kasb

    def hobbiy(self):
        print("har kuni kitob o'qidi")
    
class Employee(Person):
    def __init__(self, salary):
        self.salary = salary
        super().__init__()
    def __str__(self):
        print(f"name:{self.name}, age;{self.age},kasb:{self.kasb}, maoshi:{self.salary}")
        return super().__str__()
    
ishchi = Employee(
    name= "eshmat",
    age= 21,
    kasb= 'Backend',
    salary= "500$"
)
print(Person.hobbiy)
print(ishchi)