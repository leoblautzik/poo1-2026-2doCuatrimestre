class Vecino:
    def __init__(self, nombre, edad, localidad) -> None:
        self.nombre: str = nombre
        self.edad: int = edad
        self.localidad: str = localidad

    def __repr__(self) -> str:
        return f"{self.nombre}, {self.edad},{self.localidad}"


class GestionVecinos:
    def __init__(self) -> None:
        self.vecinos: list[Vecino] = []

    def leer_vecinos(self, archivo):
        with open(archivo, "r") as veci:
            for cada_linea in veci:
                datos = cada_linea.strip().split(",")
                vecino = Vecino(datos[0], int(datos[1]), datos[2])
                self.vecinos.append(vecino)

    def mostrar_vecinos(self):
        for cada_vecino in self.vecinos:
            print(cada_vecino)


def main():
    gv = GestionVecinos()
    gv.leer_vecinos("personas_buenos_aires.csv")
    gv.mostrar_vecinos()


if __name__ == "__main__":
    main()
