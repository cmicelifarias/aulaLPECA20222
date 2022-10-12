import math

class Poligono:
    def falar(self): print("Sou uma forma")

class Retangulo(Poligono):

    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    def calcula_area(self,base,altura):
        return self.base*self.altura

class Quadrado(Poligono):

    def __init__(self, lado):
        self.lado = lado

    def falar(self): print("Sou um quadrado")
    
    def calcula_area(self):
        return self.lado**2

class Circulo(Poligono):

    def __init__(self, raio):
        self.raio = raio

    def falar(self): print("Sou um circulo")
    
    def calcula_area(self):
        return math.pi*self.raio**2

a = Poligono()
b =  Quadrado(2)
c = Circulo(3)

a.falar()
b.falar()
c.falar()
print(b.calcula_area())
print(c.calcula_area())
a.calcula_area()
