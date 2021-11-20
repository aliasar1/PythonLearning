def calcSpecificAge(hundAt):
    try: 
        specificYear = int(input("Please enter year in which you want to find your age: "))
        calcAge = specificYear - (hundAt - 100)
        if calcAge < 0:
            print("You are not even born yet!")
        elif calcAge == 0:
            print("You will only be few months old.")
        else:
            print(f"You will be {calcAge} years old in year {specificYear}")
    except Exception as e:
        print("Error Found: " + str(e))
        calcSpecificAge(hundAt)

def remarks(age):
    if age > 150:
        print("Wow! You are my be the oldest person alive.")    

def predictions(userInput):
    if len(str(userInput)) == 4:
        age = CurrentYear - userInput
        remarks(age)
        hundAt = userInput + 100
        print(f"You will be 100 years old in year {hundAt}")
        calcSpecificAge(hundAt)

    elif len(str(userInput)) < 4:
        YOB = CurrentYear - userInput
        age = CurrentYear - YOB
        remarks(age)
        hundAt = YOB + 100
        print(f"You will be 100 years old in year {hundAt}")
        calcSpecificAge(hundAt)

    else:
        print(f"Error in calculating age, sorry!")    


if __name__ == "__main__":
    while True: 
        try:
            CurrentYear = 2021
            hundAt = 0

            userInput = int(input("\nPlease enter your age or birth year: "))
            predictions(userInput)

            cont = int(input("If you want to exit, press 1: "))
            if cont == 1:
                break
        except Exception as e:
            print("Error Found: " + str(e))    