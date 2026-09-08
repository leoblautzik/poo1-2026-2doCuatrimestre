class Guerrero:
    def __init__(
        self,
        nombre: str,
        energia: int,
        salud: int,
        costo_ataque: int,
        danio: int,
        energia_max: int,
    ):
        self.nombre = nombre
        self.energia = energia
        self.salud = salud
        self.costo_ataque = costo_ataque
        self.danio = danio
        self.energia_max = energia_max

    def atacar(self, otro_guerrero: "Guerrero") -> None:
        """Ataca a otro guerrero si tiene suficiente energía
        y no está derrotado."""
        if (
            self.energia >= self.costo_ataque
            and not self.esta_derrotado()
            and not otro_guerrero.esta_derrotado()
        ):
            self.energia -= self.costo_ataque
            otro_guerrero.salud -= self.danio

    def recibir_racion(self) -> None:
        """Recupera energía al recibir una ración de agua."""

    def esta_derrotado(self) -> bool:
        """Devuelve True si la salud llegó a 0 o menos."""
        return self.salud <= 0

    def estado(self) -> str:
        """Devuelve un string con nombre, salud y energía."""
        return f"Nombre: {self.nombre}, Salud: {self.salud}, Energía: {self.energia}"


class Soldado(Guerrero):
    def __init__(self, nombre: str):
        super().__init__(
            nombre, energia=100, salud=200, costo_ataque=10, danio=10, energia_max=100
        )

    def recibir_racion(self) -> None:
        self.energia = min(self.energia + 20, self.energia_max)


class Orco(Guerrero):
    def __init__(self, nombre: str):
        super().__init__(
            nombre, energia=120, salud=250, costo_ataque=15, danio=20, energia_max=120
        )

    def recibir_racion(self) -> None:
        self.energia = min(self.energia * 1.5, self.energia_max)


class Elfo(Guerrero):
    def __init__(self, nombre: str):
        super().__init__(
            nombre, energia=80, salud=150, costo_ataque=5, danio=15, energia_max=80
        )

    def recibir_racion(self) -> None:
        self.energia = self.energia_max


def main():
    julian = Guerrero("Julian")
    s = Soldado("Ares")
    o = Orco("Grom")
    legolas = Elfo("Legolas")

    s.atacar(o)  # Ares ataca a Grom
    o.atacar(s)  # Grom responde
    legolas.recibir_racion()
    o.atacar(legolas)
    o.atacar(legolas)
    o.atacar(legolas)
    guerreros: list[Guerrero] = [s, o, legolas]

    for cada_uno in guerreros:
        print(cada_uno.estado())

    for cada_uno in guerreros:
        cada_uno.recibir_racion()

    for cada_uno in guerreros:
        print(cada_uno.estado())


if __name__ == "__main__":
    main()
