# First creating two files in which 2nd file copy content of 1st file then will check if files are identical or not.

## This will make copy of this.txt as copy.txt
#with open("Filings/this.txt") as f:
#    content = f.read()
#
#with open("Filings/copy.txt", "w") as f:
#    f.write(content)    

f1 = "Filings/this.txt"
f2 =  "Filings/copy.txt"


with open("Filings/this.txt") as f:
    content1 = f.read()

with open("Filings/copy.txt", "r") as f:
    content2 = f.read() 

if content1 == content2:
    print("Both files are identical.")
else:
    print("Both files are not identical.")    