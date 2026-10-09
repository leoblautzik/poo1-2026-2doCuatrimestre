class Producto:
    """Cada producto tiene:
    código, descripción, precio unitario y stock disponible.
    """

    def __init__(self, codigo, descripcion, precio, stock):
        self.codigo = codigo
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock

    def __repr__(self) -> str:
        return f"{self.codigo}, {self.descripcion}, {self.precio}"

    def __eq__(self, otro) -> bool:
        return self.codigo == otro.codigo

    def __hash__(self) -> int:
        return hash(self.codigo)


class Venta:
    """producto vendido (por código), su descripción, el precio unitario y la cantidad vendida."""

    def __init__(self, producto, descripcion, precio, cantidad):
        self.producto = producto
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = cantidad


class GestorProductos:
    def __init__(self) -> None:
        self.productos = []
        self.ventas = []

    def leer_productos(self, productos):

        with open(productos, "r") as p:
            for cada_linea in p:
                datos = cada_linea.strip().split(",")
                self.productos.append(
                    Producto(datos[0], datos[1], float(datos[2]), int(datos[3]))
                )

    def leer_ventas(self, ventas):
        with open(ventas, "r") as v:
            for cada_linea in v:
                datos = cada_linea.strip().split(",")
                self.ventas.append(
                    Venta(datos[0], datos[1], float(datos[2]), int(datos[3]))
                )


def main():

    gp = GestorProductos()
    gp.leer_productos("productos.csv")
    gp.leer_ventas("ventas.csv")
    print(gp.productos)
    print(gp.ventas)


if __name__ == "__main__":
    main()
