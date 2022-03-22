"""Implemente la clase Figure, y sus subclases Rectangle, Circle y Triangle.
Defina donde corresponde los métodos para obtener: perímetro, área, diagonal, altura y base.
"""
from abc import ABC, abstractmethod

class Figure(ABC):

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass

    def m1(self):
        return 1

