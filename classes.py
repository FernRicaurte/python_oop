class Employee:
    def __init__(self):
        self.name = "Ji-Soo"
        self.age = 38
        self.position = "developer" 
        self.salary = 1200

e = Employee()
print(e.__class__)

# I have created an object with some attributes and checked for the class using __class__ as a function or method to e.