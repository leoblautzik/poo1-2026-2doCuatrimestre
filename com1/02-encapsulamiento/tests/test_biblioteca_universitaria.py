import unittest
from contextlib import redirect_stdout
from io import StringIO

from src.biblioteca_universitaria import Biblioteca, Estudiante, Libro


class TestLibro(unittest.TestCase):
    def test_crear_libro_con_datos_validos(self):
        libro = Libro("Python", "Guido van Rossum", "ISBN001", 5)

        self.assertEqual(libro.titulo, "Python")
        self.assertEqual(libro.autor, "Guido van Rossum")
        self.assertEqual(libro.ejemplares_disponibles, 5)
        self.assertEqual(libro.ejemplares_prestados, 0)

    def test_libro_sin_ejemplares_no_esta_disponible(self):
        libro = Libro("Python", "Guido", "ISBN001", 0)

        self.assertFalse(libro.hay_disponibles())

    def test_libro_con_ejemplares_esta_disponible(self):
        libro = Libro("Python", "Guido", "ISBN001", 1)

        self.assertTrue(libro.hay_disponibles())

    def test_no_se_pueden_crear_libros_con_ejemplares_negativos(self):
        with self.assertRaises(ValueError):
            Libro("Python", "Guido", "ISBN001", -1)

    def test_prestar_un_ejemplar(self):
        libro = Libro("Python", "Guido", "ISBN001", 3)

        libro.prestar()

        self.assertEqual(libro.ejemplares_disponibles, 2)
        self.assertEqual(libro.ejemplares_prestados, 1)

    def test_prestar_el_ultimo_ejemplar(self):
        libro = Libro("Python", "Guido", "ISBN001", 1)

        libro.prestar()

        self.assertEqual(libro.ejemplares_disponibles, 0)
        self.assertEqual(libro.ejemplares_prestados, 1)
        self.assertFalse(libro.hay_disponibles())

    def test_no_se_puede_prestar_sin_ejemplares(self):
        libro = Libro("Python", "Guido", "ISBN001", 0)

        with self.assertRaises(RuntimeError):
            libro.prestar()

    def test_prestar_sin_ejemplares_no_modifica_estado(self):
        libro = Libro("Python", "Guido", "ISBN001", 0)

        with self.assertRaises(RuntimeError):
            libro.prestar()

        self.assertEqual(libro.ejemplares_disponibles, 0)
        self.assertEqual(libro.ejemplares_prestados, 0)

    def test_devolver_un_ejemplar(self):
        libro = Libro("Python", "Guido", "ISBN001", 1)

        libro.prestar()
        libro.devolver()

        self.assertEqual(libro.ejemplares_disponibles, 1)
        self.assertEqual(libro.ejemplares_prestados, 0)

    def test_devolver_un_ejemplar_incrementa_disponibles(self):
        libro = Libro("Python", "Guido", "ISBN001", 3)

        libro.prestar()
        libro.devolver()

        self.assertEqual(libro.ejemplares_disponibles, 3)

    def test_no_se_puede_devolver_si_no_hay_prestamos(self):
        libro = Libro("Python", "Guido", "ISBN001", 3)

        with self.assertRaises(RuntimeError):
            libro.devolver()

    def test_prestar_y_devolver_todos_los_ejemplares(self):
        libro = Libro("Python", "Guido", "ISBN001", 3)

        libro.prestar()
        libro.prestar()
        libro.prestar()

        self.assertEqual(libro.ejemplares_disponibles, 0)
        self.assertEqual(libro.ejemplares_prestados, 3)

        libro.devolver()
        libro.devolver()
        libro.devolver()

        self.assertEqual(libro.ejemplares_disponibles, 3)
        self.assertEqual(libro.ejemplares_prestados, 0)

    def test_no_se_pueden_devolver_mas_ejemplares_de_los_prestados(self):
        libro = Libro("Python", "Guido", "ISBN001", 2)

        libro.prestar()
        libro.devolver()

        with self.assertRaises(RuntimeError):
            libro.devolver()

    def test_atributos_privados_no_son_accesibles_directamente(self):
        libro = Libro("Python", "Guido", "ISBN001", 2)

        self.assertFalse(hasattr(libro, "__titulo"))
        self.assertFalse(hasattr(libro, "__autor"))
        self.assertFalse(hasattr(libro, "__isbn"))
        self.assertFalse(hasattr(libro, "__ejemplares_disponibles"))
        self.assertFalse(hasattr(libro, "__ejemplares_prestados"))

    def test_propiedades_son_de_solo_lectura(self):
        libro = Libro("Python", "Guido", "ISBN001", 2)

        with self.assertRaises(AttributeError):
            libro.titulo = "Java"

        with self.assertRaises(AttributeError):
            libro.autor = "James Gosling"

        with self.assertRaises(AttributeError):
            libro.ejemplares_disponibles = 99

        with self.assertRaises(AttributeError):
            libro.ejemplares_prestados = 99

    def test_repr_contiene_datos_del_libro(self):
        libro = Libro("Python", "Guido", "ISBN001", 2)

        resultado = repr(libro)

        self.assertIn("Python", resultado)
        self.assertIn("Guido", resultado)
        self.assertIn("ISBN001", resultado)


