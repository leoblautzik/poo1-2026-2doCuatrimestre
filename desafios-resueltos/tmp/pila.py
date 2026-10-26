class PilaVaciaException(Exception):
    pass


class Pila:
    def __init__(self) -> None:
        self.__pila = []

    def apilar(self, e):
        self.__pila.append(e)

    def desapilar(self):
        if self.esta_vacia():
            raise PilaVaciaException
        return self.__pila.pop()

    def ver_tope(self):
        if self.esta_vacia():
            raise PilaVaciaException
        return self.__pila[len(self.__pila) - 1]

    def esta_vacia(self):
        return len(self.__pila) == 0


class Teletipo:
    def __init__(self) -> None:
        self.__pila = Pila()

    def procesar(self, cadena):
        for letra in cadena:
            if letra != "/" and letra != "&":
                self.__pila.apilar(letra)
            elif letra == "/":
                if not self.__pila.esta_vacia():
                    self.__pila.desapilar()
            elif letra == "&":
                while not self.__pila.esta_vacia():
                    self.__pila.desapilar()
        s = ""
        while not self.__pila.esta_vacia():
            s = self.__pila.desapilar() + s

        return s


def main():
    teletipo = Teletipo()
    print(teletipo.procesar("abc/d//e"))
    print(teletipo.procesar(""))
    print(teletipo.procesar("////aeiou"))
    print(teletipo.procesar("////aeiou&-"))
    print(teletipo.procesar("a/b/c/d/-"))
    print(teletipo.procesar("&a/b/c/d/-"))


if __name__ == "__main__":
    main()
