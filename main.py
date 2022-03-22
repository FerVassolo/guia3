from ej2 import Cylinder, CylinderHer

print("#2")
print("Usando Composición")

cil = Cylinder(10, 10)
print(cil.volumen())

print("Usando Herencia")
cil2 = CylinderHer(10, 10)
print(cil2.volumen())
print("\n")


print("#3")
rect = Rectangle(5, 5)
print(rect.area())

print("\n")
