from __future__ import annotations

from enum import Enum


class CategoriaPlato(Enum):
    ENTRADA = 1
    PRINCIPAL = 2
    POSTRE = 3
    BEBIDA = 4


class Plato:
    def __init__(self, nombre: str, precio: float, categoria: CategoriaPlato) -> None:
        self.__nombre = nombre
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self.__precio = precio
        self.__categoria = categoria

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self.__precio = nuevo_precio

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, nueva_categoria):
        if not isinstance(nueva_categoria, CategoriaPlato):
            raise TypeError("Categoría inválida")
        self.__categoria = nueva_categoria

    def __str__(self) -> str:
        return f"{self.__categoria.name}, {self.__nombre}, {self.__precio:.2f}"


class Pedido:
    def __init__(self):
        self.__lista_platos: list[Plato] = []

    def agregar_plato(self, plato: Plato):
        self.__lista_platos.append(plato)

    def calcular_total(self):
        return sum(plato.precio for plato in self.__lista_platos)

    def ticket(self):
        s = ""
        s = "La Ponderosa Restaurante\n"
        for p in self.__lista_platos:
            s += str(p)
            s += "\n"

        s += "Total: " + str(self.calcular_total())
        s += "\n"

        print(s)


def main():
    # Platos
    empanadas = Plato("Empanadas de carne", 4500, CategoriaPlato.ENTRADA)
    bruschetta = Plato("Bruschetta", 3800, CategoriaPlato.ENTRADA)

    milanesa = Plato("Milanesa napolitana", 8500, CategoriaPlato.PRINCIPAL)
    ravioles = Plato("Ravioles de ricota", 9200, CategoriaPlato.PRINCIPAL)
    hamburguesa = Plato("Hamburguesa completa", 7800, CategoriaPlato.PRINCIPAL)

    flan = Plato("Flan con dulce de leche", 3500, CategoriaPlato.POSTRE)
    tiramisu = Plato("Tiramisú", 4200, CategoriaPlato.POSTRE)

    gaseosa = Plato("Gaseosa", 2200, CategoriaPlato.BEBIDA)
    agua = Plato("Agua mineral", 1800, CategoriaPlato.BEBIDA)

    # Crear un pedido
    pedido = Pedido()

    pedido.agregar_plato(empanadas)
    pedido.agregar_plato(milanesa)
    pedido.agregar_plato(flan)
    pedido.agregar_plato(gaseosa)

    pedido.ticket()

    otro_pedido = Pedido()
    otro_pedido.agregar_plato(ravioles)
    otro_pedido.agregar_plato(tiramisu)
    otro_pedido.agregar_plato(agua)

    otro_pedido.ticket()

    print(CategoriaPlato.ENTRADA.value)


if __name__ == "__main__":
    main()
