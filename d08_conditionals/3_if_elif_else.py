age = int(input("Enter your age"))

if(age>21):
    print("You can drive")
elif(age==18):
    print("Lets schedule an interview")
elif(age==0):
    print("Hey you just born")
elif(age>19&age<21):
    print("You can do more practice to drive")    
else:
    print("You cannot drive")

print("End of the program")            