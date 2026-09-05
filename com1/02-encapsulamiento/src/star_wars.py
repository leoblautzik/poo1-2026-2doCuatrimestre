class Nave:
    def __init__(self, modelo, autonomia):
        self.modelo = modelo
        self.autonomia = autonomia

    def __str__(self):
        return f"Nave {self.modelo} (autonomia: {self.autonomia})"


class Escuadron:
    def __init__(self, nombre):
        self.nombre = nombre
        self.naves = []

    def agregar_nave(self, nave):
        if nave in self.naves:
            raise RuntimeError(
                "No se puede agregar dos veces la misma nave al escuadrón"
            )
        self.naves.append(nave)

    def naves_con_autonomia(self, distancia) -> list[Nave]:
        autonomas = []
        for n in self.naves:
            if n.autonomia >= distancia * 2:
                autonomas.append(n)
        return autonomas

    def __str__(self):
        naves_str = "\n".join(str(nave) for nave in self.naves)
        return f"Escuadron {self.nombre}:\n{naves_str}"


if __name__ == "__main__":
    nave = Nave("X-Wing", 120)
    alfa = nave
    escuadron = Escuadron("Rogue")

    escuadron.agregar_nave(nave)
    escuadron.agregar_nave(Nave("Y-Wing", 80))
    escuadron.agregar_nave(Nave("Y-Wing", 80))
    escuadron.agregar_nave(Nave("A-Wing", 60))
    escuadron.agregar_nave(alfa)  # duplicado, debe rechazarse

    print("--- Naves en el escuadrón ---")
    for n in escuadron.naves:
        print(n)

    print("--- Con autonomia >= 90 ---")
    for n in escuadron.naves_con_autonomia(40):
        print(n)
