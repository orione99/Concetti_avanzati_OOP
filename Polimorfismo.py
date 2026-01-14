#definisco la classe 'forma' e le sottoclassi 'rettangolo' e 'cerchio'
#creo la funzione area() e la adatto per ciascuna forma
import math
class forma:
    def area(self):
        pass
class rettangolo(forma):
    def __init__(self,base,altezza):
        self.base = base
        self.altezza = altezza
    def area(self):
        return self.base * self.altezza 
class cerchio(forma):
    def __init__(self,raggio):
        self.raggio = raggio
    def area(self):
        return  math.pi * (self.raggio ** 2) 

#creo la forma rettangolo e cerchio e ne stampo le aree
r1 = rettangolo(10,10)
c1 = cerchio(10)

print(r1.area())
print(c1.area())