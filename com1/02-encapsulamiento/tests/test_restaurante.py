import unittest

from src.restaurante import CategoriaPlato, Pedido, Plato


class TestPlato(unittest.TestCase):
    # ---------- Constructor ----------

    def test_crear_plato(self):
        plato = Plato("Milanesa", 8500, CategoriaPlato.PRINCIPAL)

        self.assertEqual(plato.nombre, "Milanesa")
        self.assertEqual(plato.precio, 8500)
        self.assertEqual(plato.categoria, CategoriaPlato.PRINCIPAL)

    def test_crear_plato_con_precio_cero(self):
        plato = Plato("Agua", 0, CategoriaPlato.BEBIDA)

        self.assertEqual(plato.precio, 0)

    def test_crear_plato_con_precio_negativo(self):
        with self.assertRaises(ValueError):
            Plato("Milanesa", -100, CategoriaPlato.PRINCIPAL)

    # ---------- Nombre ----------

    def test_modificar_nombre(self):
        plato = Plato("Milanesa", 8500, CategoriaPlato.PRINCIPAL)

        plato.nombre = "Milanesa napolitana"

        self.assertEqual(plato.nombre, "Milanesa napolitana")

    # ---------- Precio ----------

    def test_modificar_precio(self):
        plato = Plato("Milanesa", 8500, CategoriaPlato.PRINCIPAL)

        plato.precio = 9000

        self.assertEqual(plato.precio, 9000)

    def test_modificar_precio_negativo(self):
        plato = Plato("Milanesa", 8500, CategoriaPlato.PRINCIPAL)

        with self.assertRaises(ValueError):
            plato.precio = -500

        # El valor anterior debería conservarse
        self.assertEqual(plato.precio, 8500)

    # ---------- Categoría ----------

    def test_modificar_categoria(self):
        plato = Plato("Tiramisú", 4000, CategoriaPlato.POSTRE)

        plato.categoria = CategoriaPlato.ENTRADA

        self.assertEqual(plato.categoria, CategoriaPlato.ENTRADA)

    def test_todas_las_categorias(self):
        self.assertEqual(CategoriaPlato.ENTRADA.value, 1)
        self.assertEqual(CategoriaPlato.PRINCIPAL.value, 2)
        self.assertEqual(CategoriaPlato.POSTRE.value, 3)
        self.assertEqual(CategoriaPlato.BEBIDA.value, 4)


class TestPedido(unittest.TestCase):
    # ---------- Pedido vacío ----------

    def test_pedido_vacio_total_cero(self):
        pedido = Pedido()

        self.assertEqual(pedido.calcular_total(), 0)

    # ---------- Agregar platos ----------

    def test_agregar_un_plato(self):
        pedido = Pedido()
        plato = Plato("Milanesa", 8500, CategoriaPlato.PRINCIPAL)

        pedido.agregar_plato(plato)

        self.assertEqual(pedido.calcular_total(), 8500)

    def test_agregar_varios_platos(self):
        pedido = Pedido()

        pedido.agregar_plato(Plato("Empanadas", 4500, CategoriaPlato.ENTRADA))
        pedido.agregar_plato(Plato("Milanesa", 8500, CategoriaPlato.PRINCIPAL))
        pedido.agregar_plato(Plato("Flan", 3500, CategoriaPlato.POSTRE))

        self.assertEqual(pedido.calcular_total(), 16500)

    def test_agregar_platos_de_todas_las_categorias(self):
        pedido = Pedido()

        pedido.agregar_plato(Plato("Empanadas", 4000, CategoriaPlato.ENTRADA))
        pedido.agregar_plato(Plato("Ravioles", 9000, CategoriaPlato.PRINCIPAL))
        pedido.agregar_plato(Plato("Flan", 3000, CategoriaPlato.POSTRE))
        pedido.agregar_plato(Plato("Agua", 2000, CategoriaPlato.BEBIDA))

        self.assertEqual(pedido.calcular_total(), 18000)

    def test_agregar_el_mismo_plato_dos_veces(self):
        pedido = Pedido()
        plato = Plato("Gaseosa", 2000, CategoriaPlato.BEBIDA)

        pedido.agregar_plato(plato)
        pedido.agregar_plato(plato)

        self.assertEqual(pedido.calcular_total(), 4000)

    # ---------- Cálculo del total ----------

    def test_total_con_un_plato_de_precio_cero(self):
        pedido = Pedido()

        pedido.agregar_plato(Plato("Agua", 0, CategoriaPlato.BEBIDA))

        self.assertEqual(pedido.calcular_total(), 0)

    def test_total_con_varios_platos_de_precio_cero(self):
        pedido = Pedido()

        pedido.agregar_plato(Plato("Agua", 0, CategoriaPlato.BEBIDA))
        pedido.agregar_plato(Plato("Pan", 0, CategoriaPlato.ENTRADA))

        self.assertEqual(pedido.calcular_total(), 0)

    def test_total_se_actualiza_si_cambia_el_precio(self):
        pedido = Pedido()
        plato = Plato("Milanesa", 8500, CategoriaPlato.PRINCIPAL)

        pedido.agregar_plato(plato)

        plato.precio = 9000

        self.assertEqual(pedido.calcular_total(), 9000)

    # ---------- Ticket ----------

    def test_ticket_pedido_vacio(self):
        pedido = Pedido()

        # Si ticket() usa print()
        # verificamos que no lance una excepción.
        pedido.ticket()

    def test_ticket_contiene_datos_de_los_platos(self):
        pedido = Pedido()

        pedido.agregar_plato(Plato("Milanesa", 8500, CategoriaPlato.PRINCIPAL))
        pedido.agregar_plato(Plato("Flan", 3500, CategoriaPlato.POSTRE))

        # Capturamos la salida de print()
        from unittest.mock import patch

        with patch("builtins.print") as mock_print:
            pedido.ticket()

        salida = "\n".join(str(call) for call in mock_print.call_args_list)

        self.assertIn("Milanesa", salida)
        self.assertIn("Flan", salida)
        self.assertIn("8500", salida)
        self.assertIn("3500", salida)
        self.assertIn("PRINCIPAL", salida)
        self.assertIn("POSTRE", salida)
        self.assertIn("12000", salida)


if __name__ == "__main__":
    unittest.main()
