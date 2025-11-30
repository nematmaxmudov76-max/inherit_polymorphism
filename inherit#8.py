class Hero:
    def __init__(self):
        pass
    def __str__(self):
        return f"yengilmas"

class Spiderman(Hero):
    def Spiderman_power(self):
        return f"dangerous geroy"
res = Hero()
sp = Spiderman()
print(res)
print(sp.Spiderman_power())