# enumerate(iterable, start=0)

# Parameters:
# Iterable: any object that supports iteration
# Start: the index value from which the counter is to be started, by default it is 0


l1 = ["eat","sleep","repeat"]
s1 = "geek"
 
# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)
 
print ("Return type:",type(obj1))
print (list(enumerate(l1)))
 
# changing start index to 2 from 0
print (list(enumerate(s1,2)))

