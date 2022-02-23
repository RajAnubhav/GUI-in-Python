# class Employee:
#     def __init__(self, fname, lname, salary):
#         self.fname = fname  # this fname is the passed value of the variable to the function
#         # self.fname is the variable made by the class
#         self.lname = lname
#         self.salary = salary

    
# harry = Employee('harry', 'jackson', 440000)
# rohan = Employee('rohan', 'das', 230000)

# print(harry.fname, rohan.fname)

# class Employee:

#     increment = 1.5
#     def __init__(self, fname, lname, salary):
#         self.fname = fname
#         self.lname = lname
#         self.salary = salary

#     def increase(self):
#         self.salary = self.salary * self.increment


# harry = Employee('harry', 'bhai', 1)
# rohan = Employee('rohan', 'bhai', 1)
# rohan.increase()
# print("Salary of Rohan: ",rohan.salary)
# harry.increase()
# print("Salary of Harry: ", harry.salary)

class Employee:
    sum = 0.0
    def __init__(self, name, clas, roll, marks):
        self.name = name
        self.clas = clas
        self.roll = roll
        self.marks = marks

    def getMarks(self, n):
        for i in range(n):
            self.marks = int(input())
            self.sum += self.marks

    def setMarks(self, n):
        print(f"The average sum of marks achieved by {self.name}", self.sum / n)


harry = Employee('harry', 10, 9, 120)
harry.getMarks(5)
harry.setMarks(5)