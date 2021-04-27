class point4:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        

    def __sub__(self, other):
        x = self.x - other.x 
        y = self.y - other.y
        return point4(x, y)

    def __mul__(self,other):
        x = self.x * other.x
        y = self.y * other.y
        return point4(x,y)      

    def __truediv__(self,other):
        x = self.x / other.x
        y = self.y / other.y
        return point4(x, y)       

    def __eq__(self, other):
        return self is other                  

        
dot1 = point4(2 , 4)
dot2 = point4(5 , 1)
c1 = dot1 - dot2
c2 = dot2 * dot1
c3 = dot1 / dot2
bool_type =(dot1 == dot2)
print(c1.x, c1.y)
print(c2.x, c2.y)
print(c3.x, c3.y)
print(bool_type)
