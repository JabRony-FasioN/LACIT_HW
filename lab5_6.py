class Snow:
    def __init__(self, x):
        self.x  =x 
    def __add__(self, other):
        return Snow(self.x + other.x)
    def __sub__(self,other):
        return Snow(self.x + other.x)
    def __truediv__(self, other):
        return Snow(self.x / other.x)
    def __mul__(self, other):
        return Snow(self.x * other.x)     
    def makeSnow(self, x):
        mount = "*" * x + "/n"
        return mount * x

x1 = Snow(4)
x2 = Snow(10)
x3 = x2 + x1
print(x3.makeSnow(4))