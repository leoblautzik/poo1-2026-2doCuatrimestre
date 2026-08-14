"""
Leer tres valores numéricos enteros,
indicar cual es el mayor, cuál es el del medio y cuál el menor.
Considerar que los tres valores son diferentes
"""
def mayor_medio_menor(a, b ,c):

    mayor = a

    if b > mayor:
        medio = mayor
        mayor = b

    else:
        medio = b

    if c > mayor:
        menor = medio
        medio = mayor
        mayor = c

    elif c > medio:
        menor = medio
        medio = c

    else:
        menor = c

    print("Mayor:", mayor, "Medio:", medio, "Menor:", menor)


def main():

    # a = int(input("Ingrese un entero: "))
    # b = int(input("Ingrese otro entero: "))
    # c = int(input("Ingrese otro entero mas: "))

    mayor_medio_menor(1,2,3)
    mayor_medio_menor(1,3,2)
    mayor_medio_menor(2,1,3)
    mayor_medio_menor(2,3,1)
    mayor_medio_menor(3,2,1)
    mayor_medio_menor(3,1,2)
    


if __name__ == "__main__":
    main()
