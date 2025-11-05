from abc import ABC, abstractclassmethod

class Shape(ABC):
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def area(self):
        return self._width * self._height

    def get_height(self):
        return self._height
        
    def set_height(self, height):
        self._height = height


class Rectangle(Shape):
    def __init__(self, width, height):
       super().__init__(width, height)

    def get_width(self):
        return self._width
        
    def set_width(self, width):
        self._width = width
        
        
  

class Square(Shape):
    def __init__(self, size):
        super().__init__(size, size)
        
    def set_width(self, width):
        self._width = width
        self._height = width
        
    def set_height(self, height):
        self._width = height
        self._height = height


r = Rectangle(5,4)
print(r.get_height())
print(r.area())
r.set_height(10)
print(r.get_height())        

s = Square(8)
print(s.get_height())
print(s.area())
s.set_width(10)
print(s.get_height())