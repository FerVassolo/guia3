"""Implemente la clase Figure, y sus subclases Rectangle, Circle y Triangle.
Defina donde corresponde los métodos para obtener: perímetro, área, diagonal, altura y base.
"""

from Figure import Figure
import math

class Circle(Figure):
    def __init__(self, radio):
        self.radio = radio

    def perimetro(self):
        return 2 * math.pi * self.radio

    def area(self):
        return math.pi * math.pow(self.radio, 2)


class Triangle(Figure):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        self.lado = math.sqrt(math.pow((base / 2), 2) * math.pow(altura, 2))

    def perimetro(self):
        return self.lado*2 + self.base

    def area(self):
        return (self.base * self.altura)/2

    def getbBase(self):
        return self.base

    def getAltura(self):
        return self.altura

    # el triangulo no tiene diagonales

class Rectangle(Figure):

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def perimetro(self):
        return self.base * 2 + self.altura * 2

    def area(self):
        return self.base * self.altura

    def getBase(self):
        return self.base

    def getAltura(self):
        return self.altura

    def diagonales(self):
        # por pitagoras
        return math.sqrt(math.pow(self.base, 2) + math.pow(self.altura, 2))













