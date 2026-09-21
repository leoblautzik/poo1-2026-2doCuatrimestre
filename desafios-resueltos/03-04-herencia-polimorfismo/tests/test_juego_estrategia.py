"""
Tests exhaustivos para juego_estrategia.py

Reglas seguidas para escribir estos tests:
- Sin setUp/tearDown: cada test crea sus propias instancias.
- Sin acceso a atributos privados (nada de _Clase__atributo): solo se usa
  la API pública (constructor, `salud`, `esta_viva`, `puede_atacar`,
  `atacar`, `recibir_ataque`, `distancia`, `recibir_agua`,
  `recibir_flechas`, `contar_ataques`, `esta_rebelde`).
"""

import unittest

from juego_estrategia import (
    Aguatero,
    Arquero,
    Caballero,
    Caballo,
    Lancero,
    Soldado,
    Unidad,
)


class TestJuegoEstrategia(unittest.TestCase):
    def test_unidad_no_se_puede_instanciar_directamente(self):
        with self.assertRaises(TypeError):
            Unidad(salud=100, danio=10, posicion=0)

    def test_aguatero_no_se_puede_instanciar_directamente(self):
        with self.assertRaises(TypeError):
            Aguatero()


class TestInterfazAguatero(unittest.TestCase):
    def test_soldado_es_aguatero(self):
        self.assertIsInstance(Soldado(posicion=0), Aguatero)

    def test_caballero_es_aguatero(self):
        self.assertIsInstance(Caballero(posicion=0), Aguatero)

    def test_caballo_es_aguatero(self):
        self.assertIsInstance(Caballo(), Aguatero)

    def test_arquero_no_es_aguatero(self):
        self.assertNotIsInstance(Arquero(posicion=0), Aguatero)

    def test_lancero_no_es_aguatero(self):
        self.assertNotIsInstance(Lancero(posicion=0), Aguatero)


class TestSoldado(unittest.TestCase):
    def test_salud_inicial(self):
        self.assertEqual(Soldado(posicion=0).salud, 200)

    def test_esta_viva_al_crear(self):
        self.assertTrue(Soldado(posicion=0).esta_viva())

    def test_puede_atacar_a_distancia_cero(self):
        soldado = Soldado(posicion=5)
        objetivo = Lancero(posicion=5)
        self.assertTrue(soldado.puede_atacar(objetivo))

    def test_no_puede_atacar_a_distancia_mayor_a_cero(self):
        soldado = Soldado(posicion=5)
        objetivo = Lancero(posicion=6)
        self.assertFalse(soldado.puede_atacar(objetivo))

    def test_no_puede_atacar_si_el_objetivo_esta_muerto(self):
        soldado = Soldado(posicion=0)
        objetivo = Arquero(posicion=0)  # salud 50, danio soldado 10 -> 5 golpes matan
        for _ in range(5):
            objetivo.recibir_ataque(soldado)
        self.assertFalse(objetivo.esta_viva())
        self.assertFalse(soldado.puede_atacar(objetivo))

    def test_no_puede_atacar_si_el_soldado_esta_muerto(self):
        soldado = Soldado(posicion=0)  # salud 200
        atacante = Lancero(posicion=0)  # danio 25 -> 8 golpes matan
        for _ in range(8):
            soldado.recibir_ataque(atacante)
        self.assertFalse(soldado.esta_viva())
        objetivo = Lancero(posicion=0)
        self.assertFalse(soldado.puede_atacar(objetivo))

    def test_no_puede_atacar_sin_energia_suficiente(self):
        soldado = Soldado(posicion=0)
        objetivo = Lancero(posicion=0)  # salud 150, aguanta 10 golpes de 10
        for _ in range(10):
            soldado.atacar(objetivo)
        self.assertTrue(objetivo.esta_viva())  # confirma que no murio antes
        self.assertEqual(soldado.energia, 0)
        self.assertFalse(soldado.puede_atacar(objetivo))

    def test_energia_inicial(self):
        self.assertEqual(Soldado(posicion=0).energia, 100)

    def test_atacar_consume_diez_de_energia_por_ataque(self):
        soldado = Soldado(posicion=0)
        objetivo = Lancero(posicion=0)
        soldado.atacar(objetivo)
        self.assertEqual(soldado.energia, 90)
        soldado.atacar(objetivo)
        self.assertEqual(soldado.energia, 80)

    def test_energia_es_de_solo_lectura(self):
        soldado = Soldado(posicion=0)
        with self.assertRaises(AttributeError):
            soldado.energia = 9999

    def test_atacar_reduce_la_salud_del_objetivo_en_el_danio_correcto(self):
        soldado = Soldado(posicion=3)
        objetivo = Lancero(posicion=3)
        soldado.atacar(objetivo)
        self.assertEqual(objetivo.salud, 140)  # 150 - 10

    def test_atacar_no_hace_nada_si_no_puede_atacar(self):
        soldado = Soldado(posicion=0)
        objetivo = Lancero(posicion=5)  # fuera de rango
        soldado.atacar(objetivo)
        self.assertEqual(objetivo.salud, 150)
        self.assertEqual(soldado.energia, 100)  # tampoco se consume energia

    def test_recibir_agua_restaura_energia_a_cien(self):
        soldado = Soldado(posicion=0)
        objetivo = Lancero(posicion=0)
        for _ in range(10):
            soldado.atacar(objetivo)
        self.assertEqual(soldado.energia, 0)
        self.assertFalse(soldado.puede_atacar(objetivo))
        soldado.recibir_agua()
        self.assertEqual(soldado.energia, 100)
        self.assertTrue(soldado.puede_atacar(objetivo))


