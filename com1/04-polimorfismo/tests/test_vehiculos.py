import unittest

from src.vehiculos import Autobus, Motocicleta, Persona, Vehiculo


class TestPersona(unittest.TestCase):
    def test_crear_persona(self):
        persona = Persona("Juan")

        self.assertEqual("Juan", str(persona))

    def test_repr_persona(self):
        persona = Persona("Juan")

        self.assertEqual("Juan", repr(persona))

    def test_personas_con_nombres_diferentes(self):
        persona1 = Persona("Juan")
        persona2 = Persona("Ana")

        self.assertNotEqual(str(persona1), str(persona2))


class TestVehiculo(unittest.TestCase):
    def test_crear_vehiculo(self):
        vehiculo = Vehiculo(1000)

        self.assertIsInstance(vehiculo, Vehiculo)

    def test_crear_vehiculo_sin_chofer(self):
        vehiculo = Vehiculo(1000)

        self.assertIn("Chofer: None", str(vehiculo))

    def test_asignar_chofer(self):
        vehiculo = Vehiculo(1000)
        chofer = Persona("Juan")

        vehiculo.asignar_chofer(chofer)

        self.assertIn("Chofer: Juan", str(vehiculo))

    def test_asignar_chofer_dos_veces(self):
        vehiculo = Vehiculo(1000)

        vehiculo.asignar_chofer(Persona("Juan"))

        with self.assertRaisesRegex(RuntimeError, "Ya hay un chofer asignado"):
            vehiculo.asignar_chofer(Persona("Ana"))

    def test_cambiar_chofer_sin_chofer_asignado(self):
        vehiculo = Vehiculo(1000)

        with self.assertRaisesRegex(RuntimeError, "No hay chofer asignado"):
            vehiculo.cambiar_chofer(Persona("Juan"))

    def test_cambiar_chofer(self):
        vehiculo = Vehiculo(1000)

        vehiculo.asignar_chofer(Persona("Juan"))
        vehiculo.cambiar_chofer(Persona("Ana"))

        self.assertIn("Chofer: Ana", str(vehiculo))

    def test_cambiar_chofer_varias_veces(self):
        vehiculo = Vehiculo(1000)

        vehiculo.asignar_chofer(Persona("Juan"))
        vehiculo.cambiar_chofer(Persona("Ana"))
        vehiculo.cambiar_chofer(Persona("Pedro"))

        self.assertIn("Chofer: Pedro", str(vehiculo))

    def test_kilometros_en_str(self):
        vehiculo = Vehiculo(1500)

        self.assertIn("Kilometraje: 1500", str(vehiculo))

    def test_chofer_debe_ser_persona(self):
        vehiculo = Vehiculo(1000)
        chofer = Persona("Juan")

        vehiculo.asignar_chofer(chofer)

        self.assertIsInstance(chofer, Persona)


class TestMotocicleta(unittest.TestCase):
    def test_crear_motocicleta(self):
        moto = Motocicleta(1000)

        self.assertIsInstance(moto, Motocicleta)
        self.assertIsInstance(moto, Vehiculo)

    def test_agregar_acompanante(self):
        moto = Motocicleta(1000)
        acompanante = Persona("Ana")

        moto.agregar_acompanante(acompanante)

        self.assertIn("Acompañante: Ana", str(moto))

    def test_agregar_acompanante_dos_veces(self):
        moto = Motocicleta(1000)

        moto.agregar_acompanante(Persona("Ana"))

        with self.assertRaisesRegex(
            RuntimeError, "La motocicleta ya tiene un acompañante"
        ):
            moto.agregar_acompanante(Persona("Pedro"))

    def test_cambiar_chofer_con_acompanante(self):
        moto = Motocicleta(1000)

        moto.asignar_chofer(Persona("Juan"))
        moto.agregar_acompanante(Persona("Ana"))

        with self.assertRaisesRegex(
            RuntimeError, "No se puede cambiar de chofer con un acompañante a bordo"
        ):
            moto.cambiar_chofer(Persona("Pedro"))

    def test_cambiar_chofer_sin_acompanante(self):
        moto = Motocicleta(1000)

        moto.asignar_chofer(Persona("Juan"))
        moto.cambiar_chofer(Persona("Pedro"))

        self.assertIn("Chofer: Pedro", str(moto))

    def test_cambiar_chofer_sin_chofer_y_sin_acompanante(self):
        moto = Motocicleta(1000)

        with self.assertRaisesRegex(RuntimeError, "No hay chofer asignado"):
            moto.cambiar_chofer(Persona("Pedro"))

    def test_motocicleta_tiene_kilometros(self):
        moto = Motocicleta(2500)

        self.assertIn("Kilometraje: 2500", str(moto))

    def test_motocicleta_str(self):
        moto = Motocicleta(1000)

        self.assertIn("Motocicleta", str(moto))


