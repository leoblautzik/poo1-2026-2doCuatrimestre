import unittest

from nota import Nota


class TestNota(unittest.TestCase):
    def test_creacion(self):
        nota = Nota(4)
        self.assertEqual(nota.obtener_valor(), 4)

    def test_aprobado(self):
        nota = Nota(4)
        self.assertTrue(nota.aprobado())

    def test_nota_invalida_menor_que_cero(self):
        with self.assertRaises(ValueError):
            Nota(-1)

    def test_nota_invalida_mayor_que_10(self):
        with self.assertRaises(ValueError):
            Nota(12)

    def test_recupera_con_nota_inferior(self):
        nota = Nota(5)
        nota.recuperar(2)
        self.assertEqual(nota.obtener_valor(), 5)

    def test_recupera_con_nota_superior(self):
        nota = Nota(5)
        nota.recuperar(7)
        self.assertEqual(nota.obtener_valor(), 7)