class TestArquero(unittest.TestCase):
    def test_salud_inicial(self):
        self.assertEqual(Arquero(posicion=0).salud, 50)

    def test_puede_atacar_en_los_extremos_del_rango(self):
        arquero = Arquero(posicion=0)
        self.assertTrue(arquero.puede_atacar(Lancero(posicion=2)))
        self.assertTrue(arquero.puede_atacar(Lancero(posicion=5)))

    def test_no_puede_atacar_fuera_de_rango(self):
        arquero = Arquero(posicion=0)
        self.assertFalse(arquero.puede_atacar(Lancero(posicion=1)))
        self.assertFalse(arquero.puede_atacar(Lancero(posicion=6)))

    def test_no_puede_atacar_sin_flechas(self):
        arquero = Arquero(posicion=0)
        objetivo = Caballero(posicion=3)  # salud 200, aguanta 20 golpes de 5
        for _ in range(20):
            arquero.atacar(objetivo)
        self.assertTrue(objetivo.esta_viva())
        self.assertEqual(arquero.flechas, 0)
        self.assertFalse(arquero.puede_atacar(objetivo))

    def test_flechas_inicial(self):
        self.assertEqual(Arquero(posicion=0).flechas, 20)

    def test_atacar_consume_una_flecha_por_ataque(self):
        arquero = Arquero(posicion=0)
        objetivo = Lancero(posicion=3)
        arquero.atacar(objetivo)
        self.assertEqual(arquero.flechas, 19)
        arquero.atacar(objetivo)
        self.assertEqual(arquero.flechas, 18)

    def test_flechas_es_de_solo_lectura(self):
        arquero = Arquero(posicion=0)
        with self.assertRaises(AttributeError):
            arquero.flechas = 9999

    def test_recibir_flechas_con_cantidad_por_defecto_suma_seis(self):
        arquero = Arquero(posicion=0)
        objetivo = Caballero(posicion=3)
        for _ in range(20):
            arquero.atacar(objetivo)
        arquero.recibir_flechas()  # +6 por defecto
        self.assertEqual(arquero.flechas, 6)
        self.assertTrue(arquero.puede_atacar(objetivo))

    def test_recibir_flechas_con_cantidad_personalizada(self):
        arquero = Arquero(posicion=0)
        objetivo = Caballero(posicion=3)
        for _ in range(20):
            arquero.atacar(objetivo)
        self.assertFalse(arquero.puede_atacar(objetivo))
        arquero.recibir_flechas(cantidad=1)
        self.assertEqual(arquero.flechas, 1)
        self.assertTrue(arquero.puede_atacar(objetivo))

    def test_atacar_reduce_la_salud_del_objetivo_en_el_danio_correcto(self):
        arquero = Arquero(posicion=0)
        objetivo = Lancero(posicion=3)
        arquero.atacar(objetivo)
        self.assertEqual(objetivo.salud, 145)  # 150 - 5

    def test_atacar_no_hace_nada_si_no_puede_atacar(self):
        arquero = Arquero(posicion=0)
        objetivo = Lancero(posicion=0)  # fuera de rango (distancia 0)
        arquero.atacar(objetivo)
        self.assertEqual(objetivo.salud, 150)
        self.assertEqual(arquero.flechas, 20)  # tampoco se consume flecha

    def test_no_puede_atacar_si_el_arquero_esta_muerto(self):
        arquero = Arquero(posicion=0)  # salud 50
        atacante = Caballero(posicion=0)  # danio 50 -> 1 golpe mata
        arquero.recibir_ataque(atacante)
        self.assertFalse(arquero.esta_viva())
        self.assertFalse(arquero.puede_atacar(Lancero(posicion=2)))


