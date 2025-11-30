class Device:
    def status(self):
        return "ideal"

class Phone(Device): 
    def status(self):
        return f"company is perfect"
class Laptop(Device):
    def status(self):
        return 'good'
    
device = Device()
phon =Phone()
laptop = Laptop()
print(device.status())
print(phon.status())
print(laptop.status())