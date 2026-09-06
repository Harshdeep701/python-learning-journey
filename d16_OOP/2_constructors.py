class Employee:
    def __init__(self, salary ,name,bond):
        self.salary= salary #create an isntance attribute of nam salry and assign it with salary 
        self.name= name
        self.bond=bond

    def get_salary(self): 
        return self.salary
    
    def get_info(self):
        print (f"The name of the emlpoyee is {self.name}. Salary is {self.salary}. The bond is for {self.bond }year")
    
e1 = Employee(34000,"john",4)
print(e1.get_salary())
e1.get_info()
print(e1.get_info())