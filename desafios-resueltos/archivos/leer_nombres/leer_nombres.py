class LeerNombres:
    def __init__(self) -> None:
        self.__nombres: list[str] = []

    def leer_nombres(self, archivo):
        with open(archivo, "r", encoding="utf-8") as archi_nombres:
            for cada_nombre in archi_nombres:
                self.__nombres.append(cada_nombre.strip())

    def monstrar_nombres(self):
        for n in self.__nombres:
            print(n)

    def contar_nombres(self):
        return len(self.__nombres)

    def nombres_mas_largos(self) -> tuple[list[str], int]:

        largo_max = len(self.__nombres[0])
        lista_nombres_largos: list[str] = []

        for nombre in self.__nombres:
            largo_max = max(largo_max, len(nombre))

        for nombre in self.__nombres:
            if len(nombre) == largo_max:
                lista_nombres_largos.append(nombre)

        return lista_nombres_largos, largo_max

    def filtrar_por_letra(self, letra):
        contador = 0
        lista = []

        for nombre in self.__nombres:
            if nombre[0].lower() == letra.lower():
                lista.append(nombre)
                contador += 1

        return lista, contador


def main():

    lector = LeerNombres()
    lector.leer_nombres("nombres.txt")
    lector.monstrar_nombres()
    print(lector.contar_nombres())
    print(lector.nombres_mas_largos())
    print(lector.filtrar_por_letra("A"))


if __name__ == "__main__":
    main()
