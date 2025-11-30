class Employee:
    def describe(self):
        return f"they have lot of items in her house"
    
class Manager(Employee):
    def describe(self):
        return f"eshmat manager"

employee = Employee()
manager = Manager()

print(employee.describe())
print(manager.describe())