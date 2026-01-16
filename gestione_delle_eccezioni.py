#esercizio 1
class divisione:
    def dividi(self,dividendo,divisore):
        try:
            return round(dividendo / divisore,2)
        except ZeroDivisionError:
            return 'Non si puo dividere per zero'
        
x = divisione()
print(x.dividi(44,9))
print(x.dividi(7,0))

#esercizio 2
class persona:
    def __init__(self,nome,eta):
        if eta < 0 :
            raise ValueError('Eta negativa: Errore')
        self.nome = nome 
        self.eta = eta
    
    def __str__(self):
        return f' Nome: {self.nome} - Età: {self.eta}'
        
            
a = persona('Giovanni', 26)
print(a)

b = persona('Erika', 27) #inserire un valore negativo per test
print(b)

#esercizio 3
class Banca:
    def __init__(self,nome,saldo_conto):
        self.nome = nome
        self.saldo_conto = saldo_conto

    def __str__(self):
        return f'Nome: {self.nome} - Saldo: {self.saldo_conto}'
    
    def preleva(self,importo):
        if importo > self.saldo_conto:
            raise ValueError('Saldo insufficiente')
        self.saldo_conto -= importo
    

u1 = Banca('Giovanni', 1000)
print(u1)
u1.preleva(100)
print(u1)
u1.preleva(950)