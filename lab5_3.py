class sum:
    def __add__(self,point):
        self.x = self.x + point.x
        self.y = self.y + point.y
        return self
staff1 = sum()
staff2 = sum()        
staff3 = staff1 + staff2   