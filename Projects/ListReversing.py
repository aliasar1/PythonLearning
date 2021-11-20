list1 = [20, 30, 10, 23, 70, 30, 11]

# Method 1
l1 = list1[:] #COpy of list
l1.reverse()
print(l1)

# Method 2
l2 = list1[:]
l2 = l2[::-1]
print(l2)

# Method 3
l3 = list1[:]
for i in range(len(l3)//2):
    l3[i], l3[len(l3)-(i+1)] = l3[len(l3)-(i+1)], l3[i]
print(l3)

if l1 == l2 and l2 == l3:
    print("All list are equal.")
else:
    print("All list are not equal.")        

