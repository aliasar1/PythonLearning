i = 5 #Global Varibale

def add(a):
    i = 2 #Local Varibale
    # Local variable is priority, if not found then it search in global scope.
    return a+i



def subtract(a):
    global i # This will change global varibale.
    i = 12
    return i - a     

print(add(5))   
print(subtract(2)) 
print(i) # Global variable changed using global keyword in subtract method.