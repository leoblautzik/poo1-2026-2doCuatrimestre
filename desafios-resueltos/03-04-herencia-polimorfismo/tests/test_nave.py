import unittest

from src.nave import Bombardero, Caza, Crucero


class TestCombateNaves(unittest.TestCase):
    def test_caza_ataca_a_caza(self):
        c1 = Caza("X-Wing")
        c2 = Caza("TIE Fighter")
        c1.atacar(c2)
        self.assertEqual(c2.salud, 85)

    def test_caza_destruye_a_otro(self):
        atacante = Caza("X-Wing")
        victima = Caza("TIE Fighter")

        for _ in range(7):
            atacante.atacar(victima)

        self.assertTrue(victima.esta_destruida())
        self.assertEqual(victima.salud, 0)

    def test_no_se_puede_atacar_una_nave_destruida(self):
        atacante = Caza("X-Wing")
        victima = Caza("TIE Fighter")

        for _ in range(7):
            atacante.atacar(victima)

        atacante.atacar(victima)

        self.assertEqual(victima.salud, 0)

    def test_bombardero_ataca_y_se_autodana(self):
        b = Bombardero("TIE Bomber")
        c = Caza("X-Wing")

        b.atacar(c)

        self.assertEqual(c.salud, 75)
        self.assertEqual(b.salud, 145)

    def test_bombardero_se_autodestruye_con_muchos_ataques(self):
        b = Bombardero("TIE Bomber")
        objetivos = [Caza(f"X-Wing-{i}") for i in range(8)]

        for i in range(30):
            b.atacar(objetivos[i // 4])

        self.assertTrue(b.esta_destruida())
        self.assertEqual(b.salud, 0)

    def test_crucero_ataca_con_salud_alta(self):
        cr = Crucero("Destructor Estelar")
        c = Caza("X-Wing")

        cr.atacar(c)

        self.assertEqual(c.salud, 60)

    def test_crucero_no_ataca_con_salud_baja(self):
        cr = Crucero("Destructor Estelar")
        atacante = Bombardero("TIE Bomber")

        # Se reduce la salud usando la interfaz pública.
        for _ in range(10):
            atacante.atacar(cr)

        self.assertEqual(cr.salud, 50)

        victima = Caza("X-Wing")
        cr.atacar(victima)

        self.assertEqual(victima.salud, 100)

    def test_estado_muestra_nombre_y_salud(self):
        c = Caza("X-Wing")
        esperado = "Nave: X-Wing, Salud: 100"

        self.assertEqual(c.estado(), esperado)

    def test_encadenamiento_de_ataques(self):
        c = Caza("X-Wing")
        b = Bombardero("TIE Bomber")
        cr = Crucero("Destructor Estelar")

        c.atacar(b)
        b.atacar(cr)
        cr.atacar(c)

        self.assertEqual(b.salud, 130)
        self.assertEqual(cr.salud, 275)
        self.assertEqual(c.salud, 60)

    def test_destruccion_por_crucero(self):
        cr = Crucero("Destructor Estelar")
        c = Caza("X-Wing")

        for _ in range(3):
            cr.atacar(c)

        self.assertTrue(c.esta_destruida())
        self.assertEqual(c.salud, 0)


if __name__ == "__main__":
    unittest.main()
