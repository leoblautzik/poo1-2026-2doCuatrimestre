def busqueda_secuencial(lista: list[int], buscado: int) -> int:
    """
    Implementar la función: busquedaSecuencial(lista, valorBuscado)
    que recibe una lista de enteros y un valor a buscar, y devuelve la posición
    del valor buscado, o -1 si el valor no se encuentra
    """
    for i in range(len(lista)):
        if lista[i] == buscado:
            return i

    return -1


def busquedaSecuencialAlexis(lista, valorBuscado):
    i = 0
    while i < len(lista) and lista[i] != valorBuscado:
        i += 1

    if i < len(lista):
        return i
    else:
        return -1


def expand(num):
    result = ""
    cont = 1
    valor = num[0]
    # 111221
    for i in range(1, len(num)):
        if num[i] == valor:
            cont += 1
        else:
            result += str(cont)
            result += str(valor)
            valor = num[i]
            cont = 1
    result += str(cont)
    result += str(valor)
    return result


def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2

        if lista[medio] == objetivo:
            return medio
        elif objetivo > lista[medio]:
            inicio = medio + 1
        else:
            fin = medio - 1

    return -1


def factorial(n):
    if n < 0:
        raise ValueError("n debe ser mayor o igual a cero.")
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def main():
    # lista = [1, 2, 3, 4, -1, 5, 9]
    # print(busqueda_secuencial(lista, 5))
    # print(busqueda_secuencial(lista, 15))
    # print(busqueda_secuencial(lista, 1))
    # print(busqueda_secuencial(lista, 9))
    # expansivo = "1"
    # for i in range(10):
    #     print(expand(expansivo))
    #     expansivo = expand(expansivo)

    print(factorial(-5))


if __name__ == "__main__":
    main()
