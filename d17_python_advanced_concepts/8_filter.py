def is_greater_then_9(x):
    if x>9:
        return True
    else:
        return False 
    
a = [1,3,5,234,34,32,6545,23,2,5,6,7,43]

new = list(filter(is_greater_then_9,a))
print(new)