class Human:
    default_name = "Ivan"
    default_age = 20

    def __init__(self, age = default_age, name= default_name, __money = 0, __property= 0 ):
        self.age = age
        self.name = name
        self.__money = money
        self.__property = property

    def info(self):
        print(self.age, self.name, self.__money, self.__property)

    def default_info(self):
        print(self.default_age, self.default_name)

    def __make_deal(self, praise):
        self.__money -= self.praise;

    def earn_money(self, salary):
        self.__money += salary        

    def buy(self, artic, bought):
        if self.__money >= bought:
            self.__make_deal(title + price)
        else:
            print("недостаточно")   

    def __iadd__(self, other):
        self.__money += other
    
    def __isub__(self, other):
        self.__money -= other 

    def __imul__(self, other):
        self.__money *= other

    def __itruediv__(self, other):
        self.__money /= other