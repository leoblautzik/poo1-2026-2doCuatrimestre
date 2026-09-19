class Empleado:
    def __init__(self, nombre, salario_base):
        self.__nombre = nombre
        self.__salario_base = salario_base

    @property
    def salario_base(self):
        return self.__salario_base

    def calcular_bonificacion(self):
        return self.__salario_base * 0.05

    def calcular_salario(self):
        return self.__salario_base + self.calcular_bonificacion()

    def __str__(self):
        return f"Nombre: {self.__nombre}, Salario:{self.calcular_salario()}"


class Gerente(Empleado):
    def calcular_bonificacion(self):
        return super().salario_base * 0.1


class Desarrollador(Empleado):
    def calcular_bonificacion(self):
        return super().salario_base * 0.07


class Empresa:
    def __init__(self):
        self.__empleados = []

    def agregar_empleado(self, empleado):
        self.__empleados.append(empleado)

    def calcular_salarios(self):
        salarios = 0
        for e in self.__empleados:
            salarios += e.calcular_salario()
        return salarios

    def mostrar_empleados(self):
        for e in self.__empleados:
            print(e)


def main():
    pass


if __name__ == "__main__":
    main()