class TestAutobus(unittest.TestCase):
    def test_crear_autobus(self):
        autobus = Autobus(5000)

        self.assertIsInstance(autobus, Autobus)
        self.assertIsInstance(autobus, Vehiculo)

    def test_agregar_pasajero(self):
        autobus = Autobus(5000)
        pasajero = Persona("Ana")

        autobus.agregar_pasajero(pasajero)

        self.assertIn("Ana", str(autobus))

    def test_agregar_varios_pasajeros(self):
        autobus = Autobus(5000)

        autobus.agregar_pasajero(Persona("Ana"))
        autobus.agregar_pasajero(Persona("Pedro"))
        autobus.agregar_pasajero(Persona("Maria"))

        texto = str(autobus)

        self.assertIn("Ana", texto)
        self.assertIn("Pedro", texto)
        self.assertIn("Maria", texto)

    def test_cambiar_chofer_con_pasajeros(self):
        autobus = Autobus(5000)

        autobus.asignar_chofer(Persona("Juan"))
        autobus.agregar_pasajero(Persona("Ana"))

        with self.assertRaisesRegex(
            RuntimeError, "No se puede cambiar de chofer con pasajeros a bordo"
        ):
            autobus.cambiar_chofer(Persona("Pedro"))

    def test_cambiar_chofer_sin_pasajeros(self):
        autobus = Autobus(5000)

        autobus.asignar_chofer(Persona("Juan"))
        autobus.cambiar_chofer(Persona("Pedro"))

        self.assertIn("Chofer: Pedro", str(autobus))

    def test_cambiar_chofer_sin_chofer_y_sin_pasajeros(self):
        autobus = Autobus(5000)

        with self.assertRaisesRegex(RuntimeError, "No hay chofer asignado"):
            autobus.cambiar_chofer(Persona("Pedro"))

    def test_autobus_tiene_kilometros(self):
        autobus = Autobus(7000)

        self.assertIn("Kilometraje: 7000", str(autobus))

    def test_autobus_str(self):
        autobus = Autobus(5000)

        self.assertIn("Autobus", str(autobus))


class TestPolimorfismo(unittest.TestCase):
    def test_moto_y_autobus_son_vehiculos(self):
        moto = Motocicleta(1000)
        autobus = Autobus(5000)

        vehiculos = [moto, autobus]

        for vehiculo in vehiculos:
            self.assertIsInstance(vehiculo, Vehiculo)

    def test_mismo_metodo_distinto_comportamiento(self):
        moto = Motocicleta(1000)
        autobus = Autobus(5000)

        moto.agregar_acompanante(Persona("Ana"))
        autobus.agregar_pasajero(Persona("Pedro"))

        self.assertIn("Ana", str(moto))
        self.assertIn("Pedro", str(autobus))

    def test_cambiar_chofer_polimorfico(self):
        moto = Motocicleta(1000)
        autobus = Autobus(5000)

        moto.asignar_chofer(Persona("Juan"))
        autobus.asignar_chofer(Persona("Pedro"))

        moto.cambiar_chofer(Persona("Ana"))
        autobus.cambiar_chofer(Persona("Carlos"))

        self.assertIn("Chofer: Ana", str(moto))
        self.assertIn("Chofer: Carlos", str(autobus))


if __name__ == "__main__":
    unittest.main()
