class Patient:
    def __init__(self,secondName,name, surname,adres,medical_digits, disias):
        self.secondName = secondName
        self.name = name
        self.surname= surname
        self.Adres = adres
        self.medical_digits = medical_digits
        self.disias = disias

    def Set(self):    
        return self.__dict__.keys()
            
    def show(self):
        print(self.__dict__.keys())
        
first = Patient("Иванов","Иван", "Иванович","ул.Гагарина-14","1012", "Ветрянка")
second = Patient("Александров","Александр","Александрович","ул.пушкина-1","2531","Covid-19")
third = Patient("Андреев","Адрей","Андреевич","ул.Чапаева-91","6001","Covid-19")
fourth = Patient("Михайлов","Михаил","Михайлович","ул.Купало","4991","Язва")
all = [first,second,third,fourth]; out = []
#1
diagnos = input("Диагноз: ")
for i in all:
    if i.disias == diagnos:
        out.append(i.name)
print(out)
#2 
out = []
a = input("BEGG: "); b = input("END: ")
for i in all:
    if i.medical_digits >= a and i.medical_digits <= b:
        out.append(i.name)
print(out)
