class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position 
        self.salary = salary
        
    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)
        
    def __str__(self):
        return(f"{self.name} is {self.age} years old. Employee is a {self.position} with the salary of ${self.salary}")
    
    def __repr__(self):
        return (
            f"Employee("
            f"{repr(self.name)}, {repr(self.age)}, "
            f"{repr(self.position)}, {repr(self.salary)})"
            )

employee1 = Employee("Ji-Soo", 38, "developer", 1200)
employee2 = Employee("Lauren", 44, "tester", 1000)
print(eval(repr(employee1)))


# The process of using a class to create a new object is called Instantiation.

# You can give functionality to your class and pass it to the instances of your object/class. Functions inside of a class are known as methods or instance functions/methods.

# The __str__ function is the first default built in method within the class that is retrieved, so to pass the __str__ when calling an instance, is the norm. The point of this method is to return something that the print function will be able to print, so it makes no sense to print this inside of the method too. The __str__ returns a readable representation of an object/instance.

# The __repr__ function returns a more information-rich, or official, string representation of an object. This method is called by the built-in repr() function. If possible, the string returned should be a valid Python expression that can be used to recreate the object.