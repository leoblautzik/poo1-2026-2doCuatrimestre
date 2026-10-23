# Trabajo Práctico: POO, Listas, Tuplas, Diccionarios y Archivos

## Objetivos

* Modelar entidades del dominio (`Vecino`) y una clase gestora de lógica (`GestionVecinos`).
* Procesar archivos `.csv` y generar archivos de texto mediante el bloque `with open(...)`.
* Trabajar con **listas de objetos**: filtrados, búsquedas, ordenamientos y agregaciones.
* Usar **tuplas** como estructura de retorno cuando un método deba devolver varios valores agrupados.
* Usar **diccionarios** para contar, agrupar, indexar y resumir datos: claves de distintos tipos, valores que son listas u otros diccionarios, y recorrido con `items()`.
* Combinar estructuras (dict → lista de tuplas ordenada, dict con claves tupla) y elegir la más adecuada para cada problema.
* Separar responsabilidades: los datos viven en `Vecino`, la lógica en `GestionVecinos` y la salida por pantalla en `main.py`.

## Mapa de estructuras de datos del TP

| Estructura | Dónde aparece | Ejemplo |
|---|---|---|
| Lista de objetos | `self.vecinos` | `[Vecino, Vecino, ...]` |
| Tupla como retorno | `estadisticas_edad`, `extremos_nombre_por_localidad` | `(18, 75, 45.59, 28)` |
| `dict` str → int | `contar_por_localidad`, `contar_iniciales` | `{"Azul": 5, "Pilar": 6}` |
| `dict` str → lista de objetos | `agrupar_por_localidad`, `buscar_por_nombre` (índice) | `{"Pilar": [Vecino, ...]}` |
| `dict` int → int | `contar_por_decada` | `{20: 21, 30: 16}` |
| `dict` str → `dict` | `estadisticas_por_localidad` | `{"Azul": {"cantidad": 5, ...}}` |
| `dict` con clave tupla | `tabla_localidad_decada` | `{("Azul", 40): 2}` |
| Lista de tuplas | `ranking_localidades` | `[("Mar del Plata", 9), ...]` |

---

## Reglas generales

1. **Partes 1 a 3:** los diccionarios se construyen "a mano", con asignación `d[clave] = valor`, `in`, `get`, `setdefault`, `items()`, `keys()` y `values()`. **No se permite** `collections.Counter`, `collections.defaultdict` ni librerías externas (`pandas`, etc.). Quedan habilitados en la Parte 4.
2. En `obtener_localidades_unicas` (Parte 1) se trabaja **solo con listas** (sin `set` ni diccionarios). Más adelante se compara esa solución con las de diccionario.
3. **Prohibido hardcodear** localidades, edades o cantidades. Todo se calcula a partir de los datos cargados.
4. `Vecino` no sabe nada de archivos, y `GestionVecinos` **no usa `print`**: sus métodos devuelven resultados. Solo `main.py` imprime.
5. Los métodos de consulta **no deben modificar** `self.vecinos`. Para ordenar se usa `sorted(...)` y no `.sort()`.
6. **Criterios de desempate** (valen para todo el TP):
   * Extremos de nombres: gana el **primero** que aparece en el archivo.
   * `obtener_top_mayores`: ante igual edad se mantiene el orden del archivo (`sorted` es estable).
   * Rankings de localidades (por cantidad o por promedio): de mayor a menor valor y, ante empate, por **nombre de localidad en orden alfabético**.
7. Si una consulta no tiene resultados (localidad inexistente, lista vacía), el método debe responder de forma controlada, sin lanzar excepciones. Lo esperado en cada caso se indica en el enunciado.

---

## Archivo de entrada

Se utilizará el archivo `personas_buenos_aires.csv` (112 registros) con la siguiente estructura:

```csv
nombre,edad,localidad
Pedro,43,Zárate
Margarita,59,Pilar
Ciro,27,Bahía Blanca
...
```

Detalles a tener en cuenta:

* El archivo está codificado en **UTF-8** y hay tildes (`Zárate`, `Luján`, `Bahía Blanca`): abrirlo con `encoding="utf-8"`.
* Las líneas terminan en `\r\n`: aplicar `.strip()` a cada línea antes de separar por comas.
* Hay localidades con espacios (`Mar del Plata`, `Lomas de Zamora`). Una clave de diccionario es **sensible** a mayúsculas, tildes y espacios: `"Lanus"` y `"Lanús"` serían claves distintas.

