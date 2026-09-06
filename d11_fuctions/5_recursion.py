'''
fibonacci using recursion 
0 1 1 2 3 5 8 13 # this is fib series 
0 1 2 3 4 5 6 .... # this is index of the values 
to obtain this fibonacci series you can write a code
in this way 
fib(0) = 0
fib(1) = 1
fib(2) = fib(0)+fib(1)
fib(3) = fib(1)+fib(2)
fib(4) = fib(2)+fib(3)
fib(n) = fib(n-2)+fib(n-1)
and this is how you should you write fibonacci series 
 '''
def fib(n):
    #base case of fib series 
    if(n==0 or n==1):
        return n 
    return fib(n-2)+fib(n-1)
print(fib(6))
# this how the recursion is work for the 6 
fib(4) + fib(5)
fib(2) + fib(3) + fib(5)
fib(0) + fib(1) + fib(3) + fib(5)
0 + 1 + fib(1) + fib(2) + fib(3) + fib(4)
0 + 1 + 1 + fib(0) + fib(1) + fib(1) + fib(2)+ fib(4)
0 + 1 + 1 + 0 + 1 + 1 + fib(0) + fib(1) + fib(2) + fib(3)
0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + fib(0) + fib(1) + fib(3)
0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + fib(1) + fib(2)
0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + 1 + fib(0) + fib(1)
0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + 1 + 0 + 1