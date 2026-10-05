## Respuestas primer parcial 05/10/26



```python

# A.
class Pintor(Artista):
    def get_cuota_mensual(self):
        return super().get_cuota_base() * (1 + 0.10 * super().get_dias())


class Escultor(Artista):
    def get_cuota_mensual(self):
        return super().get_cuota_base() * (1 + 0.05 * super().get_dias())

# B.
class Academia:
    def __init__(self):
        self.__artistas: list[Artista] = []

    def agregar_artista(self, artista):
        self.__artistas.append(artista)

    def get_total_mensual_de_cuotas(self):
        total = 0
        for a in self.__artistas:
            total += a.get_cuota_mensual()
        return total

    def listar_planilla_de_artistas(self):
        for a in self.__artistas:
            print(a)
```


C (Verdadero o Falso)

1. VERDADERO
Gracias al polimorfismo y al enlace dinámico (dynamic binding), get_total_mensual_de_cuotas() 
recorre los artistas y llama a get_cuota_mensual() sobre cada uno. Python decide qué versión 
ejecutar según el tipo real del objeto en tiempo de ejecución. Por eso Ceramista funciona 
sin tocar Academia, que depende de la abstracción Artista y no de las clases concretas (principio abierto/cerrado).

2. FALSO
Aunque el objeto Pintor sí contiene el atributo, en Python un atributo con doble guion bajo 
sufre name mangling. En Artista se almacena como _Artista__dias, y dentro de Pintor el nombre 
self.__dias se transforma en _Pintor__dias, que no existe y lanza AttributeError. 
Para acceder desde la subclase hay que usar un getter público (por ejemplo get_dias()) 
o declarar el atributo como protegido (_dias).

3. VERDADERO
Al sobrescribir un método, la subclase puede extender el comportamiento heredado en lugar de 
reemplazarlo, invocando la versión de la superclase con super().metodo(...) y agregando lo propio antes o después. 
Esto evita duplicar código y mantiene la lógica común en un solo lugar.

4. FALSO
El encapsulamiento consiste en ocultar la representación interna y exponer solo las operaciones necesarias. 
Declarar un getter y un setter para cada atributo expone el estado igual que si fuera público y rompe el encapsulamiento. 
Se debe ofrecer únicamente lo que la abstracción necesita, preferentemente como comportamiento y no como acceso a datos, 
y muchos atributos no deberían tener setter.

5. VERDADERO
list(self.__artistas) crea una copia superficial (shallow copy): la lista es nueva, 
así que agregar o quitar elementos no afecta a la de la academia. 
Pero los elementos son las mismas referencias a los objetos Artista originales, 
por lo que un cliente puede modificar su estado (por ejemplo, los días de un Pintor). 
Para evitarlo habría que devolver copias de los objetos (copia profunda) o usar objetos inmutables.
