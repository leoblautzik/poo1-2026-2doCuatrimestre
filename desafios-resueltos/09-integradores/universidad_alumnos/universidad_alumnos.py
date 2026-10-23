class Alumno:
    def __init__(self, nombre: str, materias: list[str]) -> None:
        self.nombre: str = nombre
        self.materias: list[str] = materias

    def __repr__(self) -> str:
        return f"{self.nombre}, {self.materias}"


class Universidad:
    def __init__(self) -> None:
        self.alumnos: list[Alumno] = []

    def cargar_alumnos(self, archivo_alumnos):
        with open(archivo_alumnos, "r") as aa:
            for linea in aa:
                datos = linea.strip().split(",")
                self.alumnos.append(Alumno(datos[0], datos[1:]))

    def materias_dictadas(self) -> list[str]:
        cm: set[str] = set()

        for a in self.alumnos:
            for m in a.materias:
                cm.add(m)

        lista_m = list(cm)
        lista_m.sort()

        return lista_m

    def alumnos_por_materia(self) -> dict[str, list[str]]:
        aux: dict[str, list[str]] = {}

        for alumno in self.alumnos:
            for materia in alumno.materias:
                lista_alumnos = aux.get(materia, [])
                lista_alumnos.append(alumno.nombre)
                aux[materia] = lista_alumnos

        return aux

    def inscriptos_en_una_materia(self, materia):
        dic_aux = self.alumnos_por_materia()
        if materia not in dic_aux:
            return []
        return dic_aux[materia]

    def alumnos_mas_de_n_materias(self, n):
        la = []

        for a in self.alumnos:
            if len(a.materias) > n:
                la.append(a.nombre)

        return la

    def alumnos_mas_carga(self):
        # alumnos = []

        max_cm = max(len(alumno.materias) for alumno in self.alumnos)

        # for a in self.alumnos:
        #     if len(a.materias) == max_cm:
        #         alumnos.append(a.nombre)

        return self.alumnos_mas_de_n_materias(max_cm - 1)

    def materia_mas_alumnos(self):
        lista_m = []

        dic_aux = self.alumnos_por_materia()

        max_ca = max(len(a) for _, a in dic_aux.items())

        for m, a in dic_aux.items():
            if len(a) == max_ca:
                lista_m.append(m)

        return lista_m

    def materia_menos_alumnos(self):
        lista_m = []

        dic_aux = self.alumnos_por_materia()

        max_ca = min(len(a) for _, a in dic_aux.items())

        for m, a in dic_aux.items():
            if len(a) == max_ca:
                lista_m.append(m)

        return lista_m

    def cantidad_de_alumnos_por_materia(self):
        """Devuelve, para cada materia dictada,
        cuántos alumnos la cursan, ordenado de mayor a menor cantidad.
        Ante igualdad de cantidad, se ordena alfabéticamente por materia.
        """

        dic_m_al = self.alumnos_por_materia()
        m_ca: list[tuple[str, int]] = []

        for m, al in dic_m_al.items():
            m_ca.append((m, len(al)))

        ordenados = sorted(m_ca, key=lambda t: t[1], reverse=True)
        return ordenados

    def alumnos_comparten_materia(self, m1, m2):
        """Recibe dos materias y devuelve la lista de alumnos que cursan ambas."""
        l = []
        dic_m_al = self.alumnos_por_materia()
        al_m1 = dic_m_al[m1]
        al_m2 = dic_m_al[m2]

        for a in al_m1:
            if a in al_m2:
                l.append(a)

        return l

    def listado_materias_alumnos(self):
        dic_m_al: dict[str, list[str]] = self.alumnos_por_materia()
        materias = list(dic_m_al.keys())
        materias.sort()
        with open("materias.txt", "w") as f:
            for m in materias:
                f.write(m + "\n")
                f.write(str(dic_m_al[m]) + "\n")


def main():
    uno = Universidad()
    uno.cargar_alumnos("alumnos_materias.txt")
    # print(uno.alumnos)
    # print(uno.materias_dictadas())
    # print(uno.inscriptos_en_una_materia("Resistencia de materiales"))
    # print(uno.alumnos_mas_carga())
    # print(uno.materia_mas_alumnos())
    # print(uno.materia_menos_alumnos())
    # print(uno.cantidad_de_alumnos_por_materia())
    # print(uno.alumnos_comparten_materia("Matematica", "Quimica"))
    uno.listado_materias_alumnos()


if __name__ == "__main__":
    main()
