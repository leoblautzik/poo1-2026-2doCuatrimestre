from __future__ import annotations

import math


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
        # return math.sqrt(math.pow(self.__x, 2) + math.pow(self.__y, 2))
        # return math.hypot(self.__x, self.__y)
        return self.distancia(Punto(0, 0))

    def distancia(self, otro_punto: Punto) -> float:
        return math.hypot(self.__x - otro_punto.__x, self.__y - otro_punto.__y)


def main():
    p1 = Punto(3, 4)
    print(p1.distancia_al_origen())

    p2 = Punto(1, 1)
    p3 = Punto(4, 5)

    print(p2.distancia(p3))
    print(p3.distancia(p2))


if __name__ == "__main__":
    main()
