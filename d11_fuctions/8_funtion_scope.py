def sum(a,b):
    # and b are local variables
    c= a+b
    z= 1 # it create a local variable called z which is destroyed after this functions
    return c

def greet():
    z = 32 # local varialbe
    print("hello ")

z = 8 # z is a global variable
print(z)
print(sum(4,6))
print(z )
