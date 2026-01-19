import csv

class GestioneFileCSV:
    def __init__(self,file):
        self.file = file
    
    def leggi(self):
        try:
            with open(self.file, 'r') as f:  
                return list(csv.DictReader(f))
        except FileNotFoundError:
            print('File non trovato')
            return []
    
    def stampa_autore(self,autore):
        dati = self.leggi()
        for riga in dati:
            if riga['Autore'] == autore:
                print(f'Titolo: {riga['Titolo']} - Anno: {riga['Anno']}')


        
libreria = GestioneFileCSV('testo.csv')
dati = libreria.leggi()

for riga in dati:
    print(riga['Titolo']) 

libreria.stampa_autore('Mark Twain')

        
