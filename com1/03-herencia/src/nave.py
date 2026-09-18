"""Atributos:
nombre → identificador de la nave.
salud → puntos de vida de la nave.
danio → puntos de salud que provoca en su oponente cuando ataca

Métodos:
atacar(otra) → será redefinido en las subclases.
recibir_danio(atacante) → resta salud a la nave de acuerdo a quien la ataca
(no puede bajar de 0).
esta_destruida() → devuelve True si la salud llega a 0 o menos.
estado() → devuelve un string con nombre y salud actual.
"""

from __future__ import annotations


class Nave:
    def __init__(self, nombre, salud, danio) -> None:
        self.__nombre = nombre
        self.__salud = salud
        self.__danio = danio

    @property
    def salud(self):
        return self.__salud

    def atacar(self, otra: Nave) -> None:
        if not self.esta_destruida() and not otra.esta_destruida():
            otra.recibir_danio(self)

    def recibir_danio(self, otra: Nave) -> None:
        if not self.esta_destruida() and not otra.esta_destruida():
            self.__salud = max(self.salud - otra.__danio, 0)

    def esta_destruida(self) -> bool:
        return self.salud <= 0

    def estado(self) -> str:
        return f"Nave: {self.__nombre}, Salud: {self.salud}"

    def puede_atacar(self, otra: Nave) -> bool:
        return not self.esta_destruida() and not otra.esta_destruida()


class Caza(Nave):
    def __init__(self, nombre: str):
        super().__init__(nombre, salud=100, danio=15)

    def atacar(self, otra: Nave) -> None:
        if self.puede_atacar(otra):
            otra.recibir_danio(self)


class Bombardero(Nave):
    def __init__(self, nombre: str):
        super().__init__(nombre, salud=150, danio=25)
        self.__autodanio = 0

    def atacar(self, otra: Nave) -> None:
        """Inflige 25 de daño y recibe 5 de autodaño."""
        if self.puede_atacar(otra):
            otra.recibir_danio(self)
            self.__autodanio += 5

    @property
    def salud(self):
        return super().salud - self.__autodanio

    def esta_destruida(self) -> bool:
        return super().salud - self.__autodanio <= 0


class Crucero(Nave):
    def __init__(self, nombre: str):
        super().__init__(nombre, salud=300, danio=40)

    def puede_atacar(self, otra: Nave) -> bool:
        return super().puede_atacar(otra) and self.salud > 50

    def atacar(self, otra: Nave) -> None:
        """Inflige 40 de daño si la salud > 50, en caso contrario no ataca."""
        if self.puede_atacar(otra):
            otra.recibir_danio(self)


def main():
    pass


if __name__ == "__main__":
    main()
