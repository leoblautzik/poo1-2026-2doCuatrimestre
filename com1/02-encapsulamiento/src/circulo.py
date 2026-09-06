from __future__ import annotations

import math

from src.punto import Punto


class Circulo:
    def __init__(self, centro: Punto, radio: float):
        self.radio = radio
        self.__centro = centro

    @property
    def radio(self):
        return self.__radio

    @radio.setter
    def radio(self, nuevo_radio):
        if nuevo_radio <= 0:
            raise ValueError("El radio debe ser mayor que cero")
        self.__radio = nuevo_radio

    @property
    def diametro(self):
        return self.radio * 2

    @diametro.setter
    def diametro(self, nuevo_diametro):
        self.radio = nuevo_diametro / 2

    @property
    def perimetro(self):
        return self.radio * 2 * math.pi

    @perimetro.setter
    def perimetro(self, nuevo_perimetro):
        self.radio = nuevo_perimetro / (2 * math.pi)

    @property
    def area(self):
        return math.pi * self.radio * self.radio

    @area.setter
    def area(self, nuevo_area):
        self.radio = math.sqrt(nuevo_area / math.pi)

    @property
    def centro(self) -> Punto:
        return self.__centro

    @centro.setter
    def centro(self, nuevo_centro: Punto) -> None:
        self.__centro = nuevo_centro

    def __str__(self):
        s = "Soy un círculo felíz\n"
        s += f"radio: {self.__radio}\n"
        s += f"diametro: {self.diametro}\n"
        s += f"perimetro: {self.perimetro}\n"
        s += f"area: {self.area}"
        return s

    def intersecta_con(self, otro_circulo: Circulo) -> bool:
        return (
            self.centro.distancia(otro_circulo.centro)
            <= self.radio + otro_circulo.radio
        )


def main():
    circulito = Circulo(Punto(1, 1), 4)
    print(circulito)
    circulito.radio = 5
    print(circulito)
    circulito.area = 36
    print(circulito)

    c1 = Circulo(Punto(1, 1), 1)
    print(c1)


if __name__ == "__main__":
    main()
