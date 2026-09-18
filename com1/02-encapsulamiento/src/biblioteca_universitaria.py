"""

# Biblioteca Universitaria

## Descripción
Imagina que estás desarrollando un sistema para administrar los préstamos de una biblioteca universitaria.
La biblioteca cuenta con una colección de libros. Cada libro tiene un título, un autor, un ISBN y una cantidad limitada de ejemplares disponibles.
Los estudiantes pueden solicitar libros en préstamo, pero cada estudiante puede tener como máximo **3 libros prestados simultáneamente**.
El sistema debe permitir registrar préstamos, devoluciones y consultar qué libros se encuentran prestados.

## Clases y responsabilidades

### Libro
Cada libro debe mantener la siguiente información:
* Título.
* Autor.
* ISBN.
* Cantidad de ejemplares disponibles.
* Cantidad de ejemplares prestados.
Debe implementar, como mínimo, los siguientes métodos:
* `prestar()`: registra el préstamo de un ejemplar.
* `devolver()`: registra la devolución de un ejemplar.
* `hay_disponibles()`: indica si hay ejemplares disponibles.

### Estudiante
Cada estudiante tiene un nombre y puede mantener un registro de sus libros prestados, incluyendo las fechas de devolución previstas.
Debe implementar, como mínimo, los siguientes métodos:
* `pedir_prestado(libro, fecha_devolucion)`: solicita un libro en préstamo.
* `devolver(libro)`: devuelve un libro que tiene prestado.
Un estudiante no puede tener más de 3 libros prestados simultáneamente.

### Biblioteca
La biblioteca mantiene una colección de libros y un registro de los préstamos realizados.
Debe implementar, como mínimo, los siguientes métodos:
* `prestar(estudiante, libro, fecha_devolucion)`: registra un préstamo, validando que el libro pertenezca a la biblioteca y que haya ejemplares disponibles.
* `devolver(estudiante, libro)`: registra la devolución de un libro prestado.
* `listar_prestamos()`: muestra los préstamos activos, indicando el estudiante, el libro y la fecha de devolución prevista.

## Requisitos
### Encapsulamiento
Los atributos de las clases deben estar protegidos o privados.
El acceso o modificación de estos atributos debe hacerse mediante métodos públicos controlados, como getters, setters o métodos específicos.

### Composición y delegación
La clase `Biblioteca` debe contener una colección de objetos `Libro`.
La clase `Estudiante` debe mantener su propio registro de libros prestados.
Las operaciones deben distribuirse entre los objetos según sus responsabilidades. Por ejemplo, `Biblioteca` puede delegar en `Estudiante`, y `Estudiante` puede delegar en `Libro`.
No se debe implementar toda la lógica del sistema en una única clase.

### Restricciones y validaciones
* No se puede prestar un libro que no pertenezca a la biblioteca.
* No se puede prestar un libro que no tenga ejemplares disponibles.
* Un estudiante no puede superar el límite de 3 préstamos simultáneos.
* No se puede devolver un libro que el estudiante no tenga prestado.
* Al devolver un libro, debe actualizarse correctamente la cantidad de ejemplares disponibles.
* Los registros de préstamos deben mantenerse consistentes.

### Desafío extra
Permitir consultar rápidamente qué libros están prestados actualmente y a qué estudiante.

## Consideraciones
El programa debe estar implementado en Python utilizando programación orientada a objetos.
Se deben utilizar las clases indicadas y respetar sus responsabilidades.
Se espera que el programa permita demostrar el uso de encapsulamiento, composición y delegación.
No es necesario implementar una interfaz gráfica ni persistencia de datos.
"""


