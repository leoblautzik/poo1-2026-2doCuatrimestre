# Listas y Archivos

## Objetivos

* Implementar clases para modelar entidades del dominio (`Vecino`) y gestoras de lógica (`GestionVecinos`).  
* Practicar el procesamiento de archivos `.csv` mediante el bloque `with open(...)`.  
* Trabajar con listas de objetos, filtrados, búsquedas, ordenamientos y agregaciones.  
* Utilizar **tuplas** exclusivamente como estructuras de retorno cuando un método deba devolver múltiples valores agrupados.  
* Generar archivos de texto con datos procesados.

> **Restricción importante:** Queda **estrictamente prohibido el uso de diccionarios** (llaves `{}`, tipo `dict` o `csv.DictReader`). La gestión interna de las colecciones se realizará únicamente mediante **listas de objetos**.

---

## Archivo de Entrada

Se utilizará el archivo `personas_buenos_aires.csv` con la siguiente estructura:

```csv
nombre,edad,localidad
Ana,24,Lanus
Ian,35,La Plata
...
```

&nbsp;

---

## Modelado de Clases

### 1\. Clase `Vecino`

Representa a una persona del archivo. Debe contener:

* **Atributos de instancia:**

  * `nombre` (string)  
  * `edad` (int)  
  * `localidad` (string)  
* **Métodos:**

  * `__init__(self, nombre, edad, localidad)`: Constructor que inicializa los tres atributos.  
  * `__repr__(self)` o `__str__(self)`: Devuelve una representación legible del vecino (ej: `"Ana (24 años) - Lanus"`).

---

### 2\. Clase `GestionVecinos`

Administra la colección de objetos `Vecino` y contiene toda la lógica de negocio y procesamiento de archivos.

* **Atributos de instancia:**

  * `vecinos`: Lista donde se almacenan las instancias de la clase `Vecino`.  
* **Método Constructor:**

  * `__init__(self)`: Inicializa el atributo `vecinos` como una lista vacía.

---

## Métodos a implementar en `GestionVecinos`

### Carga de Datos

* **`cargar_desde_csv(self, ruta_archivo)`**: Abre el archivo `.csv`, omite el encabezado y lee cada fila. Por cada línea, crea una instancia de `Vecino` (convirtiendo la edad a entero) y la agrega a la lista `self.vecinos`.

---

### Ejercicios de Procesamiento

#### 1\. Filtrado y Exportación por Localidad

* **`exportar_por_localidad(self, localidad_buscada, archivo_salida)`**: Busca todos los objetos `Vecino` cuyo atributo `localidad` coincida con la pasada por parámetro. Escribe sus datos en el archivo de texto especificado con el formato: `Nombre - Edad años`.  
  * **Retorno:** Retorna un entero con la cantidad de vecinos exportados.

#### 2\. Localidades Únicas

* **`obtener_localidades_unicas(self)`**: Recorre la lista de vecinos y genera una **lista ordenada alfabéticamente** con los nombres de todas las localidades distintas que aparecen en los registros (sin duplicados).  
  * **Retorno:** Una lista de strings.

#### 3\. Estadísticas de Edad

* **`estadisticas_edad(self)`**: Calcula la edad mínima, la edad máxima, el promedio de edad y la cantidad de vecinos mayores o iguales a 60 años.  
  * **Retorno:** Una **tupla** de 4 elementos: `(edad_minima, edad_maxima, promedio_edad, cantidad_mayores_60)`. El promedio debe redondearse a 2 decimales.

#### 4\. Extremos de Nombres por Localidad

* **`extremos_nombre_por_localidad(self, localidad)`**: Filtra los vecinos que pertenecen a la localidad indicada y encuentra al vecino con el nombre más corto y al vecino con el nombre más largo.  
  * **Retorno:** Una **tupla** con dos objetos `Vecino`: `(vecino_nombre_corto, vecino_nombre_largo)`.

#### 5\. Ranking de Mayores (Top N)

* **`obtener_top_mayores(self, n)`**: Ordena la lista de vecinos de mayor a menor según la edad y extrae los primeros `n`.  
  * **Retorno:** Una lista con las `n` instancias de `Vecino` de mayor edad.

---

## Desafío Opcional: Agrupamiento sin Diccionarios

* **`contar_vecinos_por_localidad(self)`**: Aprovechando el método `obtener_localidades_unicas()`, cuenta cuántos vecinos pertenecen a cada localidad.  
  * **Retorno:** Una **lista de tuplas** donde cada tupla contenga `(nombre_localidad, cantidad_vecinos)`. La lista debe retornar ordenada de mayor a menor por la cantidad de vecinos.