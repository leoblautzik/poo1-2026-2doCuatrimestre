class Profesional:
    basico = 5000000.00

    def __init__(self, nombre, apellido) -> None:
        self.__nombre = nombre
        self.__apellido = apellido

    def honorario_mensual(self) -> float:
        return Profesional.basico

    def __str__(self) -> str:
        return f"{self.__nombre} {self.__apellido}"


class Medico:
    def __init__(self, nombre, apellido):
        self.__profesional = Profesional(nombre, apellido)

    def honorario_mensual(self) -> float:
        return self.__profesional.honorario_mensual()

    def __str__(self) -> str:
        return f"{self.__profesional.__str__()}"


class Dentista(Profesional):
    def honorario_mensual(self) -> float:
        return super().honorario_mensual()


class Cirujano:
    def __init__(self, nombre, apellido):
        self.__medico = Medico(nombre, apellido)

    def honorario_mensual(self) -> float:
        return self.__medico.honorario_mensual() * 1.25

    def __str__(self) -> str:
        return f"{self.__medico.__str__()}"


class CirujanoCardiovascular:
    def __init__(self, nombre, apellido):
        self.__cirujano = Cirujano(nombre, apellido)

    def honorario_mensual(self) -> float:
        return self.__cirujano.honorario_mensual() * 1.25

    def __str__(self) -> str:
        return f"{self.__cirujano.__str__()}"


class Endodoncista(Dentista):
    def honorario_mensual(self) -> float:
        return super().honorario_mensual() * 1.25


def main():
    medico = Medico("Carlos", "Cureta")
    print(medico, medico.honorario_mensual())
    ciruja = Cirujano("Angel", "Carnicer")
    print(ciruja, ciruja.honorario_mensual())
    cardio = CirujanoCardiovascular("Corazon", "Partido")
    print(cardio, cardio.honorario_mensual())


if __name__ == "__main__":
    main()
