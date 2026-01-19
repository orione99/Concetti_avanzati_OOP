class Studente:
    def __init__(self):
        pass
    def chiedi_informazioni(self):
        self.nome = str(input('Scrivi il tuo nome: '))
        self.eta = int(input('Scrivi la tua età: '))

    def presentati(self):
        print(f'Io sono {self.nome} e ho {self.eta} anni')

    def __str__(self):
        return f'Nome: {self.nome} - età: {self.eta}'


class Diario(Studente):
    def __init__(self, nome_file):
        self.nome_file = nome_file
    
    def scrivi(self,messaggio):
        with open(self.nome_file, 'a') as f:
            f.write(messaggio + '\n')

    

    def salva(self,file):
        with open(file,'w') as f:
            f.write(str(self))

    
p1 = Diario('studente.txt')
p1.chiedi_informazioni()
p1.salva('studente.txt')

with open('Studente.txt','r') as f:
        print(f.read())