class TestEstudiante(unittest.TestCase):
    def test_crear_estudiante(self):
        estudiante = Estudiante("Aquiles")

        self.assertEqual(estudiante.nombre, "Aquiles")

    def test_nombre_es_de_solo_lectura(self):
        estudiante = Estudiante("Aquiles")

        with self.assertRaises(AttributeError):
            estudiante.nombre = "Sócrates"

    def test_estudiante_tiene_registro_de_prestamos(self):
        estudiante = Estudiante("Aquiles")

        self.assertTrue(hasattr(estudiante, "_Estudiante__prestamos"))

    def test_estudiante_puede_pedir_un_libro(self):
        estudiante = Estudiante("Aquiles")
        libro = Libro("Python", "Guido", "ISBN001", 2)

        estudiante.pedir_prestado(libro, "30-09-2026")

        self.assertEqual(len(estudiante._Estudiante__prestamos), 1)

    def test_pedir_prestado_descuenta_ejemplar(self):
        estudiante = Estudiante("Aquiles")
        libro = Libro("Python", "Guido", "ISBN001", 2)

        estudiante.pedir_prestado(libro, "30-09-2026")

        self.assertEqual(libro.ejemplares_disponibles, 1)
        self.assertEqual(libro.ejemplares_prestados, 1)

    def test_estudiante_conserva_fecha_de_devolucion(self):
        estudiante = Estudiante("Aquiles")
        libro = Libro("Python", "Guido", "ISBN001", 2)

        estudiante.pedir_prestado(libro, "30-09-2026")

        self.assertIn((libro, "30-09-2026"), estudiante._Estudiante__prestamos)

    def test_estudiante_puede_tener_tres_prestamos(self):
        estudiante = Estudiante("Aquiles")

        libros = [
            Libro("Python", "Guido", "ISBN001", 2),
            Libro("Java", "James", "ISBN002", 2),
            Libro("C++", "Bjarne", "ISBN003", 2),
        ]

        estudiante.pedir_prestado(libros[0], "30-09-2026")
        estudiante.pedir_prestado(libros[1], "30-09-2026")
        estudiante.pedir_prestado(libros[2], "30-09-2026")

        self.assertEqual(len(estudiante._Estudiante__prestamos), 3)

    def test_estudiante_no_puede_tener_mas_de_tres_prestamos(self):
        estudiante = Estudiante("Aquiles")

        libros = [
            Libro("Python", "Guido", "ISBN001", 2),
            Libro("Java", "James", "ISBN002", 2),
            Libro("C++", "Bjarne", "ISBN003", 2),
            Libro("Rust", "Graydon", "ISBN004", 2),
        ]

        estudiante.pedir_prestado(libros[0], "30-09-2026")
        estudiante.pedir_prestado(libros[1], "30-09-2026")
        estudiante.pedir_prestado(libros[2], "30-09-2026")

        with self.assertRaises(RuntimeError):
            estudiante.pedir_prestado(libros[3], "30-09-2026")

    def test_rechazar_cuarto_prestamo_no_modifica_registro(self):
        estudiante = Estudiante("Aquiles")

        libros = [
            Libro("Python", "Guido", "ISBN001", 2),
            Libro("Java", "James", "ISBN002", 2),
            Libro("C++", "Bjarne", "ISBN003", 2),
            Libro("Rust", "Graydon", "ISBN004", 2),
        ]

        for libro in libros[:3]:
            estudiante.pedir_prestado(libro, "30-09-2026")

        with self.assertRaises(RuntimeError):
            estudiante.pedir_prestado(libros[3], "30-09-2026")

        self.assertEqual(len(estudiante._Estudiante__prestamos), 3)

    def test_rechazar_cuarto_prestamo_no_modifica_el_libro(self):
        estudiante = Estudiante("Aquiles")

        libros = [
            Libro("Python", "Guido", "ISBN001", 2),
            Libro("Java", "James", "ISBN002", 2),
            Libro("C++", "Bjarne", "ISBN003", 2),
            Libro("Rust", "Graydon", "ISBN004", 2),
        ]

        for libro in libros[:3]:
            estudiante.pedir_prestado(libro, "30-09-2026")

        with self.assertRaises(RuntimeError):
            estudiante.pedir_prestado(libros[3], "30-09-2026")

        self.assertEqual(libros[3].ejemplares_disponibles, 2)
        self.assertEqual(libros[3].ejemplares_prestados, 0)

    def test_pedir_libro_sin_ejemplares_no_agrega_prestamo(self):
        estudiante = Estudiante("Aquiles")
        libro = Libro("Python", "Guido", "ISBN001", 0)

        with self.assertRaises(RuntimeError):
            estudiante.pedir_prestado(libro, "30-09-2026")

        self.assertEqual(estudiante._Estudiante__prestamos, [])

    def test_devolver_libro_que_no_tiene_lanza_error(self):
        estudiante = Estudiante("Aquiles")
        libro = Libro("Python", "Guido", "ISBN001", 2)

        with self.assertRaises(RuntimeError):
            estudiante.devolver(libro)

    def test_devolver_libro_actualiza_registro_y_ejemplares(self):
        estudiante = Estudiante("Aquiles")
        libro = Libro("Python", "Guido", "ISBN001", 1)

        estudiante.pedir_prestado(libro, "30-09-2026")
        estudiante.devolver(libro)

        # self.assertEqual(estudiante._Estudiante__prestamos, [])
        self.assertEqual(libro.ejemplares_disponibles, 1)
        self.assertEqual(libro.ejemplares_prestados, 0)


