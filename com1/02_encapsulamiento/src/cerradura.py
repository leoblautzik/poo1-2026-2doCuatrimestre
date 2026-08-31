"""
Cerradura
Cuando una Cerradura se bloquea no puede volver a abrirse nunca más
class Cerradura {
   public Cerradura(int claveDeApertura,int cantidadDeFallosConsecutivosQueLaBloquean)
   public boolean abrir(int clave)
   public void cerrar()
   public boolean estaAbierta()
   public boolean estaCerrada()
   public boolean fueBloqueada()
   public int contarAperturasExitosas()
   public int contarAperturasFallidas()
}
"""


class Cerradura:
    def __init__(self, clave, cfcqlb) -> None:
        self.__clave = clave
        self.__cfcqlb = cfcqlb
        self.__abierta = False
        self.__bloqueada = False
        self.__aperturas_exitosas = 0
        self.__aperturas_fallidas = 0
        self.__fallos_consecutivos = 0

    def esta_abierta(self) -> bool:
        return self.__abierta

    def esta_cerrada(self) -> bool:
        return not self.esta_abierta()

    def esta_bloqueada(self) -> bool:
        return self.__bloqueada

    def fue_bloqueada(self) -> bool:
        return self.__bloqueada

    def contar_aperturas_exitosas(self) -> int:
        return self.__aperturas_exitosas

    def contar_aperturas_fallidas(self) -> int:
        return self.__aperturas_fallidas

    def abrir(self, clave) -> bool:
        if self.fue_bloqueada():
            raise RuntimeError("La cerradura fue bloqueada")
        if self.esta_abierta():
            raise RuntimeError("La cerradura esta abierta")

        if clave == self.__clave:
            self.__aperturas_exitosas += 1
            self.__abierta = True
            self.__fallos_consecutivos = 0
            return True
        else:
            self.__aperturas_fallidas += 1
            self.__fallos_consecutivos += 1
            if self.__fallos_consecutivos == self.__cfcqlb:
                self.__bloqueada = True
            return False

    def cerrar(self) -> None:
        if self.fue_bloqueada():
            raise RuntimeError("La cerradura fue bloqueada")
        if self.esta_cerrada():
            raise RuntimeError("La cerradura esta cerrada")
        self.__abierta = False


def main():
    trabex = Cerradura(1234, 3)
    print(trabex.esta_cerrada())


if __name__ == "__main__":
    main()
