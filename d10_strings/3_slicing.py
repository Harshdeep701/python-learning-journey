name = "Harsh"
print(name[0:2]) # goes from 0 to 2-1(n-1) which mean 0 to 1 
print(name[2:-1]) #same as name[2:4] which mean from 2 to 3 

print("Part two:")
# skiping the charcters 
value = "Harsh0123456789"

#print(value[0:10:n]) it mean skip the n-1 characters

print(value[0:10:1]) # skip 0 characters
print(value[0:10:2]) # skip 1 characters
print(value[0:10:3]) # skip 2(3-1) characters

print("Part 3")
print(value[:4]) # replace the first empty number with 0 # value[0:4]
print(value[1:])# replace the second empty number with length # value[1:15]