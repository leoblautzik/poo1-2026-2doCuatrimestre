"""
Dada la jerarquía que se aprecia en el diagrama UML,
considerando que solo la clase Profesional es abstracta y
las demás clases son concretas,. Todos los profesionales
tienen un honorario mensual básico de $5000000
(si se cambia el honorario básico cambia para toda la jerarquía de clases).
De todos los profesionales se guarda su nombre y apellido.
Médicos y Dentistas cobran honorarios básicos. Se pide:
Escribir los métodos que sean necesarios para calcular el honorario_mensual()
a partir del básico  considerando que los honorarios se incrementa un 25%
por cada nivel de especialización. Es decir, los honorarios de un un Cirujano son 25% ($ 1250000)
más alto que el de un médico, y los de un Cirujano Cardiovascular un 25% más alto que los de un Cirujano ($1562500)

"""

from abc import ABC


class Profesional(ABC):
    basico = 5000000.00

    def __init__(self, nombre, apellido) -> None:
        self.__nombre = nombre
        self.__apellido = apellido

    def honorario_mensual(self) -> float:
        return Profesional.basico

    def __str__(self) -> str:
        return f"{self.__nombre} {self.__apellido} : Honorarios: {self.honorario_mensual()}"


class Medico(Profesional):
    def honorario_mensual(self) -> float:
        return super().honorario_mensual()


class Dentista(Profesional):
    def honorario_mensual(self) -> float:
        return super().honorario_mensual()


class Cirujano(Medico):
    def honorario_mensual(self) -> float:
        return super().honorario_mensual() * 1.25


class CirujanoCardiovascular(Cirujano):
    def honorario_mensual(self) -> float:
        return super().honorario_mensual() * 1.25


class Endodoncista(Dentista):
    def honorario_mensual(self) -> float:
        return super().honorario_mensual() * 1.25


def main():
    medico = Medico("Alberto", "Alvarez")
    print(medico)

    endo = Endodoncista("Javier", "Pisano")
    print(endo)

    cardio = CirujanoCardiovascular("Aldo", "Marlo")
    print(cardio)


if __name__ == "__main__":
    main()
