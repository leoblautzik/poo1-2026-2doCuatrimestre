from abc import ABC, abstractmethod


class Estudiante(ABC):
    __cuota_base = 100000.00

    @classmethod
    def set_cuota_base(cls, nueva_cuota):
        Estudiante.__cuota_base = nueva_cuota

    @classmethod
    def get_cuota_base(cls):
        return Estudiante.__cuota_base

    def __init__(self, legajo, materias):
        self.__legajo = legajo
        self.__materias = materias

    @property
    def materias(self):
        return self.__materias

    @abstractmethod
    def get_cuota_mensual(slef) -> float:
        pass

    def __repr__(self) -> str:
        return f"Legajo: {self.__legajo}, materias: {self.materias}, Cuota: {self.get_cuota_mensual():.2f}"

    def __eq__(self, otro):
        return self.__legajo == otro.__legajo

    def __lt__(self, otro):
        return self.__legajo < otro.__legajo


class Abogado(Estudiante):
    def get_cuota_mensual(self) -> float:
        return Estudiante.get_cuota_base() * (1 + self.materias * 0.05)


class Arquitecto(Estudiante):
    def get_cuota_mensual(self) -> float:
        return Estudiante.get_cuota_base() * (1 + self.materias * 0.1)


class Universidad:
    Estudiante.set_cuota_base(120000)

    def __init__(self) -> None:
        self.__estudiantes: list[Estudiante] = []

    def agregar_estudiante(self, e):
        self.__estudiantes.append(e)

    def get_total_mensual_cuotas(self) -> float:
        total_cuotas = 0.0
        for e in self.__estudiantes:
            total_cuotas += e.get_cuota_mensual()

        return total_cuotas

    def listar_planilla_de_estudiantes(self):
        self.__estudiantes.sort()
        for e in self.__estudiantes:
            print(e)


def main():
    # ==========================================
    # Establecemos la cuota base
    # ==========================================
    Estudiante.set_cuota_base(100000)

    universidad = Universidad()

    # ==========================================
    # Creamos estudiantes
    # ==========================================

    a1 = Arquitecto(1050, 3)
    a2 = Arquitecto(1020, 5)
    a3 = Arquitecto(1080, 1)

    ab1 = Abogado(1010, 4)
    ab2 = Abogado(1070, 2)
    ab3 = Abogado(1030, 5)

    # ==========================================
    # Agregamos los estudiantes
    # ==========================================

    universidad.agregar_estudiante(a1)
    universidad.agregar_estudiante(a2)
    universidad.agregar_estudiante(a3)

    universidad.agregar_estudiante(ab1)
    universidad.agregar_estudiante(ab2)
    universidad.agregar_estudiante(ab3)

    # ==========================================
    # Probamos el cálculo individual
    # ==========================================

    print("=== CUOTAS INDIVIDUALES ===")

    print(f"Arquitecto 1050: ${a1.get_cuota_mensual():.2f}")
    print(f"Arquitecto 1020: ${a2.get_cuota_mensual():.2f}")
    print(f"Arquitecto 1080: ${a3.get_cuota_mensual():.2f}")

    print(f"Abogado 1010: ${ab1.get_cuota_mensual():.2f}")
    print(f"Abogado 1070: ${ab2.get_cuota_mensual():.2f}")
    print(f"Abogado 1030: ${ab3.get_cuota_mensual():.2f}")

    # ==========================================
    # Probamos el total de la universidad
    # ==========================================

    print("\n=== TOTAL RECAUDADO ===")

    total = universidad.get_total_mensual_cuotas()

    print(f"Total mensual: ${total:.2f}")

    # ==========================================
    # Probamos el listado ordenado
    # ==========================================

    print("\n=== PLANILLA DE ESTUDIANTES ===")

    universidad.listar_planilla_de_estudiantes()

    # ==========================================
    # Cambiamos la cuota base
    # ==========================================

    print("\n=== CAMBIO DE CUOTA BASE ===")

    Estudiante.set_cuota_base(120000)

    print(f"Nueva cuota base: {Estudiante.get_cuota_base():.2f}")
    # Comprobamosquecambiaparatodosprint(f"CuotaArquitecto1050:"f"{a1.get_cuota_mensual():.2f}"

    print(f"Cuota Abogado 1010: {ab1.get_cuota_mensual():.2f}")

    print(f"Nuevototalmensual:{universidad.get_total_mensual_cuotas():.2f}")

    # ==========================================
    # Volvemos a mostrar la planilla
    # ==========================================

    print("\n=== PLANILLA CON NUEVA CUOTA ===")

    universidad.listar_planilla_de_estudiantes()


if __name__ == "__main__":
    main()
