s = "hello world" # string are immutable[you cant change orignal value ]
 
# name[0] = "R" # you cant do that

a = len(s)
print(a) # it print total lenght including space 
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())

print("Part two Removing Whitespace:-")
text = " hello world "
print(text.strip()) # Output: "hello world" 
print(text.lstrip()) # Output: "hello world " use for removing spaces 
print(text.rstrip()) # Output: " hello world"

print("Part three Finding and Replacing:-")
text = "Python is fun"
print(text.find("is")) # Output: 7 print index value of first occurance 
print(text.replace("fun", "awesome")) # Output: "Python is awesome it replace all the fun with awesome

print("\nPart four splitting and joining:- ")
text= "Apple,Bananas,Pineapples"
print(text.split(","))
print(",".join(['Apple', 'Bananas', 'Pineapples']))

print("\nPart five Checking String Properties:- ")
text = "Python123"
print(text.isalpha()) # Output: False ,it check where all the character are alphabest or not 
print(text.isdigit()) # Output: False ,it check where all the character are digit or not 
print(text.isalnum()) # Output: True ,it check where all the charcters in string contain alphabet and digit or not 
print(text.isspace()) # Output: False
