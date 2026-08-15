def invertir_cadena(cadena):
    invertida = ""
    for cada_letra in cadena:
        invertida = cada_letra + invertida

    return invertida

def es_palindromo(cadena):


def main():
    frase = input("Ingrese una frase: ")
    print(invertir_cadena(frase))


if __name__ == "__main__":
    main()
