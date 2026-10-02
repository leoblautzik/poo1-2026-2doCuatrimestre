from abc import ABC, abstractmethod


class Vehiculo(ABC):
    def __init__(self, id, capacidad_maxima, energia_maxima, consumo):
        self.id = id
        self.__capacidad_maxima = capacidad_maxima
        self.__energia_maxima = energia_maxima
        self.__energia_actual = energia_maxima
        self.__consumo_por_km = consumo

    def autonomia(self) -> float:
        return self.__energia_actual / self.__consumo_por_km

    def puede_realizar_viaje(self, distancia, pasajeros) -> bool:
        return (
            1 <= pasajeros <= self.__capacidad_maxima and self.autonomia() >= distancia
        )

    def realizar_viaje(self, distancia, pasajeros):
        if self.puede_realizar_viaje(distancia, pasajeros):
            self.__energia_actual -= self.__consumo_por_km * distancia

    @abstractmethod
    def calcular_costo(self, distancia, pasajeros):
        pass

    def recargar(self):
        self.__energia_actual = self.__energia_maxima


class Colectivo(Vehiculo):
    def __init__(self, id):
        super().__init__(id, capacidad_maxima=40, energia_maxima=50, consumo=2)

    def calcular_costo(self, distancia, pasajeros):
        if not self.puede_realizar_viaje(distancia, pasajeros):
            raise RuntimeError("No se puede realizar el viaje")
        return distancia * 500

    def __str__(self) -> str:
        return f"{self.__class__.__name__} Autonomía: {self.autonomia()}"


class Taxi(Vehiculo):
    def __init__(self, id):
        super().__init__(id, capacidad_maxima=4, energia_maxima=100, consumo=1)

    def calcular_costo(self, distancia, pasajeros):
        if not self.puede_realizar_viaje(distancia, pasajeros):
            raise RuntimeError("No se puede realizar el viaje")
        return 1000 + distancia * 700

    def __str__(self) -> str:
        return f"{self.__class__.__name__} Autonomía: {self.autonomia()}"


class BicicletaElectrica(Vehiculo):
    def __init__(self, id):
        super().__init__(id, capacidad_maxima=1, energia_maxima=100, consumo=2)

    def calcular_costo(self, distancia, pasajeros):
        if not self.puede_realizar_viaje(distancia, pasajeros):
            raise RuntimeError("No se puede realizar el viaje")
        return distancia * 300

    def __str__(self) -> str:
        return f"{self.__class__.__name__} Autonomía: {self.autonomia()}"


class Van(Vehiculo):
    def __init__(self, id):
        super().__init__(id, capacidad_maxima=8, energia_maxima=80, consumo=3)

    def calcular_costo(self, distancia, pasajeros):
        if not self.puede_realizar_viaje(distancia, pasajeros):
            raise RuntimeError("No se puede realizar el viaje")
        plus = 0.0
        if pasajeros > 5:
            plus = 0.2
        return (distancia * 900) * (1 + plus)

    def __str__(self) -> str:
        return f"{self.__class__.__name__} Autonomía: {self.autonomia()}"


def main():

    bondi = Colectivo("239")
    bondi.realizar_viaje(20, 5)
    print(bondi)

    taxi = Taxi("Taxi")
    taxi.realizar_viaje(100, 2)
    print(taxi)

    taxi.recargar()
    print(taxi)
    bici = BicicletaElectrica("E-Bike")
    print(bici.puede_realizar_viaje(50, 2))


if __name__ == "__main__":
    main()
