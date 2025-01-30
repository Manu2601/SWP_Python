class Auto():
    def __init__(self, ps):
        self.ps = ps
        
    def __add__(self, otherCar):
        if isinstance(otherCar, Auto):
            return Auto(self.ps + otherCar.ps)
        else:
            raise TypeError("nur obj(Auto) kann addiert werden.")
        
    
    def __sub__(self, otherCar):
        if isinstance(otherCar, Auto):
            if isinstance(otherCar, Auto):
                return Auto(self.ps - otherCar.ps)
        else:
            raise TypeError("nur obj(Auto) kann subtrahiert werden.")
    
    def __mul__(self, otherCar):
        if isinstance(otherCar, Auto):
            return Auto(self.ps * otherCar.ps)
        else:
            raise TypeError("nur obj(Auto) kann multipliziert werden.")
        
    def __eq__(self, otherCar):
        if isinstance(otherCar, Auto):
            return self.ps == otherCar.ps
        else:
            raise TypeError("nur obj(Auto) kann verglichen werden.")
        
    def __lt__(self, otherCar):
        if isinstance(otherCar, Auto):
            return self.ps < otherCar.ps
        else:
            raise TypeError("nur obj(Auto) kann verglichen werden.")
        
    def __gt__(self, otherCar):
        if isinstance(otherCar, Auto):
            return self.ps > otherCar.ps
        else:
            raise TypeError("nur obj(Auto) kann verglichen werden.")
        
    def __len__(self):
        return len(self.ps)
        
    
a1 = Auto(100)
a2 = Auto(130)

a3 = a1 + a2
print(a3.ps)  

a4 = a2 - a1
print(a4.ps)  

a6 = a1 * a2
print(a6.ps)  

print(a1 == a2)
print(a1 < a2)
print(a1 > a2)

try:
    a7 = a1 + 10 
except TypeError as e:
    print(e)

try:
    a8 = a1 * "Auto"
except TypeError as e:
    print(e)
