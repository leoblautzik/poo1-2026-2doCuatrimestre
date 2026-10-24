import csv


class Alumno:
    def __init__(self, nombre: str, materias: list[str]) -> None:
        self.nombre = nombre
        self.materias = materias

    def __repr__(self) -> str:
        return f"{self.nombre}, {self.materias}"


class Universidad:
    def __init__(self) -> None:
        self.alumnos: list[Alumno] = []
        self.materias: dict[str, list[str]] = {}

    def cargar_alumnos(self, archivo) -> None:
        with open(archivo, "r", encoding="utf-8") as f:
            lector = csv.reader(f)
            for datos in lector:
                # nombre = datos[0]
                # materias = datos[1:]
                # alumno = Alumno(nombre, materias)
                # self.alumnos.append(alumno)
                self.alumnos.append(Alumno(datos[0], datos[1:]))

    def generar_dict_materias(self) -> None:

        for alumno in self.alumnos:
            for materia in alumno.materias:
                l_alumnos = self.materias.get(materia, [])
                l_alumnos.append(alumno.nombre)
                self.materias[materia] = l_alumnos

    def materias_dictadas(self) -> list[str]:
        """Devuelve una lista con las materias que se dictan en
        la universidad, es decir, aquellas que cursa al menos un alumno.
        Cada materia aparece una sola vez, sin repeticiones.
        La lista debe estar ordenada alfabéticamente.
        """
        return sorted(self.materias.keys())

    def inscriptos_en_una_materia(self, materia) -> list[str]:
        """Recibe el nombre de una materia y devuelve la
        lista de alumnos inscriptos en ella, en el orden
        en que aparecen en el archivo. Si la materia no existe
        o no tiene inscriptos, devuelve una lista vacía."""

        return self.materias.get(materia, [])

    def cursan_mas_de_n_materias(self, n) -> list[str]:
        """Recibe un entero n y devuelve la lista de alumnos
        que cursan estrictamente más de n materias.
        Si ninguno cumple la condición, devuelve una lista vacía.
        """
        lista_alumnos = []
        for alumno in self.alumnos:
            if len(alumno.materias) > n:
                lista_alumnos.append(alumno.nombre)

        return lista_alumnos

    def alumnos_con_mayor_carga(self) -> list[str]:
        """Devuelve la lista de los alumnos que cursan la mayor
        cantidad de materias.
        Si hay empate, la lista incluye a todos los que empatan."""

        alumnos_tragas = []
        max_cant_materias = max(len(alumno.materias) for alumno in self.alumnos)

        for alumno in self.alumnos:
            if len(alumno.materias) == max_cant_materias:
                alumnos_tragas.append(alumno.nombre)

        return alumnos_tragas

    # def materia_con_mas_alumnos(self)->list[str]:

    def cantidad_de_alumnos_por_materia(self) -> list[tuple[str, int]]:
        """Devuelve, para cada materia dictada, cuántos
        alumnos la cursan, ordenado de mayor a menor cantidad.
        """
        lista_materia_cantidad = []

        for materia, lista_alumnos in self.materias.items():
            lista_materia_cantidad.append((materia, len(lista_alumnos)))

        return sorted(lista_materia_cantidad, key=lambda t: t[1], reverse=True)

    def alumnos_que_comparten_materia(self, m1, m2) -> list[str]:
        """Recibe dos materias y devuelve la lista de alumnos
        que cursan ambas."""
        lam1ym2 = []

        lam1 = self.materias.get(m1, [])
        lam2 = self.materias.get(m2, [])

        for alumno in lam1:
            if alumno in lam2:
                lam1ym2.append(alumno)

        return lam1ym2

    def listado_por_materia(self, archivo):
        """Genera un archivo/listado en el que cada elemento asocia
        una materia con la lista de los nombres de sus alumnos.
        Las materias deben aparecer en orden alfabético y
        los alumnos de cada materia en el orden del archivo."""

        lista_materias_ordenadas = self.materias_dictadas()

        with open(archivo, "w", encoding="utf-8") as w:
            for materia in lista_materias_ordenadas:
                w.write(materia + "\n")
                w.write(str(self.materias.get(materia)) + "\n")


def main():
    uno = Universidad()
    while True:
        archivo = input("Ingrese la ruta del archivo de datos: ")
        try:
            uno.cargar_alumnos(archivo)
            uno.generar_dict_materias()
            break
        except FileNotFoundError:
            print("Archivo no encontrado, intenet de nuevo")

    # print(uno.alumnos)
    # print(uno.materias)
    # print(uno.materias_dictadas())
    # print(uno.inscriptos_en_una_materia("Gastromía"))
    # print(uno.alumnos_con_mayor_carga())
    # print(uno.cantidad_de_alumnos_por_materia())
    # uno.listado_por_materia("materias.txt")


if __name__ == "__main__":
    main()
