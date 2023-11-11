class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position 
        self.salary = salary
        
    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)
        
    def info(self):
        print(f"{self.name} is {self.age} years old. Employee is a {self.position} with the salary of ${self.salary}")

employee1 = Employee("Ji-Soo", 38, "developer", 1200)
employee2 = Employee("Lauren", 44, "tester", 1000)
employee2.increase_salary(20)
employee2.info()

# The process of using a class to create a new object is called Instantiation.
# You can give functionality to your class and pass it to the instances of your object/class. Functions inside of a class are known as methods or instance functions/methods.
