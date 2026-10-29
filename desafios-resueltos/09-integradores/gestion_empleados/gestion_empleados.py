import csv


class ErrorDatoInvalido(Exception):
    pass


class SectorInexistente(Exception):
    pass


class LineaMalFormada(Exception):
    pass


class Empleado:
    def __init__(self, nombre, sector, salario: float) -> None:
        self.nombre = nombre
        self.sector = sector
        self.salario: float = salario

    def __repr__(self) -> str:
        return f"{self.nombre}, {self.sector}, {self.salario:.2f}"


class GestionEmpleados:
    def __init__(self) -> None:
        self.empleados: list[Empleado] = []

    def cargar_empleados(self, file):
        """
        Debe leer el archivo file (empleados.csv) y crear una lista interna de objetos Empleado.
        Se debe manejar correctamente las siguientes situaciones mediante excepciones:
        Archivo no encontrado
        Líneas mal formateadas (por ejemplo, menos o más columnas de las esperadas)
        Salarios no numéricos (usar la excepción ErrorDatoInvalido)
        """
        try:
            with open(file, "r", encoding="utf8") as f:
                lector = csv.reader(f)
                # Omitido en el video. Se descarta la primer linea de encabezados.
                next(lector)
                for datos in lector:
                    try:
                        if len(datos) != 3:
                            raise LineaMalFormada()
                        nombre = datos[0]
                        sector = datos[1]
                        salario = float(datos[2])
                        e = Empleado(nombre, sector, salario)
                        self.empleados.append(e)
                    except LineaMalFormada:
                        print("Se ha encontrado una linea con formato incorrecto")
                    except ValueError:
                        print("Uno de los datos numéricos no puede ser convertido")

        except FileNotFoundError:
            print("Archivo no encontrado")

    def agrupar_por_sector(self) -> dict[str, list[Empleado]]:
        """
        Devuelve un diccionario donde la clave sea el sector y
        el valor, la lista de empleados de ese sector.
        """

        dic_sector: dict[str, list[Empleado]] = {}

        for e in self.empleados:
            k = e.sector
            lista_e = dic_sector.get(k, [])
            lista_e.append(e)
            dic_sector[k] = lista_e

        return dic_sector

    def sector_mayor_costo(self) -> tuple[str, float]:
        """
        Devuelve el nombre del sector cuyo total de sueldos
        (la suma de los salarios de sus empleados) sea mayor y el monto que paga en salarios.
        """
        aux = {}
        dic_sector = self.agrupar_por_sector()

        for sector, lista_e in dic_sector.items():
            total_salarios_sector = 0
            for e in lista_e:
                total_salarios_sector += e.salario
            aux[sector] = total_salarios_sector

        max_total_salarios = max(aux.values())

        sector_mayor_costo = ""

        for sector, total_salarios in aux.items():
            if total_salarios == max_total_salarios:
                sector_mayor_costo = sector

        return (sector_mayor_costo, max_total_salarios)

    def promedio_salarios(self, sector: str) -> float:
        """
        Devuelve el salario promedio de los empleados del sector indicado.
        Si el sector no existe, debe lanzar una excepción SectorInexistente.
        """
        dic_sector = self.agrupar_por_sector()
        try:
            if sector not in dic_sector:
                raise SectorInexistente()
            lista_e = dic_sector[sector]
            if len(lista_e) == 0:
                raise ValueError
            total = sum(e.salario for e in lista_e)
            return total / len(lista_e)

        except SectorInexistente:
            print("Sector inexistante")

        except ValueError:
            print("No se puede calcular el promedio")

        return 0.0

    def imprimir_sectores(self, file):
        """
        Escribe en el archivo sectores.txt un listado donde figura el sector y debajo
        la lista de empleados de ese sector(de a uno por linea)
        """
        dic_sector = self.agrupar_por_sector()

        with open(file, "w", encoding="utf-8") as out:
            for sector, lista_e in dic_sector.items():
                out.write("\n" + sector + "\n")
                out.writelines(str(e) + "\n" for e in lista_e)


def main():
    gestion = GestionEmpleados()
    gestion.cargar_empleados("empleados.csv")
    # print(gestion.empleados)
    print("Sector con mayor costo:", gestion.sector_mayor_costo())

    print("Promedio en IT:", gestion.promedio_salarios("IT"))
    print("Promedio en Marketing:", gestion.promedio_salarios("Marketing"))
    gestion.imprimir_sectores("sectores.txt")


if __name__ == "__main__":
    main()
