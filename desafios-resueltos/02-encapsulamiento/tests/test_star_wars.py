"""
Casos de prueba exhaustivos para la consigna Nave / Escuadron.

IMPORTANTE: ajustá el import de abajo según el nombre del módulo del alumno.
Se asume la estructura de proyecto habitual (src/ + tests/), por ejemplo:

    src/naves.py   -> contiene las clases Nave y Escuadron

Si el archivo del alumno se llama distinto, cambiá solo esta línea:
"""

import unittest

from src.star_wars import Escuadron, Nave  # <-- ajustar si hace falta


class TestNave(unittest.TestCase):
    def test_constructor_guarda_modelo_y_autonomia(self):
        nave = Nave("X-Wing", 120)
        self.assertEqual(nave.modelo, "X-Wing")
        self.assertEqual(nave.autonomia, 120)

    def test_constructor_admite_autonomia_float(self):
        nave = Nave("Y-Wing", 80.5)
        self.assertEqual(nave.autonomia, 80.5)

    def test_str_incluye_modelo_y_autonomia(self):
        nave = Nave("X-Wing", 120)
        texto = str(nave)
        self.assertIsInstance(texto, str)
        self.assertIn("X-Wing", texto)
        self.assertIn("120", texto)

    def test_dos_naves_distintas_son_objetos_distintos(self):
        n1 = Nave("Y-Wing", 80)
        n2 = Nave("Y-Wing", 80)
        # mismo modelo y autonomia, pero deben ser instancias distintas
        self.assertIsNot(n1, n2)


class TestEscuadronConstructorYStr(unittest.TestCase):
    def test_constructor_guarda_nombre(self):
        escuadron = Escuadron("Rogue")
        self.assertEqual(escuadron.nombre, "Rogue")

    def test_constructor_inicializa_naves_vacia(self):
        escuadron = Escuadron("Rogue")
        self.assertEqual(escuadron.naves, [])

    def test_naves_es_una_lista(self):
        escuadron = Escuadron("Rogue")
        self.assertIsInstance(escuadron.naves, list)

    def test_dos_escuadrones_no_comparten_la_misma_lista(self):
        # error clásico: lista mutable como default en el __init__
        e1 = Escuadron("Rogue")
        e2 = Escuadron("Alfa")
        e1.agregar_nave(Nave("X-Wing", 120))
        self.assertEqual(len(e1.naves), 1)
        self.assertEqual(len(e2.naves), 0)

    def test_str_incluye_nombre(self):
        escuadron = Escuadron("Rogue")
        self.assertIn("Rogue", str(escuadron))

    def test_str_no_rompe_con_escuadron_vacio(self):
        escuadron = Escuadron("Rogue")
        # no debe lanzar excepción
        texto = str(escuadron)
        self.assertIsInstance(texto, str)

    def test_str_incluye_datos_de_naves_agregadas(self):
        escuadron = Escuadron("Rogue")
        escuadron.agregar_nave(Nave("X-Wing", 120))
        texto = str(escuadron)
        self.assertIn("X-Wing", texto)


class TestAgregarNave(unittest.TestCase):
    def setUp(self):
        self.escuadron = Escuadron("Rogue")

    def test_agregar_una_nave(self):
        nave = Nave("X-Wing", 120)
        self.escuadron.agregar_nave(nave)
        self.assertEqual(len(self.escuadron.naves), 1)
        self.assertIn(nave, self.escuadron.naves)

    def test_agregar_varias_naves_distintas(self):
        n1 = Nave("X-Wing", 120)
        n2 = Nave("Y-Wing", 80)
        n3 = Nave("A-Wing", 60)
        self.escuadron.agregar_nave(n1)
        self.escuadron.agregar_nave(n2)
        self.escuadron.agregar_nave(n3)
        self.assertEqual(len(self.escuadron.naves), 3)
        self.assertEqual(self.escuadron.naves, [n1, n2, n3])

    def test_agregar_misma_instancia_dos_veces_lanza_runtime_error(self):
        nave = Nave("X-Wing", 120)
        self.escuadron.agregar_nave(nave)
        with self.assertRaises(RuntimeError):
            self.escuadron.agregar_nave(nave)

    def test_duplicado_no_se_agrega_a_la_lista(self):
        nave = Nave("X-Wing", 120)
        self.escuadron.agregar_nave(nave)
        try:
            self.escuadron.agregar_nave(nave)
        except RuntimeError:
            pass
        # el intento fallido no debe dejar el duplicado ni afectar el resto
        self.assertEqual(len(self.escuadron.naves), 1)

    def test_naves_distintas_mismo_modelo_pueden_coexistir(self):
        n1 = Nave("Y-Wing", 80)
        n2 = Nave("Y-Wing", 80)
        self.escuadron.agregar_nave(n1)
        # no debe lanzar excepción: son instancias distintas
        self.escuadron.agregar_nave(n2)
        self.assertEqual(len(self.escuadron.naves), 2)

    def test_ejemplo_completo_del_enunciado(self):
        nave = Nave("X-Wing", 120)
        alfa = nave
        escuadron = Escuadron("Rogue")
        escuadron.agregar_nave(nave)
        escuadron.agregar_nave(Nave("Y-Wing", 80))
        escuadron.agregar_nave(Nave("Y-Wing", 80))
        escuadron.agregar_nave(Nave("A-Wing", 60))
        with self.assertRaises(RuntimeError):
            escuadron.agregar_nave(alfa)  # duplicado
        self.assertEqual(len(escuadron.naves), 4)


