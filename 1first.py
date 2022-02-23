# the class methods take whole class as an argument

class Employee:

    increment = 1.0

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age 
        self.salary = salary

    def incrementInSalary(self):
        self.salary = self.salary + self.increment

    @classmethod
    # this class method takes whole class as an argument
    def changeIncrement(cls):
        cls.increment = 2.0

harry = Employee('harry', 32, 23400)
print(f"This is the original salary of {harry.name}: ", harry.salary)
harry.incrementInSalary()
# since the @classmethod has changed the value of the variable name increment so, we are getting updated value i.e 2.0 times the salary and not 1.0 times the salary

print("This is the change in the incremented salary", harry.salary)
harry.changeIncrement()
print("This is the change in the salary", harry.salary)