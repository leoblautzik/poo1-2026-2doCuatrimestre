from abc import ABC


class Fax:
    def enviar_fax(self):
        print("Estoy enviando un fax")


class Fotocopiadora:
    def fotocopiar(self):
        print("Estoy fotocopiando")


class ImpresoraMultifuncion(ABC):
    def imprimir(self):
        print(f"{self.__class__.__name__} Imprimiendo")

    def cancelar(self):
        print(f"{self.__class__.__name__} Cancelando Trabajos de impresion")

    def escanear(self):
        print(f"{self.__class__.__name__} Escaneando")


class ImpresoraModelo1998(ImpresoraMultifuncion):
    def __init__(self) -> None:
        self.__fax = Fax()

    def enviar_fax(self):
        self.__fax.enviar_fax()


class ImpresoraModelo2000(ImpresoraMultifuncion):
    pass


class ImpresoraModelo2014(ImpresoraModelo1998):
    def __init__(self) -> None:
        super().__init__()
        self.__fotocopiadora = Fotocopiadora()

    def fotocopiar(self):
        self.__fotocopiadora.fotocopiar()


def main():

    impreMFconFax = ImpresoraModelo1998()
    impreMFconFax.imprimir()
    impreMFconFax.cancelar()
    impreMFconFax.escanear()
    impreMFconFax.enviar_fax()

    impConFaxFotocopiadora = ImpresoraModelo2014()
    impConFaxFotocopiadora.enviar_fax()
    impConFaxFotocopiadora.fotocopiar()


if __name__ == "__main__":
    main()
