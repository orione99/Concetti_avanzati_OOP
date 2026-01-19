class appunti:
    def __init__(self, nome_file):
        self.nome_file = nome_file

    def scrivi(self,testo):
        with open(self.nome_file, 'a' ) as f:
            f.write(testo + '\n')

    def leggi(self):
        try:
            with open(self.nome_file, 'r') as f:
                print(f.read())
        except FileNotFoundError:
            print('File non trovato')
        
    def cancella(self):
        open(self.nome_file, 'w' ).close()

x = appunti('testo.txt')
x.scrivi('ciao sono giovanni')
x.scrivi('ho 26 anni')
x.leggi()


