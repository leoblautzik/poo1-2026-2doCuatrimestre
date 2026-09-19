# soldado.py

from __future__ import annotations


class Soldado:
    """
    Queremos simular enfrentamientos entre soldados.
    Para ello, vas a modelar una clase llamada Soldado
    con las siguientes características o Atributos:
    nombre: un identificador para cada soldado.
    energia: comienza en 100.
    salud: comienza en 200.
    """

    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self.__energia = 100
        self.__salud = 200

    @property
    def energia(self) -> int:
        return self.__energia

    @property
    def salud(self) -> int:
        return self.__salud

    def atacar(self, otro: Soldado) -> None:
        """Un soldado ataca a otro si tiene energía suficiente."""
        if (
            self.energia >= 10
            and not self.esta_derrotado()
            and not otro.esta_derrotado()
        ):
            self.__energia -= 10
            otro.__salud -= 10

    def recibir_racion(self) -> None:
        """El soldado recupera 20 de energía al recibir una ración de agua.
        El tope de su energía es 100.
        Un soldado derrotado no puede recibir la racion.
        """
        if not self.esta_derrotado():
            self.__energia = min(self.__energia + 20, 100)

    def esta_derrotado(self) -> bool:
        """Devuelve True si la salud del soldado llegó a 0 o menos."""
        return self.__salud <= 0

    def estado(self) -> str:
        """Devuelve un string con el nombre, la salud y la energía.
        Por ejemplo: Nombre: Rambo, Salud: 100, Energía: 50
        """
        return (
            f"Nombre: {self.nombre}, Salud: {self.__salud}, Energía: {self.__energia}"
        )


def main():
    rambo = Soldado("Rambo")
    conan = Soldado("Conan")
    for _ in range(20):  # 20 ataques de 10 de daño = 200
        rambo.atacar(conan)
    print(rambo.estado())
    print(conan.estado())


if __name__ == "__main__":
    main()
