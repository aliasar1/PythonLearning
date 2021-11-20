class Vector:

    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f" {i}a{index} +"
            index += 1
        return str1[:-1]

    def __add__(self, vec2):
        if len(self.vec) == len(vec2.vec):
            newLists = []
            for i in range(len(self.vec)):
                newLists.append(self.vec[i] + vec2.vec[i])
            return Vector(newLists)
        else:
            print("Addition failed due to dimension mismatch.")      

    def __mul__(self, vec2):
        if len(self.vec) == len(vec2.vec):
            sum =0
            for i in range(len(self.vec)):
                sum += (self.vec[i] * vec2.vec[i])
            return sum   
        else:
            print("Multiplication failed due to dimension mismatch.")   

v1 = Vector([1,4,6])    
v2 = Vector([1,6,9]) 
print(v1+v2)   
print(v1*v2)

