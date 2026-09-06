from functools import reduce
a =[1,2,3,4,5,6]
#how reduce function work
#  [3,3,4,5,6]
#  [6,4,5,6]
#  [10,5,6]
#  [15,6]
#  [21] final output 

def sum(a,b):
    return a+b

c= reduce(sum,a)
print(c)