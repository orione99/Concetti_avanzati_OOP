class Product:
    def __init__(self, name = str, price = float):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name} - {self.price:.2f}$'
    
    def __eq__(self,other):
        if not isinstance(other, Product):
            return False
        return self.name == other.name and self.price == other.price
    
class shoppingCart:
    def __init__(self):
        self.items = []
    
    def add_product(self,product : Product):
        self.items.append(product)

    def remove_product(self, product : Product):
        if product in self.items:
            self.items.remove(product)

    def total_price(self):
        return sum(p.price for p in self.items)
    
    def __len__(self):
        return len(self.items)

    def __str__(self):
        if not self.items:
            return f'Carrello vuoto'
        lines = ['Carrello']
        for p in self.items:
            lines.append(f'-{p}')
        lines.append(f'Totale: ${self.total_price():.2f}')
        return'\n'.join(lines)
    def __add__(self,other):
        new_cart = shoppingCart()
        new_cart.items = self.items + other.items
        return new_cart