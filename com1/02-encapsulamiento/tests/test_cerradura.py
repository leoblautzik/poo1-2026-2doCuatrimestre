import unittest

from src.cerradura import Cerradura


class TestCerraduraEstadoInicial(unittest.TestCase):
    def test_arranca_cerrada(self):
        c = Cerradura(1234, 3)
        self.assertTrue(c.esta_cerrada())

    def test_arranca_no_abierta(self):
        c = Cerradura(1234, 3)
        self.assertFalse(c.esta_abierta())

    def test_arranca_no_bloqueada(self):
        c = Cerradura(1234, 3)
        self.assertFalse(c.fue_bloqueada())

    def test_arranca_sin_aperturas_exitosas(self):
        c = Cerradura(1234, 3)
        self.assertEqual(c.contar_aperturas_exitosas(), 0)

    def test_arranca_sin_aperturas_fallidas(self):
        c = Cerradura(1234, 3)
        self.assertEqual(c.contar_aperturas_fallidas(), 0)


class TestAbrirConExito(unittest.TestCase):
    def test_abrir_con_clave_correcta_devuelve_true(self):
        c = Cerradura(1234, 3)
        self.assertTrue(c.abrir(1234))

    def test_abrir_con_clave_correcta_queda_abierta(self):
        c = Cerradura(1234, 3)
        c.abrir(1234)
        self.assertTrue(c.esta_abierta())
        self.assertFalse(c.esta_cerrada())

    def test_abrir_con_clave_correcta_incrementa_exitosas(self):
        c = Cerradura(1234, 3)
        c.abrir(1234)
        self.assertEqual(c.contar_aperturas_exitosas(), 1)

    def test_varias_aperturas_exitosas_se_acumulan(self):
        c = Cerradura(1234, 3)
        c.abrir(1234)
        c.cerrar()
        c.abrir(1234)
        c.cerrar()
        c.abrir(1234)
        self.assertEqual(c.contar_aperturas_exitosas(), 3)


class TestAbrirConFallo(unittest.TestCase):
    def test_abrir_con_clave_incorrecta_devuelve_false(self):
        c = Cerradura(1234, 3)
        self.assertFalse(c.abrir(9999))

    def test_abrir_con_clave_incorrecta_sigue_cerrada(self):
        c = Cerradura(1234, 3)
        c.abrir(9999)
        self.assertTrue(c.esta_cerrada())

    def test_abrir_con_clave_incorrecta_incrementa_fallidas(self):
        c = Cerradura(1234, 3)
        c.abrir(9999)
        self.assertEqual(c.contar_aperturas_fallidas(), 1)

    def test_fallos_no_consecutivos_se_acumulan_en_el_contador_total(self):
        c = Cerradura(1234, 3)
        c.abrir(9999)
        c.abrir(1234)
        c.cerrar()
        c.abrir(8888)
        self.assertEqual(c.contar_aperturas_fallidas(), 2)
        self.assertFalse(c.fue_bloqueada())


class TestAbrirYCerrarExcepciones(unittest.TestCase):
    def test_abrir_ya_abierta_lanza_excepcion(self):
        c = Cerradura(1234, 3)
        c.abrir(1234)
        with self.assertRaises(RuntimeError):
            c.abrir(1234)

    def test_cerrar_ya_cerrada_lanza_excepcion(self):
        c = Cerradura(1234, 3)
        with self.assertRaises(RuntimeError):
            c.cerrar()

    def test_cerrar_luego_de_abrir_funciona(self):
        c = Cerradura(1234, 3)
        c.abrir(1234)
        c.cerrar()
        self.assertTrue(c.esta_cerrada())

    def test_ciclo_abrir_cerrar_repetido(self):
        c = Cerradura(1234, 3)
        for _ in range(5):
            c.abrir(1234)
            c.cerrar()
        self.assertEqual(c.contar_aperturas_exitosas(), 5)
        self.assertTrue(c.esta_cerrada())


class TestBloqueo(unittest.TestCase):
    def test_se_bloquea_tras_fallos_consecutivos(self):
        c = Cerradura(1234, 3)
        c.abrir(9999)
        c.abrir(9999)
        c.abrir(9999)
        self.assertTrue(c.fue_bloqueada())

    def test_no_se_bloquea_antes_de_llegar_al_limite(self):
        c = Cerradura(1234, 3)
        c.abrir(9999)
        c.abrir(9999)
        self.assertFalse(c.fue_bloqueada())

    def test_bloqueo_con_limite_uno(self):
        c = Cerradura(1234, 1)
        c.abrir(9999)
        self.assertTrue(c.fue_bloqueada())

    def test_exito_resetea_contador_de_fallos_consecutivos(self):
        c = Cerradura(1234, 3)
        c.abrir(9999)
        c.abrir(9999)
        c.abrir(1234)
        c.cerrar()
        c.abrir(9999)
        c.abrir(9999)
        self.assertFalse(c.fue_bloqueada())

    def test_exito_resetea_y_luego_igual_se_puede_bloquear(self):
        c = Cerradura(1234, 3)
        c.abrir(9999)
        c.abrir(9999)
        c.abrir(1234)
        c.cerrar()
        c.abrir(9999)
        c.abrir(9999)
        c.abrir(9999)
        self.assertTrue(c.fue_bloqueada())

    def test_abrir_bloqueada_lanza_excepcion_incluso_con_clave_correcta(self):
        c = Cerradura(1234, 3)
        c.abrir(9999)
        c.abrir(9999)
        c.abrir(9999)
        with self.assertRaises(RuntimeError):
            c.abrir(1234)

    def test_cerrar_bloqueada_lanza_excepcion(self):
        c = Cerradura(1234, 1)
        c.abrir(9999)
        with self.assertRaises(RuntimeError):
            c.cerrar()

    def test_bloqueada_sigue_estando_cerrada(self):
        c = Cerradura(1234, 3)
        c.abrir(9999)
        c.abrir(9999)
        c.abrir(9999)
        self.assertTrue(c.esta_cerrada())

    def test_contador_de_fallidas_sigue_sumando_aunque_este_bloqueada(self):
        c = Cerradura(1234, 1)
        c.abrir(9999)
        self.assertEqual(c.contar_aperturas_fallidas(), 1)


if __name__ == "__main__":
    unittest.main()
