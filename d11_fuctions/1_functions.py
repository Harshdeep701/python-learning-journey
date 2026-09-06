a =4
b=2
c=1
average= (a+b+c)/3
print(average)

a1 =6
b1=7
c1=12
average1= (a1+b1+c1)/3
print(average1)
# rather then writing this long program you can use function to save time and reuse the code more time 

def average(a,b,c):  # any function is python is start with def keyword and adn after the name f the function is written
    d = (a+b+c)/3.0 # in this functions is define
    print("the value is:",d)

average(3,5,1) #in this line we are calling the function we define in this case we define the average function 
average(1,1,1)

print('\npart two:-')
def average(a,b,c):
     d = (a+b+c)/3.0
     return d # return fuction is use wheen we want to to give the value of d to another variables 

o=average(3,5,1) 
o1=average(1,1,1)
print(o)
print(o1)

# you can also do part two in another way
print('\npart two another way to return the value:-')
def average(a,b,c):
     return (a+b+c)/3.0
      # return fuction is use wheen we want to to give the value of d to another variables 

o=average(3,5,1) 
o1=average(1,1,1)
print(o)
print(o1)