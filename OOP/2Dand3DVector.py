class Vector2D:

    def __init__(self, i, j):
        self.capI = i
        self.capJ = j

    def __str__(self):
        return f"{self.capI}i + {self.capJ}j"

class Vector3D(Vector2D):

    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.capK = k

    def __str__(self):
        return f"{self.capI}i + {self.capJ}j + {self.capK}k"     


v2d = Vector2D(3,4)
print(v2d)
v3d = Vector3D(5,4,1)
print(v3d)



