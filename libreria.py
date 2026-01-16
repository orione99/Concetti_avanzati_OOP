class Book:
    def __init__(self, nome, autore):
        self.nome = nome
        self.autore = autore
    def __str__(self):
        return f'Titolo: {self.nome} - Autore: {self.autore}'
    
    def __eq__(self,altro):
        if not isinstance(altro,Book):
            return False
        return self.nome == altro.nome and self.autore == altro.autore
    
class Library():
    def __init__(self):
        self.items = []
        

    def add_book(self,book):
        self.items.append(book)
        

    def remove_book(self,book):
        if book in self.items:
            self.items.remove(book)

    def libri_totali(self):
        return len(self.items)
    
    def __str__(self):
        if not self.items:
            return f'libreria vuota'
        lines = ['Libreria']
        for p in self.items:
            lines.append(f'-{p}')
        lines.append(f'Totale: {len(self.items)} Libri')
        return '\n'.join(lines)
    
    def __add__(self,other):
        if not isinstance(other, Library):
            return False
        new_lib = Library()
        new_lib.items = self.items + other.items
        return new_lib        

    

b1 = Book("1984", "George Orwell")
b2 = Book("Il Signore degli Anelli", "Tolkien")
b3 = Book("1984", "George Orwell")

lib1 = Library()
lib1.add_book(b1)
lib1.add_book(b2)

lib2 = Library()
lib2.add_book(b3)

print(lib1)
print(lib1.libri_totali())

lib3 = lib1 + lib2
print(lib3)

lib1.remove_book(b1)
print(lib1)
    



    
    