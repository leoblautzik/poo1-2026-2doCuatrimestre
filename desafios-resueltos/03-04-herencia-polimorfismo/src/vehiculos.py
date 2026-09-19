class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre

    def __str__(self):
        return self.__nombre

    def __repr__(self) -> str:
        return self.__str__()


class Vehiculo:
    def __init__(self, kilometros):
        self.__kilometros = kilometros
        self.__chofer = None

    def asignar_chofer(self, chofer):
        if self.__chofer is not None:
            raise RuntimeError("Ya hay un chofer asignado")
        self.__chofer = chofer

    def cambiar_chofer(self, chofer):
        if self.__chofer is None:
            raise RuntimeError("No hay chofer asignado")
        self.__chofer = chofer

    def __str__(self) -> str:
        return f"Chofer: {self.__chofer}, Kilometraje: {self.__kilometros}"


class Motocicleta(Vehiculo):
    def __init__(self, kilometros):
        super().__init__(kilometros)
        self.__acompanante = None

    def agregar_acompanante(self, persona):
        if self.__acompanante is not None:
            raise RuntimeError("La motocicleta ya tiene un acompañante")
        self.__acompanante = persona
        print("Acompañante agregado.")

    def cambiar_chofer(self, chofer):
        if self.__acompanante is not None:
            raise RuntimeError(
                "No se puede cambiar de chofer con un acompañante a bordo"
            )
        super().cambiar_chofer(chofer)
        print("Chofer cambiado.")

    def __str__(self) -> str:
        return f"{__class__.__name__} -> {super().__str__()}, Acompañante: {self.__acompanante} "


class Autobus(Vehiculo):
    def __init__(self, kilometros):
        super().__init__(kilometros)
        self.__pasajeros = []

    def agregar_pasajero(self, persona):
        self.__pasajeros.append(persona)
        print("Pasajero agregado.")

    def cambiar_chofer(self, chofer):
        if len(self.__pasajeros) != 0:
            raise RuntimeError("No se puede cambiar de chofer con pasajeros a bordo")
        super().cambiar_chofer(chofer)

    def __str__(self) -> str:
        return f"{__class__.__name__} -> {super().__str__()}, Pasajeros: {self.__pasajeros} "


def main():
    # Creamos personas

    juan = Persona("Juan")
    ana = Persona("Ana")
    pedro = Persona("Pedro")
    maria = Persona("Maria")
    carlos = Persona("Carlos")

    # Creamos vehículos

    moto = Motocicleta(1000)
    colectivo = Autobus(5000)

    # Asignamos choferes

    moto.asignar_chofer(juan)
    colectivo.asignar_chofer(pedro)

    # Agregamos acompañante a la moto

    moto.agregar_acompanante(ana)

    # Agregamos pasajeros al colectivo

    colectivo.agregar_pasajero(maria)
    colectivo.agregar_pasajero(carlos)

    # Intentamos cambiar choferes

    # moto.cambiar_chofer(Persona("Luis"))
    # colectivo.cambiar_chofer(Persona("Roberto"))

    print(moto)
    print(colectivo)


if __name__ == "__main__":
    main()
