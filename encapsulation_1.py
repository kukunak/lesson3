class Product:
    def __init__(self, name, price, stock=0, discount=0, max_discount=20):
        self.name = name.strip()
        if len(self.name) <2:
            raise ValueError('Название товара должно быть 2 или более символов')
        self.price = abs(float(price))
        self.stock = abs(int(stock))
        self.discount = abs(float(discount))
        self.max_discount = abs(float(max_discount))
        if max_discount > 99:
            raise ValueError('Слишком большая максимальная скидка')
        if self.discount > self.max_discount:
            self.discount = self.max_discount
        
    def discounted(self):
        return self.prise - self.prise * self.discount / 100
    
    def sell(self, items_count=1):
        if items_count > self.stock:
            raise ValueError('Недостаточно товара на складе')
        # Здесь мы можем как-то взаимодейтствовать с учетной/бухгалтерской системой
        self.stock -= items_count

    def __repr__(self):
        return f'<Product name: {self.name}, price: {self.price}, stock: {self.stock}>'

product1 = Product('Товар', 100, stock=10)
product1.sell(5)
print(product1)