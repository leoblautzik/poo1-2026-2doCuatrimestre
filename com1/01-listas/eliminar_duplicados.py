"""
Eliminar elementos duplicados de una lista
"""


def eliminar_duplicados(lista):
    nueva_lista = []
    for elem in lista:
        if not elem in nueva_lista:
            nueva_lista.append(elem)
    return nueva_lista


def elementos_unicos(lista):
    """
    Determinar si todos los elementos de una lista son únicos
    """
    return len(lista) == len(eliminar_duplicados(lista))


def esta_ordenada(lista: list[int]) -> bool:
    """
    Escribir una función que reciba una lista de enteros
    y devuelva true si la lista está ordenada de mayor a
    menor y false si está desordenada
    """
    for i in range(len(lista) - 1):
        if lista[i] < lista[i + 1]:
            return False
    return True


def main():
    con_repetidos = [23, 11, 23, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 21, 5]
    sin_dupplicados = eliminar_duplicados(con_repetidos)
    print(sin_dupplicados)

    unicos = ["a", "e", "i", "o", "u"]
    print(elementos_unicos(unicos))

    no_unicos = ["a", "e", "i", "o", "u", "a"]
    print(elementos_unicos(no_unicos))

    ordenado = [12, 11, 3, 0, -4]
    desordenado = [12, 11, 3, 7, -4]

    print(esta_ordenada(ordenado))
    print(esta_ordenada(desordenado))

    print(esta_ordenada([]))
    print(esta_ordenada([1]))

    variadita = [1, "a", "Fruta", "queso", [1, 2]]
    # print(esta_ordenada(variadita))


if __name__ == "__main__":
    main()
