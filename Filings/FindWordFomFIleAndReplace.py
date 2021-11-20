# Find word donkey from file and replace it with ###### and update the file contents

with open("Filings/text.txt", "r") as f:
    data = f.read()


data = data.replace("donkey", "######")

with open("Filings/text.txt", "w") as f:
    f.write(data)