import unittest

from src.nota import Nota


class TestNota(unittest.TestCase):
    # -------------------------
    # Constructor y propiedad
    # -------------------------

    def test_crear_nota(self):
        nota = Nota(6)
        self.assertEqual(nota.valor, 6)

    # No es correcto en el contexto de una Nota cambiarla si
    # no es recuperando
    # def test_cambiar_valor(self):
    #     nota = Nota(6)
    #     nota.valor = 8
    #     self.assertEqual(nota.valor, 8)

    def test_nota_menor_a_1(self):
        with self.assertRaises(ValueError):
            Nota(0)

    def test_nota_mayor_a_10(self):
        with self.assertRaises(ValueError):
            Nota(11)

    # -------------------------
    # aprobada()
    # -------------------------

    def test_nota_aprobada(self):
        nota = Nota(4)
        self.assertTrue(nota.aprobada())

    def test_nota_no_aprobada(self):
        nota = Nota(3)
        self.assertFalse(nota.aprobada())

    # -------------------------
    # reprobada()
    # -------------------------

    def test_nota_reprobada(self):
        nota = Nota(3)
        self.assertTrue(nota.reprobada())

    def test_nota_no_reprobada(self):
        nota = Nota(4)
        self.assertFalse(nota.reprobada())

    # -------------------------
    # promociona()
    # -------------------------

    def test_nota_promociona(self):
        nota = Nota(7)
        self.assertTrue(nota.promociona())

    def test_nota_no_promociona(self):
        nota = Nota(6)
        self.assertFalse(nota.promociona())

    # -------------------------
    # regulariza()
    # -------------------------

    def test_nota_regulariza(self):
        nota = Nota(6)
        self.assertTrue(nota.regulariza())

    def test_nota_no_regulariza_por_reprobacion(self):
        nota = Nota(3)
        self.assertFalse(nota.regulariza())

    def test_nota_no_regulariza_por_promocion(self):
        nota = Nota(7)
        self.assertFalse(nota.regulariza())

    # -------------------------
    # recupera()
    # -------------------------

    def test_recupera_con_nota_mayor(self):
        nota = Nota(4)
        nota.recupera(7)
        self.assertEqual(nota.valor, 7)

    def test_recupera_con_nota_menor(self):
        nota = Nota(7)
        nota.recupera(4)
        self.assertEqual(nota.valor, 7)

    # -------------------------
    # __str__()
    # -------------------------

    def test_str(self):
        nota = Nota(8)
        self.assertEqual(str(nota), "Nota: 8")


if __name__ == "__main__":
    unittest.main()
