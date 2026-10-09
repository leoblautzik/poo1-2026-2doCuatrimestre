class Venta:
    """<codigo_producto>,<descripcion>,<categoria>,<precio_unitario>,<cantidad_vendida>,<vendedor>"""

    def __init__(
        self,
        codigo,
        descripcion,
        categoria,
        precio_unitario,
        cantidad_vendida,
        vendedor,
    ) -> None:
        self.codigo = codigo
        self.descripcion = descripcion
        self.categoria = categoria
        self.precio_unitario: float = precio_unitario
        self.cantidad_vendida: int = cantidad_vendida
        self.vendedor = vendedor

    def __repr__(self):
        return f"{self.codigo}, {self.descripcion}, {self.categoria}, {self.precio_unitario}, {self.cantidad_vendida}, {self.vendedor} Total venta: {self.monto_venta()}"

    def monto_venta(self):
        return self.cantidad_vendida * self.precio_unitario


class Empresa:
    def __init__(self):
        self.__ventas: list[Venta] = []

    def leer_ventas(self, archivo):

        with open(archivo, "r") as mis_ventas:
            for cada_linea in mis_ventas:
                datos = cada_linea.strip().split(",")
                venta = Venta(
                    datos[0],
                    datos[1],
                    datos[2],
                    float(datos[3]),
                    int(datos[4]),
                    datos[5],
                )
                self.__ventas.append(venta)

        mis_ventas.close()

    def mostrar_ventas(self):
        for cada_venta in self.__ventas:
            print(cada_venta)

    def total_general_ventas(self) -> float:
        total = 0
        for cada_venta in self.__ventas:
            total += cada_venta.monto_venta()

        return total

    def cantidad_vendida_producto(self) -> dict[str, int]:
        aux: dict[str, int] = {}

        for cada_venta in self.__ventas:
            # if cada_venta.codigo in aux:
            #     cantidad_vendida = aux[cada_venta.codigo]
            # else:
            #     cantidad_vendida = 0
            cantidad_vendida = aux.get(cada_venta.codigo, 0)

            cantidad_vendida += cada_venta.cantidad_vendida
            aux[cada_venta.codigo] = cantidad_vendida

        return aux

    def producto_mas_vendido(self):
        lista_mas_vendidos = []
        vpp = self.cantidad_vendida_producto()

        cantidades = vpp.values()
        maxima_cantidad_vendida = max(cantidades)

        for k, v in vpp.items():
            if v == maxima_cantidad_vendida:
                lista_mas_vendidos.append((k, v))

        return lista_mas_vendidos

    def ventas_por_vendedor(self) -> dict[str, float]:
        aux: dict[str, float] = {}

        for cada_venta in self.__ventas:
            monto = aux.get(cada_venta.vendedor, 0.0)
            monto += cada_venta.monto_venta()
            aux[cada_venta.vendedor] = monto

        return aux

    def vendedor_estrella(self):
        diccionario = self.ventas_por_vendedor()
        vendedor, monto = max(diccionario.items(), key=lambda par: par[1])
        return (vendedor, monto)


def main():
    acme_informatica = Empresa()
    acme_informatica.leer_ventas("ventas.txt")
    # acme_informatica.mostrar_ventas()
    # print("Total de ventas: ", acme_informatica.total_general_ventas())
    # print(acme_informatica.cantidad_vendida_producto())
    print(acme_informatica.producto_mas_vendido())
    print(acme_informatica.ventas_por_vendedor())
    print(acme_informatica.vendedor_estrella())


if __name__ == "__main__":
    main()
