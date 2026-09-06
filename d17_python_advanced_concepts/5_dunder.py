#dunder method is stand for the double underscore 
class Employee:
    company = "HP"
    def __init__(self, name, salary): #constructor function called 
        self.name = name 
        self.salary = salary

    def __str__(self):# in this we do dunder method use 
        return f"The name is {self.name} and the salary is {self.salary}"
    
    def __repr__(self): # this is also dunder method, this is mostly use by the developer 
        return f"name: {self.name}\nsalary: {self.salary}"
    
    def __len__(self): # it will return the length of this string 
        return len(self.name)


e = Employee("Harsh", 43566) # when we pass this value the comstructor function is called 
print(len(e))
# print(e.name, e.salary)
# print(str(e))
# print(repr(e))