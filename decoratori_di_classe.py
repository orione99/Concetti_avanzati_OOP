class Matematica:
    @staticmethod
    def somma(a,b):
        return a + b

print(Matematica.somma(3,5))

class Persona:
    def __init__(self,nome,eta):
        self.nome = nome
        self.eta = eta

    @classmethod
    def da_stringa(cls,stringa):
        nome,eta = stringa.split('-')
        return cls(nome,int(eta))
    
p = Persona.da_stringa('Marco-25')
print(p.nome,p.eta)

class Rettangolo:
    def __init__(self,base,altezza):
        self.base = base
        self.altezza = altezza

    @property
    def area(self):
        return self.base * self.altezza   
    
r = Rettangolo(5,3)
print(r.area)

class studente:
    def __init__(self,nome,eta,materia):
        self.nome = nome
        self._eta = eta
        self.materia = materia
    
    @classmethod
    def da_stringa(cls,stringa):
        nome,eta,materia = stringa.split('-')
        return cls(nome,int(eta),materia)
    
    @property
    def anno_di_nascita(self):
        return 2026 - self.eta
    
    @property
    def eta(self):
        return self._eta
    
    @eta.setter
    def eta(self,nuova_eta):
        if nuova_eta < 0:
            print('età sbagliata')
        else:
            self._eta = nuova_eta

p1 = studente.da_stringa('Giovanni-26-Inormatica')
print(p1.nome,p1.eta,p1.materia)
print(p1.anno_di_nascita)
print(p1.eta)


class personaggio:
    def __init__(self,nome,danno):
        self._nome = nome
        self.danno = danno
    
    @classmethod
    def punti_danno(cls,nome,punti_danno):
        danno = f'{punti_danno} punti danno'
        return cls(nome,danno)
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self,nuovo_nome):
        if nuovo_nome == 'Merlino':
            self._nome = nuovo_nome
            print('Merlino è un mago')
        else:
            print('non valido')

a1 = personaggio.punti_danno('Merlino',50)
print(a1.nome,a1.danno)
a1.nome = 'Merlino'
print
    

