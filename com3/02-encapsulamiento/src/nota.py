class Nota:
    def __init__(self, valor_inicial) -> None:
        if valor_inicial < 0 or valor_inicial > 10:
            raise ValueError("Nota inválida")

        self.__valor_nota = valor_inicial

    def obtener_valor(self):
        return self.__valor_nota

    def aprobado(self):
        return self.__valor_nota >= 4

    def desaprobado(self):
        return not self.aprobado()

    def recuperar(self, nueva_nota):
        if nueva_nota < 0 or nueva_nota > 10:
            raise ValueError("Nota inválida")

        self.__valor_nota = max(self.__valor_nota, nueva_nota)


def main():
    nota_carlitos = Nota(5)
    nota_laurita = Nota(2)

    print(nota_carlitos.obtener_valor())
    print(nota_laurita.obtener_valor())

    print(nota_carlitos.aprobado())
    print(nota_laurita.aprobado())

    print(nota_carlitos.desaprobado())
    print(nota_laurita.desaprobado())

    nota_laurita.recuperar(-4)
    print(nota_laurita.aprobado())


if __name__ == "__main__":
    main()
