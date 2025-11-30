class Flyer:
    def move(self):
        return " that is flying"

class Swimming:
    def move(self):
        return "that is swimming"

class Duck(Flyer, Swimming):
    def move(self):
        return 

duck = Duck()
fly = Flyer()
swim = Swimming()

print(duck.move())
print(fly.move())
print(swim.move())

