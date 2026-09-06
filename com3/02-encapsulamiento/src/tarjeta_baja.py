"""
Modelar la class TarjetaBaja, se inicializa con un saldo inicial,
se puede recargar y consultar el saldo, si hay dinero suficiente,
pagar viajes en colectivo o subte, se pueden consultar cantidad de viajes en subte,
cant de viajes en colectivo y totales.
Viaje en colectivo: $21.50
Viaje en Subte: $19.50
"""


class TarjetaBaja:
    VIAJE_COLECTIVO = 21.50
    VIAJE_SUBTE = 19.5

    def __init__(self, saldo_inicial: float = 0) -> None:
        if saldo_inicial < 0:
            raise ValueError("El monto debe ser mayor a cero")
        self.__saldo = saldo_inicial
        self.__contador_viajes_colectivo = 0
        self.__contador_viajes_subte = 0

    def consultar_saldo(self) -> float:
        return self.__saldo

    def recargar(self, monto: float) -> None:
        if monto <= 0:
            raise ValueError("El monto debe ser mayor a cero")
        self.__saldo += monto

    def pagar_viaje_colectivo(self) -> None:
        if self.__saldo >= TarjetaBaja.VIAJE_COLECTIVO:
            self.__saldo -= TarjetaBaja.VIAJE_COLECTIVO
            self.__contador_viajes_colectivo += 1

    def pagar_viaje_subte(self) -> None:
        if self.__saldo >= TarjetaBaja.VIAJE_SUBTE:
            self.__saldo -= TarjetaBaja.VIAJE_SUBTE
            self.__contador_viajes_subte += 1

    def consultar_cuantos_viajes_colectivo(self):
        return self.__contador_viajes_colectivo

    def consultar_cuantos_viajes_subte(self):
        return self.__contador_viajes_subte

    def consultar_cuantos_viajes_totales(self):
        return self.__contador_viajes_colectivo + self.__contador_viajes_subte


def main():
    pass


if __name__ == "__main__":
    main()
