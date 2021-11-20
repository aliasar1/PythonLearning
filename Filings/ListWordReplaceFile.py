# Replace words that are present in the list from file and censore it.

words = ["apple", "cute", "ali", "best"]

with open("Filings\sample.txt", "r") as f:
    data = f.read()

for i in range(len(words)):
    data = data.replace(words[i], "######")

with open("Filings\sample.txt", "w") as f:
    f.write(data)