class Ponto:

    def __init__(self, x, y):
    
        self.set_x(x)
        self.set_y(y)


    def set_x(self, x):

        if isinstance(x, float):
           self._x = x
        else:
            print("Entre com uma coordenada X válida (float)!")

    def set_y(self, y):

        if isinstance(y, float):
           self._y = y
        else:
            print("Entre com uma coordenada Y válida (float)!")

    def get_x(self):

        return self._x


    def get_y(self):

        return self._y


    def origem(self):

        return (self._x**2+self._y**2)**(1/2)

    def __str__(self):

        return f"Ponto({self._x}, {self._y})"
        


class Circulo(Ponto):

    def __init__(self, x, y, r):

        super().__init__(x, y)
        self.set_r(r)

    def get_r(self):

        return self_r

    def set_r(self, r):

        if isinstance(r, float):
           self._r = r
        else:
            print("Entre com um valor válido de raio (float)!")

    def area(self):

        return (22/7)*self._r**2
    
    def perimeter(self):

        return 2*(22/7)*self._r

    def __str__(self):

        return f"Circulo({self._x}, {self._y}, {self._r})"



class Line:

    def __init__(self, x1, y1, x2, y2):

        self.p1 = Ponto(x1, y1)
        self.p2 = Ponto(x2, y2)


    def distance(self):

        pass


    def __str__(self):

        pass







