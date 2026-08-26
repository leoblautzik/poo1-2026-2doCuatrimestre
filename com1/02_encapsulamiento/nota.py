class Nota:
    def __init__(self, valor_nota) -> None:
        if valor_nota < 1 or valor_nota > 10:
            raise ValueError("Nota fuera de rango")
        self.__valor = valor_nota

    @property
    def valor(self):
        return self.__valor

    # No es correcto en el contexto de una Nota cambiarla sin recuperar
    # @valor.setter
    # def valor(self, nuevo_valor):
    #     if nuevo_valor < 1 or nuevo_valor > 10:
    #         raise ValueError("Nota fuera de rango")
    #     self.__valor = nuevo_valor

    def aprobada(self):
        return self.__valor >= 4

    def reprobada(self):
        return self.__valor < 4

    def promociona(self):
        return self.__valor >= 7

    def regulariza(self):
        return self.aprobada() and not self.promociona()

    def recupera(self, nuevo_valor):
        if nuevo_valor < 1 or nuevo_valor > 10:
            raise ValueError("Nota fuera de rango")
        self.__valor = max(self.__valor, nuevo_valor)

    def __str__(self) -> str:
        return f"Nota: {self.__valor}"


def main():
    nota_matias = Nota(6)
    print(f"Esta aprobada: {nota_matias.aprobada()}")
    print(f"Esta reprobada: {nota_matias.reprobada()}")
    print(f"Esta promocinada: {nota_matias.promociona()}")
    print(nota_matias)

    nota_pepe = Nota(2)
    print(f"Esta aprobada: {nota_pepe.aprobada()}")
    print(f"Esta reprobada: {nota_pepe.reprobada()}")
    print(f"Esta promocinada: {nota_pepe.promociona()}")
    print(nota_pepe)

    print(nota_pepe.valor)


if __name__ == "__main__":
    main()
