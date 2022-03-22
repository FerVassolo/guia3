"""Realizar un programa que tenga un arreglo de Figuras,
insertar círculos, rectángulos, triángulos, etc.
Recorrer la estructura, invocando perímetro y área.
Luego recorrer la estructura e imprimir la diagonal en aquellas que lo tengan definido.
Controlar si funciona la equivalencia entre figuras. Investigue la palabra clave isinstance().
"""

from ej3 import Rectangle, Circle

rectangulo1 = Rectangle(3,4)
circulo1 = Circle(5.2)
rectangulo2 = Rectangle(6.7,2)
circulo2 = Circle(2.6)

figuras = [rectangulo1,circulo1,circulo2,rectangulo2]

print(isinstance(rectangulo2, Rectangle))
print(isinstance(circulo2, Rectangle))

for figura in figuras:
    print("Area: ", figura.area())
    print("Perimetro: ", figura.perimetro())
    if isinstance(figura, Rectangle):
        print("Diagonal: ", figura.diagonales())
    else:
        print("La figura", figura, "no es un Rectangulo")
    print("\n")
