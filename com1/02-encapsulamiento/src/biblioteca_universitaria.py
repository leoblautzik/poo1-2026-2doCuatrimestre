class Libro:
    """
    Cada Libro tiene título, autor, ISBN y un número limitado de ejemplares disponibles.
    Atributos: titulo, autor, isbn, eje_disp, eje_pestados
    metodos: prestar(), devolver(), hay_disponibles()
    """

    def __init__(self, titulo, autor, isbn, ejemplares_disponibles) -> None:
        self.titulo = titulo
        self.__autor = autor
        self.__isbn = isbn
        self.__ejemplares_disponibles = ejemplares_disponibles
        self.__ejemplares_prestados = 0

    def hay_disponibles(self) -> bool:
        return self.__ejemplares_disponibles > 0

    def prestar(self):
        if self.hay_disponibles():
            self.__ejemplares_disponibles -= 1
            self.__ejemplares_prestados += 1

    def devolver(self):
        self.__ejemplares_disponibles += 1
        self.__ejemplares_prestados -= 1

    def __repr__(self) -> str:
        return f"{self.titulo}, {self.__autor}, {self.__isbn}, EjemDisponibles: {self.__ejemplares_disponibles}, EjemPrestados: {self.__ejemplares_prestados}"


class Estudiante:
    def __init__(self):
        self.__cuenta_prestamo = CuentaPrestamo()

    def pedir_prestado(self, libro, fecha_devolucion):
        self.__cuenta_prestamo.pedir_prestado(libro, fecha_devolucion)

    def devolver(self, libro):
        self.__cuenta_prestamo.devolver(libro)

    def __repr__(self) -> str:
        return f"{self.__cuenta_prestamo.__repr__()}"


class CuentaPrestamo:
    """La CuentaDePrestamo es responsable de manejar la lógica
    de cuántos libros tiene un estudiante y si puede tomar más.
    Los préstamos deben gestionarse a través de una clase CuentaDePrestamo,
    que lleva un registro interno de los libros prestados y fechas de devolución.
    """

    def __init__(self) -> None:
        self.__prestamos: list[tuple[Libro, str]] = []

    def pedir_prestado(self, libro, fecha_devolucion):
        if len(self.__prestamos) >= 3:
            raise RuntimeError("Ya no puede pedir mas libros")
        self.__prestamos.append((libro, fecha_devolucion))

    def devolver(self, libro):
        self.__prestamos.remove(libro)

    def __repr__(self) -> str:
        s = ""
        for e in self.__prestamos:
            s += e[0].titulo
            s += "\n"
        return s


class Biblioteca:
    def __init__(self, libros: list[Libro]) -> None:
        self.__libros: list[Libro] = libros
        self.__prestamos: list[tuple[Estudiante, Libro]] = []

    def prestar(
        self, estudiante: Estudiante, libro_solicitado: Libro, fecha_devolucion: str
    ):
        if not libro_solicitado in self.__libros:
            raise RuntimeError("El libro no se encuentra en la biblioteca")

        pos = self.__libros.index(libro_solicitado)
        libro = self.__libros[pos]

        if not libro.hay_disponibles():
            print("No hay ejemplares disponibles")
        else:
            estudiante.pedir_prestado(libro, fecha_devolucion)
            libro.prestar()
            self.__prestamos.append((estudiante, libro))

    def devolver(self, estudiante: Estudiante, libro_devuelto: Libro):
        libro = self.__libros[self.__libros.index(libro_devuelto)]
        libro.devolver()
        estudiante.devolver(libro)
        self.__prestamos.remove((estudiante, libro))

    def listar_prestamos(self):
        for p in self.__prestamos:
            print(p)


def main():

    libro1 = Libro("Titulo1", "Autor1", "84xB", 5)
    libro2 = Libro("Titulo2", "Autor2", "99xZ", 5)
    libro3 = Libro("Titulo3", "Autor3", "99xZ", 6)
    libro4 = Libro("Titulo4", "Autor4", "99xZ", 2)

    el_ateneo = Biblioteca([libro1, libro2, libro3, libro4])

    aquiles = Estudiante()

    el_ateneo.prestar(aquiles, libro1, "mañana")
    el_ateneo.prestar(aquiles, libro2, "30-09-26")
    el_ateneo.prestar(aquiles, libro3, "30-09-26")
    # el_ateneo.prestar(aquiles, libro4, "30-09-26")
    el_ateneo.listar_prestamos()


if __name__ == "__main__":
    main()
