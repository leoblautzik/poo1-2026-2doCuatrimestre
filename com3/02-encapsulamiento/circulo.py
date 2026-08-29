import math


class Circulo:
    def __init__(self, radio) -> None:
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
        return math.pi * self.diametro

    @perimetro.setter
    def perimetro(self, nuevo_perimetro):
        self.radio = nuevo_perimetro / 2 / math.pi

    @property
    def area(self):
        return math.pi * pow(self.radio, 2)

    @area.setter
    def area(self, nueva_area):
        self.radio = math.sqrt(nueva_area / math.pi)

    def __str__(self) -> str:
        return f"Circulo: radio: {self.radio:.2f}, diametro: {self.diametro:.2f}, perimetro: {self.perimetro:.2f}, area: {self.area:.2f}"


def main():
    circulito = Circulo(4)
    print(circulito)
    circulito.radio = 5
    print(circulito)
    circulito.diametro = 16
    print(circulito)

    circulito.area = 32
    print(circulito)


if __name__ == "__main__":
    main()
