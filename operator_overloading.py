import math
class frazione:
    def __init__(self,num,den):
        self.num = num
        self.den = den
    def __add__(self,altro):
        num = self.num *altro.den + altro.num * self.den
        den = self.den * altro.den
        return frazione(num,den)
    def __eq__(self,altro):
        return self.num * altro.den == self.den * altro.num
    def __str__(self):
        return f'{self.num}/{self.den}'
    def _semplificata(self):
        mcd = math.gcd(self.num,self.den)
        self.num //= mcd
        self.den //= mcd
        


f1 = frazione(3,4)
f2 = frazione(3,4)
f3 = f1 + f2
f3._semplificata()

print(f1 == f2)
print(f1)
print(f3)