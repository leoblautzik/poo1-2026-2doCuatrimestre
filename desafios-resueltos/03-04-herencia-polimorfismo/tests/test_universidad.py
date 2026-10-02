```python
import unittest

from estudiante import Estudiante
from arquitecto import Arquitecto
from abogado import Abogado
from universidad import Universidad


class TestEstudiante(unittest.TestCase):

    def test_cuota_base(self):
        Estudiante.set_cuota_base(100000)

        self.assertEqual(100000, Estudiante.get_cuota_base())

    def test_cuota_arquitecto_una_materia(self):
        Estudiante.set_cuota_base(100000)

        arquitecto = Arquitecto(1001, 1)

        # 100000 + 10% de 100000
        self.assertEqual(110000, arquitecto.get_cuota_mensual())

    def test_cuota_arquitecto_tres_materias(self):
        Estudiante.set_cuota_base(100000)

        arquitecto = Arquitecto(1002, 3)

        # 100000 + 3 * 10% de 100000
        self.assertEqual(130000, arquitecto.get_cuota_mensual())

    def test_cuota_arquitecto_cinco_materias(self):
        Estudiante.set_cuota_base(100000)

        arquitecto = Arquitecto(1003, 5)

        self.assertEqual(150000, arquitecto.get_cuota_mensual())

    def test_cuota_abogado_una_materia(self):
        Estudiante.set_cuota_base(100000)

        abogado = Abogado(2001, 1)

        # 100000 + 5% de 100000
        self.assertEqual(105000, abogado.get_cuota_mensual())

    def test_cuota_abogado_tres_materias(self):
        Estudiante.set_cuota_base(100000)

        abogado = Abogado(2002, 3)

        # 100000 + 3 * 5% de 100000
        self.assertEqual(115000, abogado.get_cuota_mensual())

    def test_cuota_abogado_cinco_materias(self):
        Estudiante.set_cuota_base(100000)

        abogado = Abogado(2003, 5)

        self.assertEqual(125000, abogado.get_cuota_mensual())

    def test_cambio_cuota_base_afecta_a_todos(self):
        Estudiante.set_cuota_base(100000)

        arquitecto = Arquitecto(1001, 2)
        abogado = Abogado(2001, 2)

        self.assertEqual(120000, arquitecto.get_cuota_mensual())
        self.assertEqual(110000, abogado.get_cuota_mensual())

        # Cambiamos la cuota base
        Estudiante.set_cuota_base(200000)

        self.assertEqual(240000, arquitecto.get_cuota_mensual())
        self.assertEqual(220000, abogado.get_cuota_mensual())


class TestUniversidad(unittest.TestCase):

    def test_agregar_estudiante(self):
        universidad = Universidad()

        estudiante = Arquitecto(1001, 2)

        universidad.agregar_estudiante(estudiante)

        self.assertEqual(1, len(universidad._estudiantes))

    def test_agregar_varios_estudiantes(self):
        universidad = Universidad()

        universidad.agregar_estudiante(
            Arquitecto(1001, 2)
        )

        universidad.agregar_estudiante(
            Abogado(1002, 3)
        )

        universidad.agregar_estudiante(
            Arquitecto(1003, 1)
        )

        self.assertEqual(3, len(universidad._estudiantes))

    def test_total_mensual_cuotas(self):
        Estudiante.set_cuota_base(100000)

        universidad = Universidad()

        universidad.agregar_estudiante(
            Arquitecto(1001, 2)   # 120000
        )

        universidad.agregar_estudiante(
            Abogado(1002, 3)      # 115000
        )

        universidad.agregar_estudiante(
            Arquitecto(1003, 5)   # 150000
        )

        # 120000 + 115000 + 150000
        self.assertEqual(
            385000,
            universidad.get_total_mensual_cuotas()
        )

    def test_total_sin_estudiantes(self):
        universidad = Universidad()

        self.assertEqual(
            0,
            universidad.get_total_mensual_cuotas()
        )

    def test_total_cambia_al_cambiar_cuota_base(self):
        Estudiante.set_cuota_base(100000)

        universidad = Universidad()

        universidad.agregar_estudiante(
            Arquitecto(1001, 2)
        )

        universidad.agregar_estudiante(
            Abogado(1002, 2)
        )

        # Arquitecto: 120000
        # Abogado:    110000
        self.assertEqual(
            230000,
            universidad.get_total_mensual_cuotas()
        )

        Estudiante.set_cuota_base(200000)

        # Arquitecto: 240000
        # Abogado:    220000
        self.assertEqual(
            460000,
            universidad.get_total_mensual_cuotas()
        )


if __name__ == "__main__":
    unittest.main()


