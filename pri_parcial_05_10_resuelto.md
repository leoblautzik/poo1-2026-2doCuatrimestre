## Respuestas primer parcial 05/10/26


### A 

Una academia de arte admite pintores y escultores. De todos se guarda el legajo y los días por semana que asiste.  
Todos los artistas pagan una cuota base, igual para todos.  
Los pintores pagan la cuota base más un 10 % de la cuota base por cada día que asisten, y los escultores un 5 % mas por día.  
Se dispone de la clase Artista (abstracta) ya implementada, con get_dias(), get_cuota_base(), get_cuota_mensual() abstracto y __repr__.  
Implementar Pintor y Escultor con la funcionalidad necesaria para cumplir con la parte 


```python

class Pintor(Artista):
    def get_cuota_mensual(self):
        return super().get_cuota_base() * (1 + 0.10 * super().get_dias())


class Escultor(Artista):
    def get_cuota_mensual(self):
        return super().get_cuota_base() * (1 + 0.05 * super().get_dias())
```

### B

B. Implementar la class Academia de acuerdo al siguiente modelo:


```python

class Academia:
    def __init__(self):
        self.__artistas: list[Artista] = []

    def agregar_artista(self, artista):
    """Los artistas se van agregando en una lista de Artista artistas, que es atributo privado de la class"""
        self.__artistas.append(artista)

    def get_total_mensual_de_cuotas(self):
    """Retorna el importe total recaudado por todos los artistas de la Academia"""
        total = 0
        for a in self.__artistas:
            total += a.get_cuota_mensual()
        return total

    def listar_planilla_de_artistas(self):
    """Emite por consola el listado de los artistas de a uno por línea, mostrando en cada una el número de legajo, cantidad de días y el valor de la cuota que abona."""
        for a in self.__artistas:
            print(a)
```


C (Verdadero o Falso)

1.  Si se agrega una clase Ceramista que hereda de Artista e implementa get_cuota_mensual(), el método get_total_mensual_de_cuotas() de Academia incluye correctamente su cuota sin modificar ninguna línea de Academia. Esto es posible porque el método que se ejecuta depende del tipo real del objeto y no del tipo de la variable que lo referencia.
    VERDADERO -> Gracias al polimorfismo y al enlace dinámico (dynamic binding), get_total_mensual_de_cuotas() 
    recorre los artistas y llama a get_cuota_mensual() sobre cada uno. Python decide qué versión 
    ejecutar según el tipo real del objeto en tiempo de ejecución. Por eso Ceramista funciona 
    sin tocar Academia, que depende de la abstracción Artista y no de las clases concretas (principio abierto/cerrado).  

2.  En Pintor, si decido usar self.__dias dentro de get_cuota_mensual(),puedo acceder a los días del artista, ya que Pintor hereda ese atributo de Artista y forma parte de su estado.  
    FALSO -> Aunque el objeto Pintor sí contiene el atributo, en Python un atributo con doble guion bajo 
    sufre name mangling. En Artista se almacena como _Artista__dias, y dentro de Pintor el nombre 
    self.__dias se transforma en _Pintor__dias, que no existe y lanza AttributeError. 
    Para acceder desde la subclase hay que usar un getter público (por ejemplo get_dias()) 
    o declarar el atributo como protegido (_dias).

3.  Una subclase puede sobrescribir un método de su superclase y, dentro de la nueva versión, reutilizar el comportamiento original invocando a la superclase (por ejemplo, con super()), en lugar de reescribirlo por completo.  
    VERDADERO -> Al sobrescribir un método, la subclase puede extender el comportamiento heredado en lugar de 
    reemplazarlo, invocando la versión de la superclase con super().metodo(...) y agregando lo propio antes o después. 
    Esto evita duplicar código y mantiene la lógica común en un solo lugar.

4.  Para respetar el encapsulamiento, toda clase debe declarar todos sus atributos como privados y ofrecer un getter y un setter para cada uno, de modo que ningún cliente acceda directamente al estado del objeto.    
    FALSO -> El encapsulamiento consiste en ocultar la representación interna y exponer solo las operaciones necesarias. 
    Declarar un getter y un setter para cada atributo expone el estado igual que si fuera público y rompe el encapsulamiento. 
    Se debe ofrecer únicamente lo que la abstracción necesita, preferentemente como comportamiento y no como acceso a datos, 
    y muchos atributos no deberían tener setter.

5.  Academia guarda los artistas en self.__artistas, suponga que define get_artistas() que retorna list(self.__artistas). Un cliente ya no puede agregar ni quitar artistas de la academia mediante esa lista, pero sí puede modificar el estado de los objetos Artista que contiene (por ejemplo, cambiar los días de un Pintor).  
    VERDADERO -> list(self.__artistas) crea una copia superficial (shallow copy): la lista es nueva, 
    así que agregar o quitar elementos no afecta a la de la academia. 
    Pero los elementos son las mismas referencias a los objetos Artista originales, 
    por lo que un cliente puede modificar su estado (por ejemplo, los días de un Pintor). 
    Para evitarlo habría que devolver copias de los objetos (copia profunda) o usar objetos inmutables.
