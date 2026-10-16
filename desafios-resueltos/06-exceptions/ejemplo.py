def divide():
    try:
        op1 = int(input("Nu 1: "))
        op2 = int(input("Num 2: "))
        print("La división es " + str(op1 / op2))
    except ValueError:
        print("Valores incorrectos")
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
    finally:
        print("Cálculo finalizado")


def main():
    divide()


if __name__ == "__main__":
    main()