class Libro:
    """
    Cada Libro tiene título, autor, ISBN y un número limitado de ejemplares disponibles.
    Atributos: titulo, autor, isbn, eje_disp, eje_pestados
    metodos: prestar(), devolver(), hay_disponibles()
    """

    def __init__(self, titulo, autor, isbn, ejemplares_disponibles) -> None:
        if ejemplares_disponibles < 0:
            raise ValueError("La cantidad de ejemplares no puede ser negativa")
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn
        self.__ejemplares_disponibles = ejemplares_disponibles
        self.__ejemplares_prestados = 0

    @property
    def titulo(self):
        return self.__titulo

    @property
    def autor(self):
        return self.__autor

    @property
    def ejemplares_disponibles(self):
        return self.__ejemplares_disponibles

    @property
    def ejemplares_prestados(self):
        return self.__ejemplares_prestados

    def hay_disponibles(self) -> bool:
        return self.__ejemplares_disponibles > 0

    def prestar(self):
        if not self.hay_disponibles():
            raise RuntimeError("No quedan ejemplares disponibles")
        self.__ejemplares_disponibles -= 1
        self.__ejemplares_prestados += 1

    def devolver(self):
        if self.__ejemplares_prestados == 0:
            raise RuntimeError("No se han prestado ejemplares de ese libro")
        self.__ejemplares_disponibles += 1
        self.__ejemplares_prestados -= 1

    def __repr__(self) -> str:
        return f"{self.__titulo}, {self.__autor}, {self.__isbn}, EjemDisponibles: {self.__ejemplares_disponibles}, EjemPrestados: {self.__ejemplares_prestados}"


class Estudiante:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__prestamos: list[tuple[Libro, str]] = []

    @property
    def nombre(self) -> str:
        return self.__nombre

    def pedir_prestado(self, libro, fecha_devolucion):
        if len(self.__prestamos) >= 3:
            raise RuntimeError("El estudiante ya tiene tres préstamos")

        libro.prestar()

        self.__prestamos.append((libro, fecha_devolucion))

    def devolver(self, libro):

        if len(self.__prestamos) == 0:
            raise RuntimeError("No hay prestamos")

        # lista_b = [b for a, b in lista]

        libros = [libro for libro, _ in self.__prestamos]

        if libro not in libros:
            raise RuntimeError("El estudiante no tiene ese libro")

        for prestamo in self.__prestamos:
            if prestamo[0] == libro:
                libro.devolver()
                self.__prestamos.remove(prestamo)

    def __repr__(self) -> str:
        s = f"Estudiante: {self.nombre}, \n"
        s = s + f"Libros prestados: {self.__prestamos}"
        return s


class Biblioteca:
    def __init__(self, libros: list[Libro]) -> None:
        self.__libros: list[Libro] = libros
        self.__prestamos: list[tuple[Estudiante, Libro, str]] = []

    def prestar(
        self, estudiante: Estudiante, libro_solicitado: Libro, fecha_devolucion: str
    ):
        if not libro_solicitado in self.__libros:
            raise RuntimeError("El libro no se encuentra en la biblioteca")

        pos = self.__libros.index(libro_solicitado)
        libro = self.__libros[pos]

        estudiante.pedir_prestado(libro, fecha_devolucion)

        self.__prestamos.append((estudiante, libro, fecha_devolucion))

    def devolver(self, estudiante: Estudiante, libro_devuelto: Libro):
        estudiante_libro = [
            (estudiante, libro) for estudiante, libro, _ in self.__prestamos
        ]
        if (estudiante, libro_devuelto) not in estudiante_libro:
            raise RuntimeError("Devolución inconsistente")

        libro = self.__libros[self.__libros.index(libro_devuelto)]

        estudiante.devolver(libro)
        for p in self.__prestamos:
            if p[0] == estudiante and p[1] == libro_devuelto:
                self.__prestamos.remove(p)

    def listar_prestamos(self):
        for p in self.__prestamos:
            print(p[0].nombre, p[1].titulo, p[2])


def main():

    libro1 = Libro("Titulo1", "Autor1", "84xB", 5)
    libro2 = Libro("Titulo2", "Autor2", "99xZ", 5)
    libro3 = Libro("Titulo3", "Autor3", "99xZ", 6)
    libro4 = Libro("Titulo4", "Autor4", "99xZ", 2)

    el_ateneo = Biblioteca([libro1, libro2, libro3, libro4])

    aquiles = Estudiante("Aquiles")

    el_ateneo.prestar(aquiles, libro1, "mañana")
    el_ateneo.prestar(aquiles, libro2, "30-09-26")
    el_ateneo.prestar(aquiles, libro3, "30-09-26")
    # el_ateneo.prestar(aquiles, libro4, "30-09-26")
    el_ateneo.listar_prestamos()


if __name__ == "__main__":
    main()