---

## Modelado de clases

### 1. Clase `Vecino`

Representa a una persona del archivo.

* **Atributos de instancia:** `nombre` (str), `edad` (int), `localidad` (str).
* **Métodos:**
  * `__init__(self, nombre, edad, localidad)`: inicializa los tres atributos.
  * `__repr__(self)` o `__str__(self)`: representación legible, por ejemplo `"Ana (24 años) - Lanús"`.

### 2. Clase `GestionVecinos`

Administra la colección de objetos `Vecino` y contiene toda la lógica de negocio.

* **Atributos de instancia:**
  * `vecinos`: lista con las instancias de `Vecino`.
  * `indice_nombres`: diccionario usado como índice de búsqueda por nombre (se completa en el ejercicio 2.7).
* **Constructor:** `__init__(self)` inicializa `vecinos` como lista vacía e `indice_nombres` como diccionario vacío.

---

## Parte 0: Carga de datos

* **`cargar_desde_csv(self, ruta_archivo)`**:
  Abre el archivo, omite el encabezado y lee cada fila. Por cada línea crea una instancia de `Vecino` (convirtiendo la edad a entero) y la agrega a `self.vecinos`.
  * Si se llama más de una vez, **reinicia** la lista (no acumula duplicados).
  * Al terminar, debe dejar armado `indice_nombres` llamando a `construir_indice_nombres()` (ejercicio 2.7).
  * **Retorno:** cantidad de vecinos cargados (entero).

---

## Parte 1: Listas y tuplas

#### 1.1 Filtrado y exportación por localidad
* **`exportar_por_localidad(self, localidad_buscada, archivo_salida)`**:
  Busca los `Vecino` cuya `localidad` coincida **exactamente** con la indicada y escribe sus datos en el archivo de texto con el formato `Nombre - Edad años`.
  * **Retorno:** entero con la cantidad de vecinos exportados.
  * Si no hay coincidencias retorna `0` y **no crea** el archivo.

#### 1.2 Localidades únicas
* **`obtener_localidades_unicas(self)`**:
  Genera una **lista ordenada alfabéticamente** con las localidades distintas (sin duplicados), usando solo listas.
  * **Retorno:** lista de strings.

#### 1.3 Estadísticas de edad
* **`estadisticas_edad(self)`**:
  Calcula edad mínima, edad máxima, promedio de edad y cantidad de vecinos con 60 años o más.
  * **Retorno:** tupla `(edad_minima, edad_maxima, promedio_edad, cantidad_mayores_60)`. El promedio se redondea a 2 decimales.
  * Si no hay vecinos cargados retorna `(None, None, None, 0)`.

#### 1.4 Extremos de nombres por localidad
* **`extremos_nombre_por_localidad(self, localidad)`**:
  Entre los vecinos de la localidad indicada, encuentra al de nombre más corto y al de nombre más largo.
  * **Retorno:** tupla de dos objetos `Vecino`: `(vecino_nombre_corto, vecino_nombre_largo)`.
  * Si la localidad no existe retorna `(None, None)`.

#### 1.5 Ranking de mayores (Top N)
* **`obtener_top_mayores(self, n)`**:
  Ordena los vecinos de mayor a menor edad y toma los primeros `n`.
  * **Retorno:** lista con las `n` instancias de `Vecino` de mayor edad (si `n` supera la cantidad de vecinos retorna todos; si `n` es 0, lista vacía).

---

## Parte 2: Diccionarios (conteo, agrupamiento e índices)

> **Pista general:** casi todos estos ejercicios siguen el mismo patrón. Se recorre `self.vecinos`; para cada vecino se decide la **clave**; si la clave ya está en el diccionario se actualiza su valor, y si no está se crea. Identificar cuál es la clave en cada ejercicio es la mitad del problema.

#### 2.1 Conteo por localidad
* **`contar_por_localidad(self)`**: cuenta cuántos vecinos hay en cada localidad.
  * **Retorno:** `dict` `{localidad: cantidad}`.

