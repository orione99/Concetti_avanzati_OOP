from abc import ABC, abstractclassmethod
class veicolo():
    @abstractclassmethod
    def muovi(self):
        pass
class aereo(veicolo):
    def muovi(self):
        print("L'aereo vola in cielo")
class auto(veicolo):
    def muovi(self):
        print("L'auto si muove su strada")

a1 = auto()
a2 = aereo()

a1.muovi()
a2.muovi()


class personaggio():
    def __init__(self, nome, danno, vita):
        self.nome = nome
        self.danno = danno
        self.vita = vita
    @abstractclassmethod
    def attacco(self,bersaglio):
        pass
    def è_morto(self):
        return self.vita <= 0
    
class mago(personaggio):
    def attacco(self,bersaglio):
        bersaglio.vita -= self.danno
        print(f"{self.nome} lancia una magia su {bersaglio.nome} (-{self.danno} vita)")

class guerriero(personaggio):
    def attacco(self,bersaglio):
        bersaglio.vita -= self.danno
        print(f"{self.nome} colpisce {bersaglio.nome} con la spada (-{self.danno} vita)")
    
merlino = mago('Merlino', 50, 250)
achille = guerriero('Achille', 60, 200)

while not merlino.è_morto() and not achille.è_morto():
    merlino.attacco(achille)
    if achille.è_morto():
        print('Achille è morto')
        break
    achille.attacco(merlino)
    if merlino.è_morto():
        print('Merlino è morto')
        break