class TestLancero(unittest.TestCase):
    def test_salud_inicial(self):
        self.assertEqual(Lancero(posicion=0).salud, 150)

    def test_puede_atacar_en_los_extremos_del_rango(self):
        lancero = Lancero(posicion=0)
        self.assertTrue(lancero.puede_atacar(Arquero(posicion=1)))
        self.assertTrue(lancero.puede_atacar(Arquero(posicion=3)))

    def test_no_puede_atacar_fuera_de_rango(self):
        lancero = Lancero(posicion=0)
        self.assertFalse(lancero.puede_atacar(Arquero(posicion=0)))
        self.assertFalse(lancero.puede_atacar(Arquero(posicion=4)))

    def test_no_tiene_restriccion_de_recurso_y_puede_seguir_atacando(self):
        lancero = Lancero(posicion=0)
        objetivo = Caballero(posicion=1)
        for _ in range(20):
            lancero.atacar(objetivo)
        # a diferencia de soldado/arquero, el lancero no depende de un
        # recurso que se agote: mientras este vivo y en rango, puede seguir.
        nuevo_objetivo = Caballero(posicion=1)
        self.assertTrue(lancero.puede_atacar(nuevo_objetivo))

    def test_atacar_reduce_la_salud_del_objetivo_en_el_danio_correcto(self):
        lancero = Lancero(posicion=0)
        objetivo = Soldado(posicion=1)
        lancero.atacar(objetivo)
        self.assertEqual(objetivo.salud, 175)  # 200 - 25

    def test_no_puede_atacar_si_esta_muerto(self):
        lancero = Lancero(posicion=0)  # salud 150
        atacante = Caballero(posicion=0)  # danio 50 -> 3 golpes matan
        for _ in range(3):
            lancero.recibir_ataque(atacante)
        self.assertFalse(lancero.esta_viva())
        self.assertFalse(lancero.puede_atacar(Arquero(posicion=1)))


