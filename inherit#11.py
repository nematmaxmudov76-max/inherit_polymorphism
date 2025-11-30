class Bird:
    def __init__(self, type):
        self.type = type

    def fly():
        return f"flying...."
class Parrot(Bird):
    def parrot():
        return f"don't flying"
    
    def __str__(self):
        print(f"animals type:{self.type}")
        return super().__str__()
par =  Parrot(
    type="wild animla"
)

print(Bird.fly())        
print(Parrot.parrot())
print(par)