class Point:  #класс
    x = 0 # атрибуты ( переменные внутри класса)
    y = 0
    def coordinates(self):  # метод для класса
        print(f'координаты: x {self.x}, y {self.y} ')

my_point = Point()

my_point.coordinates()

my_point.x = 10
my_point.y = -5

my_point.coordinates()

class Point:
    def __init__(self, x, y):#конструктор класса 
        self.x = x
        self.y = y
    def coordinates(self):  # метод для класса
        print(f'координаты: x {self.x}, y {self.y} ')
    def __repr__(self):
        return f'<Point x: {self.x}, y: {self.y}>'

my_point = Point(1, 3)
my_point.coordinates()
my_point.x = 10
my_point.y = -5
my_point.coordinates()
print(my_point) # адрес объекта, если без def __repr__

          