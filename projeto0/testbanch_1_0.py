from package.shapes_2d import Ponto, Circulo, Line



def workspace():

    p1 = Ponto(2.0,3.0)
    print(p1)
    
    c1= Circulo(4.0,5.0,3.0)
    print(c1)
    print(f"A area do circulo eh: {c1.area()}")

    l1= Line(1.0, 3.0, 4.2, 5.3)
    print(l1.p1)
    print(l1.p2)


if __name__ == "__main__":

    workspace()
