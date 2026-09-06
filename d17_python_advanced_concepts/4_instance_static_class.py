class Employee:
    company="hp"
    def __init__(self, name, salary): #costructor made
        self.name = name # name and slary is an attibute belong to an object 
        self.salary = salary
    #instancd methos (default)    
    def print_info(self):
        info= f"The name is {self.name} and they salary is {self.salary}"
        print(info)

    #static method is a metod which does not require a slef to work 
    @staticmethod
    def sum(a,b):
        return a+b

    #class method
    @classmethod
    def print_company(cls):
        print(cls.company) # we are doing this because we want employee in this method  when we want to refer this class
    @classmethod
    def change_company(cls,new_company ):
        cls.company=new_company #when we want to change the company from hp to new_company

e1 = Employee("jacl",45)
e2= Employee("jill",345)
print(Employee.company)
print(e1.company) # same output

e1.print_info()
print(e1.sum(5,9))

e1.print_company()
e1.change_company("dell")
e1.print_company()