#### 2.2 Agrupamiento por localidad
* **`agrupar_por_localidad(self)`**: agrupa los objetos `Vecino` según su localidad.
  * **Retorno:** `dict` `{localidad: [Vecino, Vecino, ...]}`. Cada lista conserva el orden del archivo.
  * *Pista:* `setdefault(clave, [])` o un `if clave not in ...`.

#### 2.3 Promedio de edad por localidad
* **`promedio_edad_por_localidad(self)`**: calcula la edad promedio de cada localidad.
  * **Retorno:** `dict` `{localidad: promedio}` con el promedio redondeado a 2 decimales.
  * Se permite reutilizar `agrupar_por_localidad()`.

#### 2.4 Distribución por década de edad
* **`contar_por_decada(self)`**: cuenta vecinos por década de edad. La clave es la década como entero: `(edad // 10) * 10`. Por ejemplo, 26 años → clave `20`; 18 años → clave `10`.
  * **Retorno:** `dict` `{decada: cantidad}`.
  * Aquí las claves son **enteros**, no strings.

#### 2.5 Frecuencia de letras iniciales
* **`contar_iniciales(self)`**: cuenta cuántos nombres empiezan con cada letra (en mayúscula).
  * **Retorno:** `dict` `{letra: cantidad}`.

#### 2.6 Nombres repetidos
* **`nombres_repetidos(self)`**: detecta los nombres que aparecen más de una vez en el archivo.
  * **Retorno:** `dict` `{nombre: cantidad}` solo con los nombres cuya cantidad sea mayor a 1 (si no hay repetidos, diccionario vacío).
  * *Pista:* primero se arma el diccionario de frecuencias completo y luego se filtra.

#### 2.7 Índice de búsqueda por nombre
* **`construir_indice_nombres(self)`**: arma `self.indice_nombres`, un diccionario `{nombre_en_minusculas: [Vecino, ...]}`. Se usa una **lista** como valor porque un mismo nombre puede corresponder a más de una persona.
* **`buscar_por_nombre(self, nombre)`**: busca usando el índice, sin recorrer `self.vecinos`, y sin distinguir mayúsculas de minúsculas.
  * **Retorno:** lista de `Vecino` (vacía si no hay coincidencias).

---

## Parte 3: Diccionarios anidados, claves compuestas y reportes

#### 3.1 Estadísticas completas por localidad
* **`estadisticas_por_localidad(self)`**: arma un resumen de cada localidad.
  * **Retorno:** `dict` de diccionarios:
    ```python
    {
        "Mar del Plata": {"cantidad": 9, "min": 21, "max": 55, "promedio": 37.44},
        ...
    }
    ```
  * Se permite reutilizar `agrupar_por_localidad()`.

#### 3.2 Localidades extremas por edad promedio
* **`localidades_extremas_por_edad(self)`**: encuentra la localidad con menor y con mayor edad promedio.
  * **Retorno:** tupla de dos tuplas: `((localidad_mas_joven, promedio), (localidad_mas_veterana, promedio))`.
  * Ante empate, aplica el desempate alfabético de las reglas generales.
  * *Pista:* `min()` y `max()` aceptan el parámetro `key`.

#### 3.3 Ranking de localidades
* **`ranking_localidades(self)`**: parte de `contar_por_localidad()` y lo convierte en una lista ordenada.
  * **Retorno:** **lista de tuplas** `(localidad, cantidad)`, ordenada de mayor a menor cantidad y, ante empate, alfabéticamente por localidad.
  * *Pista:* `sorted(d.items(), key=...)`. Una tupla como clave de ordenamiento permite ordenar por dos criterios.
  * Este método reemplaza al desafío opcional de la versión anterior (`contar_vecinos_por_localidad`).

#### 3.4 Tabla cruzada localidad × década
* **`tabla_localidad_decada(self)`**: cuenta vecinos por cada combinación de localidad y década.
  * **Retorno:** `dict` cuya **clave es una tupla**: `{(localidad, decada): cantidad}`. Solo aparecen las combinaciones que existen en los datos.
  * Reflexión asociada: una lista no puede ser clave de un diccionario, pero una tupla sí. ¿Por qué?

