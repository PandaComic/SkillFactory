import math
class Rectagle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def get_width(self):
        return self.width
    def get_height(self):
        return self.height
    def getArea(self):
        return self.width * self.height

class NonPositiveDigitException(ValueError):
    pass
class Square:
    def __init__(self, width):
        self.width = width
        if width <= 0:
            raise NonPositiveDigitException("Сторона квадрата не может быть меньше либо = 0!")
        def getArea_square(self):
            return self.width**2
        class Circle:
            def __init__(self, radius):
                self.radius = radius
            def get_area_circle(self):
                return math.pi*self.radius**2