class TestBiblioteca(unittest.TestCase):
    def test_crear_biblioteca(self):
        libro = Libro("Python", "Guido", "ISBN001", 2)

        biblioteca = Biblioteca([libro])

        self.assertTrue(hasattr(biblioteca, "_Biblioteca__libros"))

    def test_biblioteca_puede_prestar_un_libro(self):
        libro = Libro("Python", "Guido", "ISBN001", 2)
        estudiante = Estudiante("Aquiles")
        biblioteca = Biblioteca([libro])

        biblioteca.prestar(estudiante, libro, "30-09-2026")

        self.assertEqual(libro.ejemplares_prestados, 1)

    def test_biblioteca_registra_el_prestamo(self):
        libro = Libro("Python", "Guido", "ISBN001", 2)
        estudiante = Estudiante("Aquiles")
        biblioteca = Biblioteca([libro])

        biblioteca.prestar(estudiante, libro, "30-09-2026")

        self.assertEqual(len(biblioteca._Biblioteca__prestamos), 1)

    def test_biblioteca_conserva_fecha_de_devolucion(self):
        libro = Libro("Python", "Guido", "ISBN001", 2)
        estudiante = Estudiante("Aquiles")
        biblioteca = Biblioteca([libro])

        biblioteca.prestar(estudiante, libro, "15-10-2026")

        self.assertEqual(biblioteca._Biblioteca__prestamos[0][2], "15-10-2026")

    def test_no_se_puede_prestar_libro_fuera_de_biblioteca(self):
        libro_biblioteca = Libro("Python", "Guido", "ISBN001", 2)
        libro_externo = Libro("Java", "James", "ISBN002", 2)

        estudiante = Estudiante("Aquiles")
        biblioteca = Biblioteca([libro_biblioteca])

        with self.assertRaises(RuntimeError):
            biblioteca.prestar(estudiante, libro_externo, "30-09-2026")

    def test_prestar_libro_fuera_de_biblioteca_no_modifica_estudiante(self):
        libro_biblioteca = Libro("Python", "Guido", "ISBN001", 2)
        libro_externo = Libro("Java", "James", "ISBN002", 2)

        estudiante = Estudiante("Aquiles")
        biblioteca = Biblioteca([libro_biblioteca])

        with self.assertRaises(RuntimeError):
            biblioteca.prestar(estudiante, libro_externo, "30-09-2026")

        self.assertEqual(estudiante._Estudiante__prestamos, [])

    def test_no_se_puede_prestar_libro_sin_ejemplares(self):
        libro = Libro("Python", "Guido", "ISBN001", 0)
        estudiante = Estudiante("Aquiles")
        biblioteca = Biblioteca([libro])

        with self.assertRaises(RuntimeError):
            biblioteca.prestar(estudiante, libro, "30-09-2026")

    def test_no_se_puede_superar_tres_prestamos_desde_biblioteca(self):
        libros = [
            Libro("Python", "Guido", "ISBN001", 2),
            Libro("Java", "James", "ISBN002", 2),
            Libro("C++", "Bjarne", "ISBN003", 2),
            Libro("Rust", "Graydon", "ISBN004", 2),
        ]

        estudiante = Estudiante("Aquiles")
        biblioteca = Biblioteca(libros)

        biblioteca.prestar(estudiante, libros[0], "30-09-2026")
        biblioteca.prestar(estudiante, libros[1], "30-09-2026")
        biblioteca.prestar(estudiante, libros[2], "30-09-2026")

        with self.assertRaises(RuntimeError):
            biblioteca.prestar(estudiante, libros[3], "30-09-2026")

    def test_devolver_libro_actualiza_ejemplares(self):
        libro = Libro("Python", "Guido", "ISBN001", 1)
        estudiante = Estudiante("Aquiles")
        biblioteca = Biblioteca([libro])

        biblioteca.prestar(estudiante, libro, "30-09-2026")

        # Este test requiere que Estudiante.devolver()
        # quite correctamente el préstamo.
        biblioteca.devolver(estudiante, libro)

        self.assertEqual(libro.ejemplares_disponibles, 1)
        self.assertEqual(libro.ejemplares_prestados, 0)

    def test_devolver_libro_elimina_prestamo_de_biblioteca(self):
        libro = Libro("Python", "Guido", "ISBN001", 1)
        estudiante = Estudiante("Aquiles")
        biblioteca = Biblioteca([libro])

        biblioteca.prestar(estudiante, libro, "30-09-2026")
        biblioteca.devolver(estudiante, libro)

        self.assertEqual(biblioteca._Biblioteca__prestamos, [])

    def test_devolver_libro_no_prestado_lanza_error(self):
        libro = Libro("Python", "Guido", "ISBN001", 1)
        estudiante = Estudiante("Aquiles")
        biblioteca = Biblioteca([libro])

        with self.assertRaises(RuntimeError):
            biblioteca.devolver(estudiante, libro)

    def test_dos_estudiantes_pueden_tener_el_mismo_libro(self):
        libro = Libro("Python", "Guido", "ISBN001", 2)

        aquiles = Estudiante("Aquiles")
        socrates = Estudiante("Sócrates")
        biblioteca = Biblioteca([libro])

        biblioteca.prestar(aquiles, libro, "30-09-2026")
        biblioteca.prestar(socrates, libro, "30-09-2026")

        self.assertEqual(libro.ejemplares_prestados, 2)
        self.assertEqual(len(biblioteca._Biblioteca__prestamos), 2)

    def test_devolver_libro_de_un_estudiante_no_elimina_el_de_otro(self):
        libro = Libro("Python", "Guido", "ISBN001", 2)

        aquiles = Estudiante("Aquiles")
        socrates = Estudiante("Sócrates")
        biblioteca = Biblioteca([libro])

        biblioteca.prestar(aquiles, libro, "30-09-2026")
        biblioteca.prestar(socrates, libro, "30-09-2026")

        biblioteca.devolver(socrates, libro)

        prestamos = biblioteca._Biblioteca__prestamos

        self.assertEqual(len(prestamos), 1)
        self.assertEqual(prestamos[0][0], aquiles)

    def test_listar_prestamos_muestra_datos(self):
        libro = Libro("Python", "Guido", "ISBN001", 1)
        estudiante = Estudiante("Aquiles")
        biblioteca = Biblioteca([libro])

        biblioteca.prestar(estudiante, libro, "30-09-2026")

        salida = StringIO()

        with redirect_stdout(salida):
            biblioteca.listar_prestamos()

        resultado = salida.getvalue()

        self.assertIn("Aquiles", resultado)
        self.assertIn("Python", resultado)
        self.assertIn("30-09-2026", resultado)


if __name__ == "__main__":
    unittest.main()
