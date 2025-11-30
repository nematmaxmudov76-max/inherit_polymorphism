class Phone:
    def __init__(self,name, price, color, brend):
        self.name = name
        self.price = price
        self.color = color
        self.brend = brend

    def call(self):
        print("Caling...")

    def __str__(self):
        return f"name:{self.name}, price:{self.price}, color:{self.color}, brend:{self.brend}"


class Domashni(Phone):
    def __init__(self, name, price, color, brend, is_wired):
        self.is_wired = is_wired
        print("tuuuuut tuuuuut")
        super().__init__(name, price, color, brend)
    
class SotkaOld(Phone):
    def __init__(self, name, price, color, brend, fonar):
        self.fonar = fonar
        print("messenging")
        super().__init__(name, price, color, brend)

class SotkaNew(Phone):
    def messenging(self):
        print("Writing, calling")
    def play(self):
        print("Snake ...")

panasonik = Domashni(
    name="P234",
    price=120,
    color="black",
    brend="panasonik",
    is_wired=True
)
nokia = SotkaOld(
    name="noki3600",
    price=50,
    color="blue",
    brend="nokia",
    fonar=True
)

print(panasonik)
print(nokia)
print(issubclass(SotkaOld, Phone))


# class Animals:
#     def __init__(self, speed, speak,  name):
#         self.speed = speed
#         self.speak = speak
#         self.name = name
#     def listen_anilmals(self):
#         print("exelend")
        
# class Cat(Animals):
#     def __init__(self, spead, speak, is_whisker):
#         is_whisker = is_whisker
#         super().__init__(spead, speak, )

# class Dog(Animals):
#     def all_day(self):
#         print("all day sleaping ...")

# koshka = Cat(
#     spead= "15 m/s",
#     speak="Meaouuuu..",
#     is_whisker=True,
#     name = "Dora"
# )

# tuzik = Dog(
#     speed='20 m/s',
#     speak="WOF WOF",
#     name="tuzik"
# )
# print(Cat)
# print(Dog)


