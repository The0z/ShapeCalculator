import math


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return "Rectangle(width=" + str(self.width) + ", height=" + \
                str(self.height) + ")"

    # Setters
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    # Getters
    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2*self.width + 2*self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        msg = ""
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        for i in range(self.height):
            msg += "*"*self.width + "\n"
        return msg

    def get_amount_inside(self, shape):
        vert = math.floor(self.height/shape.height)
        horz = math.floor(self.width/shape.width)
        return int(vert*horz)


class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return "Square(side=" + str(self.width) + ")"

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, side):
        self.set_side(side)

    def set_height(self, side):
        self.set_side(side)