class TestNavesConAutonomia(unittest.TestCase):
    def setUp(self):
        self.escuadron = Escuadron("Rogue")
        self.x_wing = Nave("X-Wing", 120)  # ida+vuelta hasta 60
        self.y_wing = Nave("Y-Wing", 80)  # ida+vuelta hasta 40
        self.a_wing = Nave("A-Wing", 60)  # ida+vuelta hasta 30
        for n in (self.x_wing, self.y_wing, self.a_wing):
            self.escuadron.agregar_nave(n)

    def test_devuelve_solo_naves_que_alcanzan_ida_y_vuelta(self):
        resultado = self.escuadron.naves_con_autonomia(50)
        self.assertEqual(resultado, [self.x_wing])

    def test_devuelve_lista_vacia_si_ninguna_alcanza(self):
        resultado = self.escuadron.naves_con_autonomia(1000)
        self.assertEqual(resultado, [])

    def test_devuelve_todas_si_todas_alcanzan(self):
        resultado = self.escuadron.naves_con_autonomia(10)
        self.assertEqual(len(resultado), 3)
        for n in (self.x_wing, self.y_wing, self.a_wing):
            self.assertIn(n, resultado)

    def test_caso_limite_autonomia_exactamente_el_doble_de_la_distancia(self):
        # autonomia == 2 * distancia -> justo alcanza para ir y volver
        nave_justa = Nave("B-Wing", 100)
        escuadron = Escuadron("Ala Azul")
        escuadron.agregar_nave(nave_justa)
        resultado = escuadron.naves_con_autonomia(50)
        self.assertIn(nave_justa, resultado)

    def test_caso_limite_autonomia_un_poco_menos_del_doble(self):
        nave_corta = Nave("B-Wing", 99)
        escuadron = Escuadron("Ala Azul")
        escuadron.agregar_nave(nave_corta)
        resultado = escuadron.naves_con_autonomia(50)
        self.assertEqual(resultado, [])

    def test_distancia_cero_devuelve_todas_las_naves(self):
        resultado = self.escuadron.naves_con_autonomia(0)
        self.assertEqual(len(resultado), 3)

    def test_escuadron_vacio_devuelve_lista_vacia(self):
        escuadron_vacio = Escuadron("Fantasma")
        resultado = escuadron_vacio.naves_con_autonomia(10)
        self.assertEqual(resultado, [])

    def test_resultado_es_una_lista(self):
        resultado = self.escuadron.naves_con_autonomia(10)
        self.assertIsInstance(resultado, list)

    def test_no_modifica_la_lista_de_naves_del_escuadron(self):
        naves_antes = list(self.escuadron.naves)
        self.escuadron.naves_con_autonomia(50)
        self.assertEqual(self.escuadron.naves, naves_antes)

    def test_no_modifica_autonomia_de_las_naves(self):
        autonomias_antes = [n.autonomia for n in self.escuadron.naves]
        self.escuadron.naves_con_autonomia(50)
        autonomias_despues = [n.autonomia for n in self.escuadron.naves]
        self.assertEqual(autonomias_antes, autonomias_despues)

    def test_lista_devuelta_no_es_la_misma_referencia_que_naves(self):
        resultado = self.escuadron.naves_con_autonomia(10)
        self.assertIsNot(resultado, self.escuadron.naves)

    def test_mutar_lista_devuelta_no_afecta_al_escuadron(self):
        resultado = self.escuadron.naves_con_autonomia(10)
        cantidad_original = len(self.escuadron.naves)
        resultado.clear()
        self.assertEqual(len(self.escuadron.naves), cantidad_original)

    def test_preserva_orden_de_insercion(self):
        # todas alcanzan con distancia chica -> el orden debe respetar
        # el orden en que fueron agregadas
        resultado = self.escuadron.naves_con_autonomia(10)
        self.assertEqual(resultado, [self.x_wing, self.y_wing, self.a_wing])

    def test_naves_repetidas_de_modelo_se_evaluan_individualmente(self):
        escuadron = Escuadron("Ala Roja")
        corta = Nave("Y-Wing", 50)  # no alcanza para distancia 30
        larga = Nave("Y-Wing", 80)  # sí alcanza
        escuadron.agregar_nave(corta)
        escuadron.agregar_nave(larga)
        resultado = escuadron.naves_con_autonomia(30)
        self.assertEqual(resultado, [larga])


if __name__ == "__main__":
    unittest.main()
