from __future__ import annotations

import math
from functools import total_ordering


@total_ordering
class Punto:
    def __init__(self, x, y) -> None:
        self.__x = x
        self.__y = y

    def esta_sobre_eje_x(self) -> bool:
        return self.__y == 0

    def esta_sobre_eje_y(self) -> bool:
        return self.__x == 0

    def es_origen_coordenadas(self):
        return self.esta_sobre_eje_x() and self.esta_sobre_eje_y()

    def distancia_al_origen(self):
        return self.distancia(Punto(0, 0))

    def distancia(self, otro_punto: Punto) -> float:
        return math.hypot(self.__x - otro_punto.__x, self.__y - otro_punto.__y)

    def __eq__(self, value: object, /) -> bool:
        if not isinstance(value, Punto):
            return NotImplemented
        return (self.__x, self.__y) == (value.__x, value.__y)

    def __lt__(self, value: object, /) -> bool:
        if not isinstance(value, Punto):
            return NotImplemented
        return (self.__x, self.__y) < (value.__x, value.__y)


def main():
    p1 = Punto(3, 4)
    print(p1.distancia_al_origen())

    p2 = Punto(1, 1)
    p3 = Punto(4, 5)

    print(p2.distancia(p3))
    print(p3.distancia(p2))


if __name__ == "__main__":
    main()
