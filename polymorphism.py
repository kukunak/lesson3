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

    def get_color(self):
        raise NotImplementedError

    def __repr__(self):
        return f'<Product name: {self.name}, price: {self.price}, stock: {self.stock}>'
    
class Phone(Product): #наследуем класс продукта
    def __init__(self, name, price, color, stock=0, discount=0, max_discount=20):
        super().__init__(name, price, stock, discount, max_discount)
        self.color = color
    
    def get_color(self):
        return f'Цвет корпуса: {self.color}'
    def get_memory_size(self):
        #Выводимразмер памяти в Гб
        pass

    def __repr__(self):
        return f'<Phone name: {self.name}, price: {self.price}, stock: {self.stock}>'

my_phone = Phone('Iphone', 60000, 'Black', )
print(my_phone.get_color())

class Sofa(Product): #наследуем класс продукта
    def __init__(self, name, price, color, texture, stock=0, discount=0, max_discount=20):
        super().__init__(name, price, stock, discount, max_discount)
        self.color = color
        self.texture = texture
    
    def get_color(self):  #метод называется одинаково, но работает по-разному
        return f'Цвет дивана: {self.color}, Тип ткани: {self.texture}'

    def __repr__(self):
        return f'<Sofa name: {self.name}, price: {self.price}, stock: {self.stock}>'

sofa1 = Sofa('Диван', 215466, 'Gray', 'Велюр' )
print(sofa1.get_color())

# наследование позволяет выносить общую функциональность наследователя и добавлять новый функционал
# отличный от наследователя

