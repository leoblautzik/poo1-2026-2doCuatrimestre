class LeerNombres:
    def __init__(self) -> None:
        self.nombres: list[str] = []

    def leer_nombres(self, archivo):
        with open(archivo, "r") as n:
            for cada_nombre in n:
                self.nombres.append(cada_nombre.strip())

    def mostrar_nobres(self):
        for cada_nombre in self.nombres:
            print(cada_nombre)

    def cuantos_nombres(self) -> int:
        return len(self.nombres)

    def nombres_mas_largos(self) -> tuple[list[str], int]:
        tuplita = ([], 0)
        if len(self.nombres) == 0:
            return tuplita

        len_max = len(self.nombres[0])
        for cada_nombre in self.nombres:
            len_max = max(len_max, len(cada_nombre))

        lista_largos = []

        for cada_nombre in self.nombres:
            if len(cada_nombre) == len_max:
                lista_largos.append(cada_nombre)

        return (lista_largos, len_max)

    def comienzan_con(self, letra: str) -> tuple[list[str], int]:
        letra = letra.upper()
        lista_filtrada = []
        for n in self.nombres:
            if n[0].upper() == letra:
                lista_filtrada.append(n)

        return (lista_filtrada, len(lista_filtrada))

    def nombres_que_contienen(self, cadenita: str) -> tuple[list[str], int]:
        cadenita = cadenita.lower()
        lista_filtrada = []
        for n in self.nombres:
            if cadenita in n.lower():
                lista_filtrada.append(n)

        return (lista_filtrada, len(lista_filtrada))

    def guardar_ordenados(self, archivo):
        nombres_ordenados = sorted(self.nombres)
        with open(archivo, "w") as no:
            for n in nombres_ordenados:
                no.writelines(n + "\n")

    def guardar_resultados(self, archivo):
        """Nombre(s) más largo(s): Carlos, Miguel
        Nombres que comienzan con 'A': Ana
        Nombres que contienen 'an': Ana
        Cantidad total de nombres: 10
        Cantidad que comienzan con 'A': 1
        Cantidad que contienen 'an': 1
        Lista ordenada alfabéticamente:
        Ana, Carlos, Elena, Jorge, Luis, Lucía, María, Miguel, Pedro, Sofía
        """

        with open(archivo, "w") as r:
            r.write(f"Nombres más largos:  {self.nombres_mas_largos()} \n")
            r.write(f'Nombres que comienzan con "A": {self.comienzan_con("a")}\n')
            r.write(f"Cantidad total de nombres: {self.cuantos_nombres()}")


def main():
    aulita = LeerNombres()
    aulita.leer_nombres("nombres.txt")
    # aulita.mostrar_nobres()
    print(aulita.cuantos_nombres())
    print(aulita.nombres_mas_largos())
    print(aulita.comienzan_con("A"))
    aulita.guardar_ordenados("nombres_ordenados.out")
    aulita.guardar_resultados("resultados.txt")


if __name__ == "__main__":
    main()
