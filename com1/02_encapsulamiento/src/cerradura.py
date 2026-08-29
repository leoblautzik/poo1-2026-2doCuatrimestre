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
        self.__abierta = True
        self.__bloqueada = False

    def esta_abierta(self) -> bool:
        return self.__abierta

    def esta_cerrada(self) -> bool:
        return not self.esta_abierta()

    def esta_bloqueada(self) -> bool:
        return self.__bloqueada

    def abrir(self, clave):
        pass


def main():
    trabex = Cerradura(1234, 3)
    print(trabex.esta_abierta())


if __name__ == "__main__":
    main()
