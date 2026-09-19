import unittest
from io import StringIO
from contextlib import redirect_stdout
from src.empleados_bonificaciones import Desarrollador, Empleado, Empresa, Gerente


class TestEmpleado(unittest.TestCase):
    def test_calcular_bonificacion_empleado(self):
        empleado = Empleado("Ana", 100000)

        self.assertEqual(empleado.calcular_bonificacion(), 5000)

    def test_calcular_salario_empleado(self):
        empleado = Empleado("Ana", 100000)

        self.assertEqual(empleado.calcular_salario(), 105000)


class TestGerente(unittest.TestCase):
    def test_calcular_bonificacion_gerente(self):
        gerente = Gerente("Carlos", 100000)

        self.assertEqual(gerente.calcular_bonificacion(), 10000)

    def test_calcular_salario_gerente(self):
        gerente = Gerente("Carlos", 100000)

        self.assertEqual(gerente.calcular_salario(), 110000)


class TestDesarrollador(unittest.TestCase):
    def test_calcular_bonificacion_desarrollador(self):
        desarrollador = Desarrollador("Laura", 100000)

        self.assertAlmostEqual(
            desarrollador.calcular_bonificacion(), 7000, delta=0.0001
        )

    def test_calcular_salario_desarrollador(self):
        desarrollador = Desarrollador("Laura", 100000)

        self.assertEqual(desarrollador.calcular_salario(), 107000)


class TestEmpresa(unittest.TestCase):
    def test_calcular_salarios(self):
        empresa = Empresa()
        empresa.agregar_empleado(Empleado("Ana", 100000))
        empresa.agregar_empleado(Gerente("Carlos", 100000))
        empresa.agregar_empleado(Desarrollador("Laura", 100000))

        self.assertEqual(empresa.calcular_salarios(), 322000)

    def test_mostrar_empleados(self):
        empresa = Empresa()
        empresa.agregar_empleado(Empleado("Ana", 100000))
        empresa.agregar_empleado(Gerente("Carlos", 100000))
        empresa.agregar_empleado(Desarrollador("Laura", 100000))

        salida = StringIO()

        with redirect_stdout(salida):
            empresa.mostrar_empleados()

        self.assertEqual(
            salida.getvalue(),
            "Ana - Salario: 105000\n"
            "Carlos - Salario: 110000\n"
            "Laura - Salario: 107000\n",
        )


if __name__ == "__main__":
    unittest.main()
