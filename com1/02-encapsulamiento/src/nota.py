from functools import total_ordering


@total_ordering
class Nota:
    def __init__(self, valor_nota) -> None:
        if valor_nota < 1 or valor_nota > 10:
            raise ValueError("Nota fuera de rango")
        self.__valor = valor_nota

    @property
    def valor(self):
        return self.__valor

    # No es correcto en el contexto de una Nota cambiarla sin recuperar
    # @valor.setter no se implementa

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

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, value: object, /) -> bool:
        if not isinstance(value, Nota):
            return NotImplemented
        return self.__valor == value.__valor

    def __lt__(self, value: object, /) -> bool:
        if not isinstance(value, Nota):
            return NotImplemented
        return self.__valor < value.__valor


def main():
    nota_matias = Nota(10)
    nota_laurita = Nota(2)
    nota_pedro = Nota(8)
    nota_luis = Nota(8)
    nota_ana = Nota(2)
    nota_benancio = Nota(5)

    notas = [nota_matias, nota_laurita, nota_pedro, nota_luis, nota_ana, nota_benancio]
    print(notas)
    print(sorted(notas))


if __name__ == "__main__":
    main()
