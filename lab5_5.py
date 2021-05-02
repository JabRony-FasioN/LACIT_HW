class Drob:
    def __init__(self, x=1, y=1):
        self.x = x
        self.y = y

    def normalize(self):
        if abs(self.y) > abs(self.x):
            for i in range(2, abs(self.x) + 1):
                while self.x % i == 0 and self.y % i == 0:
                    self.x /= i
                    self.y /= i
        elif abs(self.x) > abs(self.y):
            for i in range(2, abs(self.y) + 1):
                while self.x % i == 0 and self.y % i == 0:
                    self.x /= i
                    self.y /= i
        else:
            self.x = 1
            self.y = 1

    def print(self):
        print(str(int(self.x)) + '/' + str(int(self.y)))

    def __add__(self, other):
        d3 = Drob(int(self.x * other.y + other.x * self.y), int(self.y * other.y))
        return d3

    def __sub__(self, other):
        d3 = Drob(int(self.x * other.y - other.x * self.y), int(self.y * other.y))
        return d3

    def __mul__(self, other):
        d3 = Drob(int(self.x * other.x), int(self.y * other.y))
        return d3

    def __truediv__(self, other):
        d3 = Drob(int(self.x * other.y), int(self.y * other.x))
        return d3

    def __lt__(self, other):
        if self.x / self.y < other.x / other.y:
            return True
        else:
            return False

    def __le__(self, other):
        if self.x / self.y <= other.x / other.y:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.x / self.y == other.x / other.y:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.x / self.y > other.x / other.y:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.x / self.y >= other.x / other.y:
            return True
        else:
            return False


d1 = Drob(3, 9)
d1.normalize()
d1.print()
d2 = Drob(4, 6)
d2.normalize()
d2.print()
d3 = d1 + d2
d3.normalize()
print('Сумма дробей:')
d3.print()
d3 = d1 - d2
d3.normalize()
print('Разность дробей:')
d3.print()

d3 = d1 / d2
d3.normalize()
print('Частное дробей:')
d3.print()

d3 = d1 * d2
d3.normalize()
print('Проивзедение дробей:')
d3.print()
print('Сравнение дробей d1 и d2:')
d1.print()
d2.print()
print('d1 > d2: ' + str(d1 > d2))
print('d1 >= d2: ' + str(d1 >= d2))
print('d1 < d2: ' + str(d1 < d2))
print('d1 <= d2: ' + str(d1 <= d2))
print('d1 == d2: ' + str(d1 == d2))
