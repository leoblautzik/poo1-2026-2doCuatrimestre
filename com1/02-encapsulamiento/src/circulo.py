import math


class Circulo:
    def __init__(self, radio):
        self.radio = radio

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

    def __str__(self):
        s = "Soy un círculo felíz\n"
        s += f"radio: {self.__radio}\n"
        s += f"diametro: {self.diametro}\n"
        s += f"perimetro: {self.perimetro}\n"
        s += f"area: {self.area}"
        return s


def main():
    circulito = Circulo(4)
    print(circulito)
    circulito.radio = 5
    print(circulito)
    circulito.area = 36
    print(circulito)

    c1 = Circulo(1)
    print(c1)


if __name__ == "__main__":
    main()