#### 3.5 Reporte general de localidades
* **`exportar_reporte_localidades(self, archivo_salida)`**: escribe un archivo de texto con una línea por localidad, siguiendo el orden de `ranking_localidades()`, con el formato:
  ```
  Mar del Plata | 9 vecinos | edad prom: 37.44 | min: 21 | max: 55
  ```
  * Debe apoyarse en `estadisticas_por_localidad()` y `ranking_localidades()`.
  * **Retorno:** cantidad de líneas escritas (entero).

---

## Parte 4: Desafíos opcionales

1. **Moda de edad:** `moda_edad(self)` retorna una tupla `(edad, frecuencia)` de la edad más repetida. Ante empate, la menor edad.
2. **Comparativa de enfoques:** implementar `contar_por_localidad_sin_dict(self)` que retorne una lista de tuplas `(localidad, cantidad)` usando únicamente listas (el enfoque de la versión anterior). Medir tiempos con `time.perf_counter()` contra la versión con diccionario, repitiendo la lista de vecinos varias miles de veces para que la diferencia sea visible. Comparar también `obtener_localidades_unicas` con una versión que use `set` o `dict.fromkeys`.
3. **Herramientas de `collections`:** reescribir `contar_por_localidad`, `agrupar_por_localidad` y `contar_iniciales` con `Counter` y `defaultdict`, y comparar legibilidad y cantidad de líneas.
4. **Comprehensions:** reescribir con *dict comprehension* los métodos donde sea posible. Agregar `localidades_con_al_menos(self, minimo)`, que retorne `{localidad: cantidad}` solo de las localidades con `cantidad >= minimo`.
5. **Un archivo por localidad:** `exportar_archivos_por_localidad(self, carpeta)` crea la carpeta (`os.makedirs(..., exist_ok=True)`) y genera un `.txt` por localidad usando `agrupar_por_localidad()`. Retorna la cantidad de archivos creados. Atención con los espacios y las tildes en los nombres de archivo.
6. **Vecino ↔ diccionario ↔ JSON:** agregar a `Vecino` el método `a_diccionario(self)` y un método de clase `desde_diccionario(cls, d)`. Con ellos, implementar `exportar_json(self, ruta)` y `cargar_desde_json(self, ruta)` usando el módulo `json`.
7. **Carga con `csv.DictReader`:** escribir una segunda versión de la carga con `csv.DictReader` y comparar con la lectura manual.
8. **Búsqueda tolerante:** que `buscar_por_nombre` y `exportar_por_localidad` ignoren mayúsculas y tildes (con `unicodedata`), de modo que `"lanus"` encuentre a `"Lanús"`.
9. **Menú con diccionario de funciones:** en `main.py`, un menú interactivo donde cada opción sea una clave de un diccionario cuyo valor sea la función a ejecutar (en lugar de una cadena de `if/elif`).

---

## Programa principal (`main.py`)

Debe cargar el archivo, invocar **todos** los métodos obligatorios y mostrar los resultados por pantalla de forma legible. Además:

* Mostrar la distribución por década como un **histograma de texto**, por ejemplo:
  ```
  20s | █████████████████████ 21
  30s | ████████████████ 16
  ```
  (recorriendo el diccionario con las claves ordenadas).
* Mostrar el Top 5 de localidades del ranking y el detalle de una localidad elegida (estadísticas más listado de sus vecinos).
* Mostrar un ejemplo de búsqueda por nombre con un nombre repetido.

## Estructura y entrega

```
.vscode/
src/
    __init__.py
    vecino.py
    gestion_vecinos.py
    main.py
tests/
    __init__.py
    test_gestion_vecinos.py
personas_buenos_aires.csv
```

* Las pruebas se escriben con `unittest` y se verifican contra los valores de referencia del anexo.
* Cada método debe tener una breve descripción (docstring) que indique qué recibe y qué retorna.

## Criterios de evaluación

* Funcionamiento correcto de los métodos y de los casos borde indicados.
* Uso adecuado de cada estructura (lista, tupla, diccionario) según lo pedido, respetando las restricciones de cada parte.
* Diseño orientado a objetos: responsabilidades bien separadas, sin `print` dentro de la lógica, sin modificar `self.vecinos` en las consultas.
* Legibilidad: nombres claros, código sin repeticiones innecesarias, docstrings.
* Pruebas y programa principal.

