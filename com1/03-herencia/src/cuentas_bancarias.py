from __future__ import annotations

from abc import ABC, abstractmethod


class Cuenta(ABC):
    def __init__(self, dni):
        self.__dni = dni
        self._saldo = 0

    @property
    def dni(self):
        return self.dni

    def depositar(self, monto: float) -> None:
        if monto < 100:
            raise ValueError("El monto debe ser mayor o igual a 100")
        self._saldo += monto

    @abstractmethod
    def extraer(self, monto: float) -> float:
        pass

    @property
    def saldo(self) -> float:
        return self._saldo

    @abstractmethod
    def dinero_disponible(self) -> float:
        pass

    def transferir(self, cuenta_destino: Cuenta, monto: float) -> None:
        if monto < 100:
            raise ValueError("El monto debe ser mayor o igual a 100")
        cuenta_destino.depositar(self.extraer(monto))


class CajaDeAhorro(Cuenta):
    def __init__(self, dni):
        super().__init__(dni)
        self.__reserva = 0

    def extraer(self, monto: float) -> float:
        if monto < 100:
            raise ValueError("El monto debe ser mayor o igual a 100")
        if self._saldo >= monto:
            self._saldo -= monto
            return monto
        return 0.00

    def reservar(self, monto) -> None:
        if monto < 100:
            raise ValueError("El monto debe ser mayor o igual a 100")
        if monto > self.saldo:
            return
        self._saldo -= monto
        self.__reserva += monto

    def dinero_disponible(self) -> float:
        return self.saldo + self.__reserva


class CuentaCorriente(Cuenta):
    def __init__(self, dni, descubierto):
        super().__init__(dni)
        self.__descubierto = descubierto

    def extraer(self, monto) -> float:
        if monto < 100:
            raise ValueError("El monto debe ser mayor o igual a 100")
        if self.dinero_disponible() >= monto:
            self._saldo -= monto
            return monto
        return 0.00

    def dinero_disponible(self) -> float:
        return self.saldo + self.__descubierto


def main():

    canuto = CajaDeAhorro(1234)
    cajita = CajaDeAhorro(2345)
    print(canuto.saldo)
    canuto.depositar(100000)
    print(canuto.saldo)
    canuto.extraer(5000)
    print(canuto.saldo)
    canuto.reservar(20000)
    print(canuto.saldo)

    canuto.transferir(cajita, 30000)
    print(canuto.saldo, cajita.saldo)

    cc = CuentaCorriente(444, 500.00)
    cc.depositar(1000)
    cc.extraer(500)
    print(cc.saldo, "500")
    cc.extraer(800)
    print(cc.saldo, "-300")
    cc.extraer(200)
    print(cc.saldo, "-500.00")


if __name__ == "__main__":
    main()
