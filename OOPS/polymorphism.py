from abc import ABC,abstractmethod

class Shape:
    
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):

    def __init__(self,radius):
        self.radius = radius

    def area(self):
        print("Area of the cicle is:",(3.14*self.radius*self.radius))

class Square(Shape):

    def __init__(self,a):
        self.a = a

    def area(self):
        print("Area of the square is:",(self.a*self.a))

class Triangle(Shape):

    def __init__(self,base,height):
        self.base = base
        self.height = height

    def area(self):
        print("Area of the triangle is:",(0.5*self.base*self.height))

class Book(Square):
    def __init__(self, a):
        super().__init__(a)     # Book shape is also square/rectangle here we used square so we used square's area function



c = Circle(6)
s = Square(5)
t = Triangle(3,6)
b = Book(14)
c.area()
s.area()
t.area()
b.area()