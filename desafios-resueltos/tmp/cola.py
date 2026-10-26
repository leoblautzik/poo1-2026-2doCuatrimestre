from collections import deque
from typing import Generic, TypeVar

T = TypeVar("T")


class ColaVaciaException(Exception):
    pass


class Cola(Generic[T]):
    def __init__(self) -> None:
        self.__cola = deque[T]()

    def encolar(self, e: T):
        self.__cola.append(e)

    def desencolar(self) -> T:
        if self.esta_vacia():
            raise ColaVaciaException
        return self.__cola.popleft()

    def ver_primero(self) -> T:
        if self.esta_vacia():
            raise ColaVaciaException
        return self.__cola.popleft()

    def esta_vacia(self) -> bool:
        return len(self.__cola) == 0


cola__de_enteros = Cola[int]()
cola_de_personas = Cola[Persona]()
