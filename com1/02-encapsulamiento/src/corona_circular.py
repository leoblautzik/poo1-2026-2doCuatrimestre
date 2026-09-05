from circulo import Circulo


class CoronaCircular:
    def __init__(self, radio_interior, radio_exterior) -> None:
        self.__circulo_grande = Circulo(radio_exterior)
        self.__circulo_chico = Circulo(radio_interior)

    @property
    def radio_interior(self):
        return self.__circulo_chico.radio

    @radio_interior.setter
    def radio_interior(self, nuevo_radio):
        if nuevo_radio >= self.__circulo_grande.radio:
            raise ValueError("El radio interior debe ser menor que el exterior")
        self.__circulo_chico.radio = nuevo_radio

    @property
    def radio_exterior(self):
        return self.__circulo_grande.radio

    @radio_exterior.setter
    def radio_exterior(self, nuevo_radio):
        if nuevo_radio <= self.__circulo_chico.radio:
            raise ValueError("El radio exterior debe ser mayor que el interior")
        self.__circulo_grande.radio = nuevo_radio

    def perimetro(self):
        return self.__circulo_grande.perimetro + self.__circulo_chico.perimetro

    def perimetro_interior(self):
        return self.__circulo_chico.perimetro

    def perimetro_exterior(self):
        return self.__circulo_grande.perimetro

    def area(self):
        return self.__circulo_grande.area - self.__circulo_chico.area


def main():
    coronita = CoronaCircular(4, 6)
    print(coronita.area())
    coronita.radio_interior = 2
    print(coronita.area())


if __name__ == "__main__":
    main()
