"""
============================================================
                    EJERCICIOS CON DICT
============================================================
"""


def contar_frecuencias(palabras: list[str]) -> dict[str, int]:
    """Recibe una lista de palabras y devuelve un diccionario donde
    las claves son palabras y los valores la cantidad de veces
    que aparece cada una.

    contar_frecuencias(["uno", "dos", "uno"]), {"uno": 2, "dos": 1}
    """
    frecuencias: dict[str, int] = {}

    for p in palabras:
        p = p.lower().strip()

        frecuencias[p] = frecuencias.setdefault(p, 0) + 1

    return frecuencias


def palabra_mas_frecuente(dic: dict[str, int]) -> tuple[int, list[str]]:
    """devuelve la palabra con mayor frecuencia y su frecuencia.
    en caso de que haya empate, se debe retornar la frecuencia maxima y
    todas las palabras que se repiten ese numero de veces"""

    frec_max = 0
    palabras_mas_frecuentes = []

    for frecuencia in dic.values():
        frec_max = max(frec_max, frecuencia)

    for palabra, value in dic.items():
        if value == frec_max:
            palabras_mas_frecuentes.append(palabra)

    return (frec_max, palabras_mas_frecuentes)

    # return max(dic.items(), key=lambda item: item[1])


def invertir_diccionario(dic_in: dict[str, list[str]]) -> dict[str, list[str]]:
    """Tenemos que ayudar a los docentes a preparar la información
    solicitada por el Departamento de Alumnos.
    Cuando toman asistencia anotan los presentes por día de clase,
    pero ahora desde Alumnos se les pide que envíen la información
    de asistencia por alumno, ordenada por nombre de alumnos.
    Por ejemplo, si la lista que se recibe es:
    [
     (“Mie 10”, [“Ana", "Pedro"]),
     (“Vie 12”, [“Ana", "Luz”]),
     (“Mie 17”, [“Luz”, "Pedro"])
    ]
    El resultado debe ser:
    [("Ana", [ "Mie 10", "Vie 12"]),
     ("Luz", [ "Vie 12", "Mie 17"] ),
     ("Pedro", ["Mie 10", "Mie 17"])].
    """
    dic_out: dict[str, list[str]] = {}

    for dia, alumnos in dic_in.items():
        for cada_alumno in alumnos:
            lista_dias = dic_out.setdefault(cada_alumno, [])
            lista_dias.append(dia)
            dic_out[cada_alumno] = lista_dias

    return dic_out


def fusionar_diccionarios(dic1: dict[str, int], dic2: dict[str, int]) -> dict[str, int]:
    """Devuelve un nuevo diccionario que contiene todas las claves de ambos.
    Si una clave aparece en ambos, el valor debe ser la suma de los dos."""

    dic_out: dict[str, int] = {}

    for k, v in dic1.items():
        dic_out[k] = dic_out.setdefault(k, 0) + v

    for k, v in dic2.items():
        dic_out[k] = dic_out.setdefault(k, 0) + v

    return dic_out


def filtrar_por_valor(dic_in: dict[str, int], minimo: int) -> dict[str, int]:
    """Devuelve un nuevo diccionario con solo las claves cuyo valor es mayor o
    igual que 'minimo'."""

    dic_out: dict[str, int] = {}

    for k, v in dic_in.items():
        if v >= minimo:
            dic_out[k] = v

    return dic_out


def clave_mas_larga(dic: dict[str, str]) -> str:
    """Recibe un diccionario cuyas claves y valores son strings.
    Devuelve la clave con mayor longitud.
    Si el diccionario está vacío, devuelve cadena vacía."""

    if not dic:
        return ""

    clave_max = ""
    for key in dic:
        if len(key) > len(clave_max):
            clave_max = key

    return clave_max

    return max(dic.keys(), key=len)


def main():
    pass


if __name__ == "__main__":
    main()
