# This program finds WORD from file if it exists.

with open("Filings\poems.txt", "r") as f:
    data = f.read()
    if "twincle" in data:
        print("Twincle word is present in file.")
    else:
        print("Twincle word is not present in file.")    
