#decorator is a function that takes a function it create  a new function inside its body(wrapper) then it return that new function 

def decorator(func): #funtion isan arguments 
    def wrapper():
        print("I ma about to execute a function")
        func()
        print("i have executed this function ")
    return wrapper

@decorator
def say_hello():
    print("hello")

# f = decorator(say_hello)
# f()   
# this is also a good way of writing a decorator the alternative way of writng decorator is write @decorator before the function you want ot call andthen simpley call the function 

say_hello() #alterantive way of calling the decorator 