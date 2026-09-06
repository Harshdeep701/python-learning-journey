class Employee:
    company = "asus" #This is class attributes

    def __init__(self, salary ,name,bond, company):
        self.salary= salary #create an isntance attribute of nam salry and assign it with salary 
        self.name= name
        self.bond=bond
        self.company=company

    def get_salary(self): 
        return self.salary
    
    def get_info(self):
        print(f"The name of the emlpoyee is {self.name}. Salary is {self.salary}. The bond is for {self.bond }year")

e1 = Employee(3400,"john",3,"Tesla")
print(e1.company) #it will always print instance attribute wheneven present 
print(Employee.company) # this will always print class attributes 
#object introspection
print(dir(e1)) # it will print all the methods 