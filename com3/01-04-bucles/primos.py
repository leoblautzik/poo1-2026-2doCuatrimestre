"""
Escribir un programa que pida al usuario un número entero y
muestre por pantalla si es un número primo o no
"""


def es_primo(n):
    if n < 2:
        raise ValueError("n debe ser mayor que 1")

    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def main():
    print(es_primo(2))
    print(es_primo(4))
    print(es_primo(12))
    print(es_primo(15))
    print(es_primo(17))
    print(es_primo(200000001))
    print(es_primo(121))

    aux = int(input("Hasta cual: "))

    for i in range(2, aux):
        if es_primo(i):
            print(i)


if __name__ == "__main__":
    main()
