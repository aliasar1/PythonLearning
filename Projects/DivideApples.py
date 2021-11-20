def check(n, mn, mx):
    for i in range(mn, mx+1):
        if mn == mx:
            print(f"Range is not defined as {mn} and {mx} are equal.")
        elif n%i == 0:
            print(f"{i} is divisible by {n}")
        else:
            print(f"{i} is not divisible by {n}")  

if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter total number of apples: "))
            mn = int(input("Enter minimum range: "))
            mx = int(input("Enter maximum range: "))
            check(n, mn, mx)
        except Exception as e:
            print("Error Found: " + str(e))   
