class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getXY(self):
        return [ self.x,self.y ]

    def Show(self,point):
        print(point, "= (", self.x, "; ", self.y,")")