## Preguntas de reflexión

Responder brevemente, en comentarios al final de `main.py` o en un archivo `REFLEXION.md`:

1. ¿Por qué `contar_por_localidad` devuelve un diccionario y no una lista de tuplas? ¿Qué ventaja tiene buscar una clave frente a recorrer una lista?
2. ¿Qué tipos de datos pueden ser claves de un diccionario y cuáles no? ¿Por qué una tupla sirve como clave en `tabla_localidad_decada` y una lista no?
3. `estadisticas_edad` devuelve una tupla y `estadisticas_por_localidad` devuelve un diccionario de diccionarios. ¿Cuándo conviene cada uno?
4. Si una localidad figurara como `"Lanus"` en algunas filas y como `"Lanús"` en otras, ¿qué pasaría con los conteos? ¿Cómo lo resolverías?
5. ¿Cuándo es mejor guardar datos en un diccionario y cuándo en una lista de objetos `Vecino`?

---

## Anexo: valores de referencia

Con el archivo `personas_buenos_aires.csv` provisto deben obtenerse estos resultados.

**Carga y Parte 1**

| Método | Resultado esperado |
|---|---|
| `cargar_desde_csv` | `112` |
| `exportar_por_localidad("Mar del Plata", ...)` | `9` |
| `exportar_por_localidad("Lanús", ...)` | `1` |
| `exportar_por_localidad("Lanus", ...)` | `0` (sin tilde no coincide) |
| `len(obtener_localidades_unicas())` | `28` |
| `obtener_localidades_unicas()[:3]` | `["Avellaneda", "Azul", "Bahía Blanca"]` |
| `estadisticas_edad()` | `(18, 75, 45.59, 28)` |
| `extremos_nombre_por_localidad("Mar del Plata")` | `(Ana, Hermenegildo)` |
| `extremos_nombre_por_localidad("Inexistente")` | `(None, None)` |
| `obtener_top_mayores(3)` | Marcelo (75), Valentina (74), Desiderio (74) |

**Parte 2**

| Método | Resultado esperado |
|---|---|
| `contar_por_localidad()` | 28 claves; `"Mar del Plata": 9`, `"Lanús": 1`; la suma de valores da `112` |
| `agrupar_por_localidad()["Mar del Plata"]` | lista de 9 `Vecino` |
| `promedio_edad_por_localidad()` | `"Mar del Plata": 37.44`, `"Junín": 25.0`, `"Merlo": 58.0`, `"Tigre": 54.25` |
| `contar_por_decada()` | `{10: 5, 20: 21, 30: 16, 40: 20, 50: 22, 60: 18, 70: 10}` |
| `contar_iniciales()` | `"M": 15`, `"C": 10`, `"E": 10` |
| `nombres_repetidos()` | `{"Gonzalo": 2}` |
| `buscar_por_nombre("gonzalo")` | 2 vecinos: Gonzalo (52, Banfield) y Gonzalo (43, Olavarría) |
| `buscar_por_nombre("Zzz")` | `[]` |

**Parte 3**

| Método | Resultado esperado |
|---|---|
| `estadisticas_por_localidad()["Mar del Plata"]` | `{"cantidad": 9, "min": 21, "max": 55, "promedio": 37.44}` |
| `localidades_extremas_por_edad()` | `(("Junín", 25.0), ("Merlo", 58.0))` (Merlo y Olavarría empatan en 58.0; gana Merlo por orden alfabético) |
| `ranking_localidades()[:7]` | `[("Mar del Plata", 9), ("Lomas de Zamora", 6), ("Luján", 6), ("Moreno", 6), ("Pilar", 6), ("Quilmes", 6), ("Zárate", 6)]` |
| `tabla_localidad_decada()` (Mar del Plata) | `(MdP, 20): 3`, `(MdP, 30): 2`, `(MdP, 40): 1`, `(MdP, 50): 3` |
| `exportar_reporte_localidades(...)` | `28` líneas escritas |

**Parte 4**

| Método | Resultado esperado |
|---|---|
| `moda_edad()` | `(64, 6)` |
