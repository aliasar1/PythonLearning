# Wipe content of files

#with open("Filings/wipable.txt", "w") as f:
#    f.write("")

#Renaming files 

import os

oldFile = "wipable.txt"
newName = "renamed.txt"

with open(oldFile) as f:
    content = f.read()

with open(newName, "w") as f:
    f.write(content)

os.remove(oldFile)
