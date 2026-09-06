import unittest

from src.tarjeta_baja import TarjetaBaja


class TestTarjetaBaja(unittest.TestCase):
    def test_consultar_saldo_inicial(self):
        tb = TarjetaBaja(100)
        self.assertEqual(100, tb.consultar_saldo())

    def test_recargar_100(self):
        tb = TarjetaBaja(100)
        tb.recargar(100)
        self.assertEqual(200, tb.consultar_saldo())

    def test_pago_un_viaje_en_colectivo_dinero_suficiente(self):
        tb = TarjetaBaja(50)
        tb.pagar_viaje_colectivo()
        tb.pagar_viaje_colectivo()
        self.assertEqual(7, tb.consultar_saldo())
        self.assertEqual(2, tb.consultar_cuantos_viajes_colectivo())

    def test_pago_un_viaje_en_colectivo_dinero_INsuficiente(self):
        tb = TarjetaBaja(20)
        tb.pagar_viaje_colectivo()
        self.assertEqual(20, tb.consultar_saldo())

    def test_pago_un_viaje_en_colectivo_dinero_justito(self):
        tb = TarjetaBaja(21.5)
        tb.pagar_viaje_colectivo()
        self.assertEqual(0, tb.consultar_saldo())
        self.assertEqual(1, tb.consultar_cuantos_viajes_colectivo())


if __name__ == "__main__":
    unittest.main()
