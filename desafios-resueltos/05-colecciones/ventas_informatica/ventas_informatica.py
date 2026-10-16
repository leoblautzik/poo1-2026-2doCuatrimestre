class LineaMalitaException(Exception):
    pass


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
        if precio_unitario <= 0:
            raise ValueError
        self.precio_unitario: float = precio_unitario
        if cantidad_vendida <= 0:
            raise ValueError
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
        with open(archivo, "r") as v:
            for cada_linea in v:
                try:
                    datos = cada_linea.strip().split(",")
                    if len(datos) != 6:
                        raise LineaMalitaException()
                    venta = Venta(
                        datos[0],
                        datos[1],
                        datos[2],
                        float(datos[3]),
                        int(datos[4]),
                        datos[5],
                    )
                    self.__ventas.append(venta)
                except LineaMalitaException:
                    print("Hay una linea malita")
                except ValueError:
                    print("Formato de datos incorrecto")
        v.close()

    def mostrar_ventas(self):
        for venta in self.__ventas:
            print(venta)

    def total_general_ventas(self) -> float:
        total = 0
        for venta in self.__ventas:
            total += venta.monto_venta()

        return total

    def ventas_por_vendedor(self) -> dict[str, float]:
        dic_out: dict[str, float] = {}

        for cada_venta in self.__ventas:
            monto_acumulado = (
                dic_out.get(cada_venta.vendedor, 0) + cada_venta.monto_venta()
            )
            dic_out[cada_venta.vendedor] = monto_acumulado

        return dic_out

    def cantidad_vendida_producto(self) -> dict[str, int]:
        dict_out: dict[str, int] = {}

        for cada_venta in self.__ventas:
            acumulado = dict_out.get(cada_venta.codigo, 0) + cada_venta.cantidad_vendida
            dict_out[cada_venta.codigo] = acumulado

        return dict_out

    def producto_mas_vendido(self) -> tuple[int, list[str]]:
        lista = []
        dic = self.cantidad_vendida_producto()

        maxima_cantidad_vendida = max(dic.values())

        for k, v in dic.items():
            if v == maxima_cantidad_vendida:
                lista.append(k)

        return maxima_cantidad_vendida, lista


def main():
    acme_informatica = Empresa()
    acme_informatica.leer_ventas("ventas.txt")
    acme_informatica.mostrar_ventas()
    print("Total de ventas: ", acme_informatica.total_general_ventas())
    print(acme_informatica.cantidad_vendida_producto())
    print(acme_informatica.producto_mas_vendido())
    print(acme_informatica.ventas_por_vendedor())
    # print(acme_informatica.vendedor_estrella())


if __name__ == "__main__":
    main()
