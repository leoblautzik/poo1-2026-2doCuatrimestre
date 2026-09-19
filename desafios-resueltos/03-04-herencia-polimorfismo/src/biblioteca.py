# -----------------------------
# Ejercicio: Sistema de Biblioteca Virtual
# -----------------------------

# Clase base
class Material:
    def __init__(self, titulo: str, autor: str, anio: int):
        # Atributos privados
        self.__titulo = titulo
        self.__autor = autor
        self.__anio = anio

    @property
    def titulo(self) -> str:
        return self.__titulo

    @property
    def autor(self) -> str:
        return self.__autor

    @property
    def anio(self) -> int:
        return self.__anio

    def __str__(self) -> str:
        # TODO: representación genérica de un material
        return f"{self.__class__.__name__}: Título: {self.titulo}, Autor: {self.autor}, Año: {self.anio}"

    def __repr__(self) -> str:
        return self.__str__()


# -----------------------------
# Subclases (Herencia)
# -----------------------------
class Libro(Material):
    def __init__(self, titulo: str, autor: str, anio: int, genero: str):
        super().__init__(titulo, autor, anio)
        self.__genero = genero

    def __str__(self) -> str:
        return f"{super().__str__()}, Género: {self.__genero}"


class Revista(Material):
    def __init__(self, titulo: str, autor: str, anio: int, numero_edicion: int):
        super().__init__(titulo, autor, anio)
        self.__numero_edicion = numero_edicion

    def __str__(self) -> str:
        return f"{super().__str__()}, Edición: {self.__numero_edicion}"


class DVD(Material):
    def __init__(self, titulo: str, autor: str, anio: int, duracion: int):
        super().__init__(titulo, autor, anio)
        self.__duracion = duracion

    def __str__(self) -> str:
        # TODO: devolver cadena representando un DVD
        return f"{super().__str__()}, Duración: {self.__duracion}"


# -----------------------------
# Clase Usuario (Composición)
# -----------------------------
class Usuario:
    def __init__(self, nombre: str):
        self.__nombre = nombre
        self.__materiales_prestados: list[Material] = []  # lista de objetos Material

    def prestar(self, material: Material):
        # Agregar material a la lista de prestados
        self.__materiales_prestados.append(material)

    def devolver(self, material: Material):
        # TODO: quitar material de la lista de prestados

        if not material in self.__materiales_prestados:
            raise ValueError("Ese material no se encuantra en la lista de prestados")

        self.__materiales_prestados.remove(material)

    def listar_materiales(self):
        s = f"Materiales prestados a {self.__nombre} \n"
        for m in self.__materiales_prestados:
            s = s + m.__str__() + "\n"
        print(s)
        # print(self.__materiales_prestados)


# -----------------------------
# Función polimórfica
# -----------------------------
def mostrar_informacion(material: Material) -> None:
    # TODO: imprimir el objeto (usará __str__ polimórfico)
    print(material)


def main():
    libro = Libro("1984", "George Orwell", 1949, "Ciencia ficción")

    revista = Revista("National Geographic", "Varios autores", 2025, 150)
    dvd = DVD("Matrix", "Wachowski", 1999, 136)

    ana = Usuario("Ana")
    pedro = Usuario("Pedro")

    ana.prestar(libro)
    ana.prestar(revista)

    pedro.prestar(dvd)

    print("=== MATERIALES DE ANA ===")
    ana.listar_materiales()

    print("\n=== MATERIALES DE PEDRO ===")
    pedro.listar_materiales()

    print("\n=== INFORMACIÓN DE TODOS LOS MATERIALES ===")

    mostrar_informacion(libro)
    mostrar_informacion(revista)
    mostrar_informacion(dvd)

    print("\n=== DEVOLUCIÓN ===")

    ana.devolver(revista)

    print("\nMateriales de Ana después de devolver la revista:")
    ana.listar_materiales()


if __name__ == "__main__":
    main()
