# Match cases
a =int(input("Enter the number between 1 and 10:"))
match a :# : it tell the block start form this 
    case 1:
        print("You won a charger") 
    case 3:
        print("You won $3")
    case 6:
        print("You won a camera ")
    case _:
        print("Better luck next time ")    