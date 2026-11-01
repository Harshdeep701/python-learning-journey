print('Hello " World')
print('Hello' , 'World' )# in output you see comma , was remove as in python it is replace by space as it use as seprator
print("Hello" , "World" )
print("Hello World" , 'Harsh',6, sep=",")
#as the comma replace by space (sep) we overwrite it with comma so now we can see the comma too
print("Hello World" , 'Harsh',6, sep="/") #now it is replace by / 
print("Hello World" , 'Harsh',6, sep="a") #now it is replace by a 
#everthing in this sep=" anything" is replace by every separate comma in the code 
print('Hello  line 9 world',end=',')#end show what come next after the code of line 
print('Harsh',end='//\n')#first end line with// and then shift to next line 
print("Hello", "World", sep=", ", end="!\n")#end with ! and then shift to next line 
print('yo')