class TestCaballero(unittest.TestCase):
    def test_salud_inicial(self):
        self.assertEqual(Caballero(posicion=0).salud, 200)

    def test_puede_atacar_en_los_extremos_del_rango(self):
        caballero = Caballero(posicion=0)
        self.assertTrue(caballero.puede_atacar(Arquero(posicion=1)))
        self.assertTrue(caballero.puede_atacar(Arquero(posicion=2)))

    def test_no_puede_atacar_fuera_de_rango(self):
        caballero = Caballero(posicion=0)
        self.assertFalse(caballero.puede_atacar(Arquero(posicion=0)))
        self.assertFalse(caballero.puede_atacar(Arquero(posicion=3)))

    def test_atacar_reduce_la_salud_del_objetivo_en_el_danio_correcto(self):
        caballero = Caballero(posicion=0)
        objetivo = Soldado(posicion=1)
        caballero.atacar(objetivo)
        self.assertEqual(objetivo.salud, 150)  # 200 - 50

    def test_el_caballo_se_pone_rebelde_tras_tres_ataques(self):
        caballero = Caballero(posicion=0)
        objetivo = Caballero(posicion=1)  # salud 200, aguanta 3 golpes de 50
        for _ in range(3):
            self.assertTrue(caballero.puede_atacar(objetivo))
            caballero.atacar(objetivo)
        self.assertTrue(objetivo.esta_viva())  # confirma que no murio antes
        self.assertFalse(caballero.puede_atacar(objetivo))

    def test_recibir_agua_calma_al_caballo_y_permite_atacar_de_nuevo(self):
        caballero = Caballero(posicion=0)
        objetivo = Caballero(posicion=1)
        for _ in range(3):
            caballero.atacar(objetivo)
        self.assertFalse(caballero.puede_atacar(objetivo))
        caballero.recibir_agua()
        self.assertTrue(caballero.puede_atacar(objetivo))

    def test_no_puede_atacar_si_el_caballero_esta_muerto(self):
        caballero = Caballero(posicion=0)  # salud 200
        atacante = Lancero(posicion=0)  # danio 25 -> 8 golpes matan
        for _ in range(8):
            caballero.recibir_ataque(atacante)
        self.assertFalse(caballero.esta_viva())
        self.assertFalse(caballero.puede_atacar(Arquero(posicion=1)))


class TestCaballo(unittest.TestCase):
    def test_no_esta_rebelde_al_crear(self):
        self.assertFalse(Caballo().esta_rebelde())

    def test_no_esta_rebelde_con_menos_de_tres_ataques(self):
        caballo = Caballo()
        caballo.contar_ataques()
        caballo.contar_ataques()
        self.assertFalse(caballo.esta_rebelde())

    def test_se_pone_rebelde_exactamente_al_tercer_ataque(self):
        caballo = Caballo()
        caballo.contar_ataques()
        caballo.contar_ataques()
        caballo.contar_ataques()
        self.assertTrue(caballo.esta_rebelde())

    def test_contar_ataques_no_sigue_sumando_una_vez_rebelde(self):
        caballo = Caballo()
        for _ in range(10):
            caballo.contar_ataques()
        self.assertTrue(caballo.esta_rebelde())

    def test_recibir_agua_calma_al_caballo(self):
        caballo = Caballo()
        for _ in range(3):
            caballo.contar_ataques()
        self.assertTrue(caballo.esta_rebelde())
        caballo.recibir_agua()
        self.assertFalse(caballo.esta_rebelde())


class TestReglasGenerales(unittest.TestCase):
    def test_recibir_ataque_reduce_la_salud_exactamente_en_el_danio(self):
        objetivo = Lancero(posicion=0)
        atacante = Soldado(posicion=0)
        objetivo.recibir_ataque(atacante)
        self.assertEqual(objetivo.salud, 140)  # 150 - 10

    def test_esta_viva_es_falso_al_llegar_exactamente_a_cero(self):
        objetivo = Arquero(posicion=0)  # salud 50
        atacante = Soldado(posicion=0)  # danio 10
        for _ in range(5):
            objetivo.recibir_ataque(atacante)
        self.assertEqual(objetivo.salud, 0)
        self.assertFalse(objetivo.esta_viva())

    def test_esta_viva_es_falso_por_debajo_de_cero(self):
        objetivo = Arquero(posicion=0)  # salud 50
        atacante = Lancero(posicion=0)  # danio 25
        for _ in range(3):
            objetivo.recibir_ataque(atacante)
        self.assertLess(objetivo.salud, 0)
        self.assertFalse(objetivo.esta_viva())

    def test_distancia_es_simetrica(self):
        a = Soldado(posicion=2)
        b = Arquero(posicion=7)
        self.assertEqual(a.distancia(b), b.distancia(a))
        self.assertEqual(a.distancia(b), 5)

    def test_distancia_cero_en_la_misma_posicion(self):
        a = Soldado(posicion=4)
        b = Lancero(posicion=4)
        self.assertEqual(a.distancia(b), 0)

    def test_salud_es_de_solo_lectura(self):
        soldado = Soldado(posicion=0)
        with self.assertRaises(AttributeError):
            soldado.salud = 9999


if __name__ == "__main__":
    unittest.main(verbosity=2)
