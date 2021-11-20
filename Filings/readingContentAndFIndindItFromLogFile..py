# Reading log file and finding the line where it is present and displaying what is present. Checking for word pyhton.

content = True
i = 1
with open("Filings\log.txt", "r") as f:

    while content:
        content = f.readline()
        if "python" in content.lower():
            print(f"Yes python is present on line {i}")
            print(content, end="")
        i+=1