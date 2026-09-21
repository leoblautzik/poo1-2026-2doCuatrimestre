from __future__ import annotations

from abc import ABC, ABCMeta, abstractmethod


class Aguatero(metaclass=ABCMeta):
    @abstractmethod
    def recibir_agua(self):
        pass


class Unidad(ABC):
    def __init__(self, salud, danio, posicion):
        self.__salud = salud
        self.__danio = danio
        self.__posicion = posicion

    @property
    def salud(self):
        """Solo para testing"""
        return self.__salud

    @abstractmethod
    def puede_atacar(self, objetivo: Unidad) -> bool:
        pass

    @abstractmethod
    def atacar(self, objetivo):
        pass

    def recibir_ataque(self, atacante: Unidad):
        self.__salud -= atacante.__danio

    def esta_viva(self):
        return self.__salud > 0

    def distancia(self, objetivo: Unidad):
        return abs(self.__posicion - objetivo.__posicion)


class Soldado(Unidad, Aguatero):
    def __init__(self, posicion):
        super().__init__(salud=200, danio=10, posicion=posicion)
        self.__energia = 100

    @property
    def energia(self):
        """Solo para testing"""
        return self.__energia

    def puede_atacar(self, objetivo: Unidad) -> bool:
        """
        distancia == 0 y energía suficiente,
        no esta muerto, y el objetivo tampoco
        """
        return (
            self.distancia(objetivo) == 0
            and self.__energia >= 10
            and self.esta_viva()
            and objetivo.esta_viva()
        )

    def atacar(self, objetivo: Unidad):
        if self.puede_atacar(objetivo):
            objetivo.recibir_ataque(self)
            self.__energia -= 10

    def recibir_agua(self):
        self.__energia = 100


class Arquero(Unidad):
    def __init__(self, posicion):
        super().__init__(salud=50, danio=5, posicion=posicion)
        self.__flechas = 20

    @property
    def flechas(self):
        """Solo para testing"""
        return self.__flechas

    def puede_atacar(self, objetivo: Unidad) -> bool:
        """
        2 <= distancia <= 5
        flechas > 0
        no esta muerto y su objetivo tampoco
        """
        return (
            2 <= self.distancia(objetivo) <= 5
            and self.__flechas > 0
            and self.esta_viva()
            and objetivo.esta_viva()
        )

    def atacar(self, objetivo: Unidad):
        if self.puede_atacar(objetivo):
            self.__flechas -= 1
            objetivo.recibir_ataque(self)

    def recibir_flechas(self, cantidad=6):
        self.__flechas += cantidad


class Lancero(Unidad):
    def __init__(self, posicion):
        super().__init__(salud=150, danio=25, posicion=posicion)

    def puede_atacar(self, objetivo: Unidad) -> bool:
        """
        1 <= distancia <= 3
        no esta muerto y su objetivo tampoco
        """
        return (
            1 <= self.distancia(objetivo) <= 3
            and self.esta_viva()
            and objetivo.esta_viva()
        )

    def atacar(self, objetivo: Unidad):
        if self.puede_atacar(objetivo):
            objetivo.recibir_ataque(self)


class Caballero(Unidad, Aguatero):
    def __init__(self, posicion):
        super().__init__(salud=200, danio=50, posicion=posicion)
        self.__caballo = Caballo()

    def puede_atacar(self, objetivo: Unidad) -> bool:
        """
        1<= distancia<=2
        no esta muerto y su objetivo tampoco
        su caballo no esta rebelde
        """
        return (
            1 <= self.distancia(objetivo) <= 2
            and self.esta_viva()
            and objetivo.esta_viva()
            and not self.__caballo.esta_rebelde()
        )

    def atacar(self, objetivo: Unidad):
        if self.puede_atacar(objetivo):
            self.__caballo.contar_ataques()
            objetivo.recibir_ataque(self)

    def recibir_agua(self):
        self.__caballo.recibir_agua()


class Caballo(Aguatero):
    def __init__(self):
        self.__ataques_realizados = 0
        # self.__rebelde = False

    def recibir_agua(self):
        self.__ataques_realizados = 0

    def contar_ataques(self):
        if not self.esta_rebelde():
            self.__ataques_realizados += 1

    def esta_rebelde(self):
        return self.__ataques_realizados >= 3
