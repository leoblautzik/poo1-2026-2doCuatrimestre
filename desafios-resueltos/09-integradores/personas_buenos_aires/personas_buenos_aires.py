import csv

""" Implementar clases para modelar entidades del dominio (Vecino) y 
gestoras de lógica (GestionVecinos).
Practicar el procesamiento de archivos .csv mediante el bloque with open(...).
Trabajar con listas de objetos, filtrados, búsquedas, ordenamientos y 
agregaciones.
Utilizar tuplas exclusivamente como estructuras de retorno cuando un 
método deba devolver múltiples valores agrupados.
Utilizar diccionarios para contar, agrupar y resumir los datos de los vecinos.
Generar archivos de texto con datos procesados.
"""


class Vecino:
    def __init__(self, nombre: str, edad: int, localidad: str) -> None:
        self.nombre: str = nombre
        self.edad: int = edad
        self.localidad: str = localidad

    def __repr__(self) -> str:
        return f"Nombre: {self.nombre}, edad: {self.edad}, localidad: {self.localidad}"


class GestionVecinos:
    """Administra la colección de objetos Vecino y contiene
    toda la lógica de negocio y procesamiento de archivos.
    """

    def __init__(self) -> None:
        self.vecinos: list[Vecino] = []

    def cargar_desde_csv(self, archivo):
        """Abre el archivo .csv, omite el encabezado y
        lee cada fila. Por cada línea, crea una instancia de Vecino
        (convirtiendo la edad a entero) y la agrega a la lista self.vecinos.
        """
        with open(archivo, "r", encoding="utf-8") as pba:
            lector = csv.reader(pba)
            lector.__next__()
            for datos in lector:
                self.vecinos.append(Vecino(datos[0], int(datos[1]), datos[2]))

    def exportar_por_localidad(self, localidad_buscada):
        """Busca todos los objetos Vecino cuyo atributo localidad coincida
        con la pasada por parámetro. Escribe sus datos en el archivo de
        texto especificado con el formato: Nombre - Edad años.
        Retorno: Retorna un entero con la cantidad de vecinos exportados.
        """
        salida = localidad_buscada + ".txt"
        with open(salida, "w", encoding="utf-8") as f:
            f.write("Nombre              " + "\t" + "Edad" + "\n")
            for v in self.vecinos:
                if v.localidad == localidad_buscada:
                    f.write(f"{v.nombre:20} \t {v.edad}\n")

    def obtener_localidades_unicas(self) -> list[str]:
        """Recorre la lista de vecinos y genera una lista ordenada
        alfabéticamente con los nombres de todas las localidades
        distintas que aparecen en los registros (sin duplicados).
        Retorno: Una lista de strings.
        """
        localidades_unicas = []

        for v in self.vecinos:
            if v.localidad not in localidades_unicas:
                localidades_unicas.append(v.localidad)

        localidades_unicas.sort()
        return localidades_unicas

    def estadisticas_edad(self, edad_tope):
        """Calcula la edad mínima, la edad máxima, el promedio de edad y
        la cantidad de vecinos mayores o iguales a 60 años.
        Retorno: Una tupla de 4 elementos:
        (edad_minima, edad_maxima, promedio_edad, cantidad_mayores_60).
        El promedio debe redondearse a 2 decimales.
        """

        if len(self.vecinos) == 0:
            return
        edad_minima = self.vecinos[0].edad
        edad_maxima = self.vecinos[0].edad
        contador_mayores_al_tope = 0
        suma_edades = 0

        for v in self.vecinos:
            edad_minima = min(edad_minima, v.edad)
            edad_maxima = max(edad_maxima, v.edad)
            if v.edad > edad_tope:
                contador_mayores_al_tope += 1
            suma_edades += v.edad

        edad_promedio = round(suma_edades / len(self.vecinos), 2)

        return (
            edad_minima,
            edad_maxima,
            edad_promedio,
            contador_mayores_al_tope,
        )

    def extremos_nombre_por_localidad(self, localidad):
        """
        Filtra los vecinos que pertenecen a la localidad indicada y encuentra al
        vecino con el nombre más corto y al vecino con el nombre más largo.
        Retorno: Una tupla con dos objetos Vecino:
        (vecino_nombre_corto, vecino_nombre_largo).
        """
        if localidad not in self.obtener_localidades_unicas():
            return

        nombre_corto: str = ""
        nombre_largo: str = ""

        es_primero = True
        for v in self.vecinos:
            if v.localidad == localidad:
                if es_primero or len(v.nombre) < len(nombre_corto):
                    nombre_corto = v.nombre

                if es_primero or len(v.nombre) > len(nombre_largo):
                    nombre_largo = v.nombre

                es_primero = False

        return (nombre_corto, nombre_largo)

    def contar_vecinos_por_localidad(self):
        """Aprovechando el método obtener_localidades_unicas(),
        cuenta cuántos vecinos pertenecen a cada localidad.
        Retorno: Una lista de tuplas donde cada tupla contenga
        (nombre_localidad, cantidad_vecinos).
        La lista debe retornar ordenada de mayor a menor por la
        cantidad de vecinos.
        """

        localidades = self.obtener_localidades_unicas()
        lista_tuplas = []

        for l in localidades:
            contador = 0
            for v in self.vecinos:
                if v.localidad == l:
                    contador += 1
            lista_tuplas.append((l, contador))

        lista_tuplas.sort(key=lambda lista_tuplas: lista_tuplas[1])

        return lista_tuplas

    def contar_vecinos_por_localidad_dic(self):
        """Utilizando un diccionario, cuenta cuántos vecinos pertenecen
        a cada localidad.
        Retorno: Un diccionario (dict[str, int]):
            {nombre_localidad: cantidad_vecinos}.
        """
        dic_out: dict[str, int] = {}
        # lista_tuplas = []

        for v in self.vecinos:
            localidad = v.localidad
            cantidad_vecinos = dic_out.get(localidad, 0) + 1
            dic_out[localidad] = cantidad_vecinos

        # for k, v in dic_out.items():
        #     lista_tuplas.append((k, v))
        #
        # lista_tuplas.sort(key=lambda lista_tuplas: lista_tuplas[1])

        return dic_out

    def localidades_mas_pobladas(self):
        """Determina cuál es la mayor cantidad de vecinos que tiene una
        localidad y qué localidades alcanzan esa cantidad (puede haber empates).
        Retorno: Una tupla (tuple[int, list[str]]): (cantidad_vecinos, lista_de_localidades).
        """
        aux = self.contar_vecinos_por_localidad_dic()
        lista = []
        max_cant_vecinos = max(aux.values())

        for k, v in aux.items():
            if v == max_cant_vecinos:
                lista.append(k)

        return max_cant_vecinos, lista


def main():

    gv = GestionVecinos()
    gv.cargar_desde_csv("personas_buenos_aires.csv")
    # print(gv.vecinos)
    # gv.exportar_por_localidad("Zárate")
    # gv.exportar_por_localidad("Quilmes")
    # print(gv.obtener_localidades_unicas(), len(gv.obtener_localidades_unicas()))
    # print(gv.estadisticas_edad(45))
    # print(gv.extremos_nombre_por_localidad("Quilmes"))
    print(gv.contar_vecinos_por_localidad())
    print(gv.contar_vecinos_por_localidad_dic())


if __name__ == "__main__":
    main()
