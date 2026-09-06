s={34,23,1,3,22}
print(s)

s.add(32) # it will add the number to set at randow place 
print(s)
s.remove(23)
print(s)
# s.remove(145566) it will show an error 
s.discard(145566) # remove this element only if it present in the sets
print(s)

# python will print the output in any order as they want 
# because the set are unordered 