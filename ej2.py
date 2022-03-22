"""Diseñe e implemente las clases Circle y Cylinder,
empleando composición y luego empleando herencia,
de manera tal que pueda calcular el área y el volumen respectivamente.
"""

import math

# Usando COMPOSICIÓN
class Circle:
#A = Π x r²
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * math.pow(self.radio, 2)


class Cylinder:
    #V = Π h r², es decir, Pi por altura por radio al cuadrado.
    def __init__(self, radio, altura):
        self.radio = Circle(radio)
        self.altura = altura

    def volumen(self):
        return Circle.area(self.radio) * self.altura


# Usando Herencia
class CylinderHer(Circle):

    def __init__(self, radio, altura):
        super().__init__(radio)
        self.altura = altura

    def volumen(self):
        return self.area() * self.altura

cilindro = Cylinder(int(input("introducir radio ")), 5)

print(cilindro.volumen())
