class Rectangle:
    def __init__(self, width: int, height : int):
        self.width = width
        self.height = height

    def set_width(self, width :int):
        self.width = width

    def set_height(self, height : int):
        self.height = height

    def get_area(self):
        return (self.width*self.height)

    def get_perimeter(self):
        return (2*self.width + 2*self.height)

    def get_diagonal(self):
        return ((self.width**2 + self.height**2) ** .5)

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return 'Too big for picture.'
        pict = ''
        for i in range(self.height):
             pict += '*'*self.width+'\n'
        return pict

    def get_amount_inside(self, shape : object):
        totals = self.height*self.width
        return int(totals/(shape.width*shape.height))

    def __repr__(self) -> str:
        return f'Rectangle(width={self.width}, height={self.height})'

class Square(Rectangle):
    def __init__(self, side : int):
        super(Square, self).__init__(side, side)
        self.side = side

    def set_side(self, side : int):
        self.side = side
        super().__init__(side, side)

    def set_width(self, width :int):
        self.side = width
        super().__init__(self, width)

    def set_height(self, height : int):
        self.side = height
        super().__init__(self, height)

    def __repr__(self) -> str:
        return f'Square(side={self.side})'
