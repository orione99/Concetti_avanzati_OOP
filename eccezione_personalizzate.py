class Età_non_correttaError(Exception):
    pass

class studente:
    def __init__(self, nome, età):
        if età < 0:
            raise Età_non_correttaError('eta inferiore a 0')
        self.nome = nome
        self.eta = età
    def __str__(self):
        return f'Nome: {self.nome} - Età: {self.eta}'

print('--- TEST ---')   
p1 = studente('Giovanni', 26)
print(p1)

class Prodotto_esauritoError(Exception):
    pass

class magazzino:
    def __init__(self, nome_prodotto, quantità):
        self.nome_prodotto = nome_prodotto
        self.quantità = quantità

    def prelievo_prodotti(self, prelievo):
        if self.quantità < prelievo:
            raise Prodotto_esauritoError(f'Quantita richiesta eccessiva, disponibilità: {self.quantità}')
        self.quantità -= prelievo
    
    def __str__(self):
        return f'- Magazzino -\n Nome prodotto: {self.nome_prodotto} - Quantità: {self.quantità}'

print('--- TEST ---')
m1 = magazzino('Penne', 25)
print(m1)

try:
    m1.prelievo_prodotti(26)
except Prodotto_esauritoError as e:
    print(e)