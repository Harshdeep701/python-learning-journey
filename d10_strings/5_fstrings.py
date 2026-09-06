name = "Alice"
age = 30
name1 = "Axe"
age1 = 36
temp = "My name is {} and I am {} years old."
print("My name is {} and I am {} years old.".format(name, age))

s = temp.format(name,age) # second way of printing
print(s)
print(f"My name is {name} and I am {age} years old.")
print(f"My name is {name1} and I am {age1} years old.")

# in this we use f string 
print("ord() and chr() - Character Encoding")
print(ord('A')) # Output: 65 # print ascii value 
print(chr(65)) # Output: 'A'

pi =3.14159265
print(f"Pi rounded to 2 decimal places: {pi:.2f}")

x = 10
y = 5
print(f"The sum of {x} and {y} is {x + y}")

text = "Python"
print(f"{text:>10}") # Right align
print(f"{text:<10}") # Left align
print(f"{text:^10}") # Center align