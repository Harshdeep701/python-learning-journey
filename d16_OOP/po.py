class Person:
    def __init__(self, name, age): # name and age are attibutes
        self.name = name
        self.age = age
p1 = Person("John",45) #p1 is instance 
print(p1.name, p1.age)
