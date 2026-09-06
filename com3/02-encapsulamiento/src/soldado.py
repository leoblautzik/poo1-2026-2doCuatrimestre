# soldado.py

from __future__ import annotations


class Soldado:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.energia = 100
        self.salud = 200

    def atacar(self, otro: Soldado) -> None:
        """Un soldado ataca a otro si tiene energía suficiente."""

    def recibir_racion(self) -> None:
        """El soldado recupera energía al recibir una ración de agua."""

    def esta_derrotado(self) -> bool:
        """Devuelve True si la salud del soldado llegó a 0 o menos."""
        return False

    def estado(self) -> str:
        """Devuelve un string con el nombre, la salud y la energía.
        Por ejemplo: Nombre: Rambo, Salud: 100, Energía: 50
        """
        return ""


def main():
    pass


if __name__ == "__main__":
    main()
