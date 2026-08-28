import unittest

from cerradura import Cerradura


class TestCerradura(unittest.TestCase):
    def test_example(self):
        self.assertEqual(1 + 1, 2)

    def test_creacion(self):
        trabex = Cerradura(1234, 3)
        self.assertTrue(trabex.esta_abierta())
        self.assertFalse(trabex.esta_cerrada())
        self.assertFalse(trabex.esta_bloqueada())


if __name__ == "__main__":
    unittest.main()
