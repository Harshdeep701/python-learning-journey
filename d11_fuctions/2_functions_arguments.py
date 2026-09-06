#poitional arguments
def add(a,b): # a nd b are parameters 
    x = a+b
    return x
c= add(3,5) # where as 3 and 5 are arguments 
print(c)

#Default argumrnts
def add(a,b, plus =9 ): # a nd b are parameters  and we alos add plus as default arguments and assign 9 to it  
    x = a+b+plus
    return x
c= add(3,5) # where as 3 and 5 are arguments as we assign the 9 to the plus so no need to write the thired value on this line of code 
print(c)

# another ways
def add(a,b,plus=9):
    x = a+b+plus
    return x

c = add(3,5,2) #inthis the plus value is overwrite by 2 in this line of code 
print(c)

#Keywords Arguments
def add(a,b):
     return a+b
   
    
c1= add( b= 5,a=3) # same as postional but in this you can call b frist and you can call a or another variables
print(c1)