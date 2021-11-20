import os

def soldier(path, file, ext):
    os.chdir(path)

    if file in os.listdir(path):
        with open(file, 'r') as f:
            data = f.read().split('\n')
            print(data)
            num_lines = sum(1 for line in open(file))
            f.close()
            os.remove(file)   
            lines = 0
            for i in data:
                lines = lines + 1
                data = i.capitalize()        
                with open(file, 'a') as f:
                    if lines == num_lines:
                        f.write(str(data))
                    else:
                        f.write(str(data)+"\n")
    count = 0
    for i in os.listdir(path):
        if i.endswith("."+ext):
            count = count + 1
            os.rename(i, f"{count}.{ext}")

    for i in os.listdir(path):
        newi = i.capitalize()
        os.rename(i, newi)        


if __name__ == "__main__":
    path = input("Enter the path of folder: ")
    file = input("Enter the file name with extension: ")
    ext = input("Enter the file extension to change them in number sequence: ") 
    soldier(path, file, ext)                