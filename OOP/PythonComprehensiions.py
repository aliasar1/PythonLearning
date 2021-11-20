ls = input("Enter a list element separated by space ")
ls = ls.split()
print(ls)

conv = int(input("Press 1: List\nPress 2: Dictionary\nPress 3: Sets"))

if conv == 1:
    ls1 = [i for i in ls]
    print(ls1)
    print(type(ls1))

elif conv == 2:
    dict = {f"item: {i}" for i in ls}
    print(dict)
    print(type(dict)) 

elif conv == 3:
    st = {i for i in ls}
    print(st)
    print(type(st))       
