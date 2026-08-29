# poo1-2026-2doCuatrimestre

Desafíos:
[Desafíos](https://docs.google.com/document/d/1MEzr3MH6jAIujhfk1A70Y_JGcvShkq9__xcKxYhXLgk/edit?usp=sharing)

Asistencia:
[Planilla de Asistencia](https://docs.google.com/spreadsheets/d/1TlPqKkJ_k13SYOFci77_zyYrFhlsFOGAKdSCiH-OxnI/edit?usp=sharing)


## Estructura de carpetas y módulos para trabajar con Python y unittest

Archivo de configuración para VSCode + unittest.

Dentro del proyecto y en la raíz del mismo, crear una carpeta `.vscode`. Dentro de esa carpeta crear un archivo `settings.json` con el siguiente contenido:

```json
{
    "python.testing.unittestArgs": [
        "-v",
        "-s",
        "tests",
        "-p",
        "test_*.py"
    ],
    "python.testing.pytestEnabled": false,
    "python.testing.unittestEnabled": true
}
```

Para que unittest haga descubrimiento recursivo de los tests, se recomienda la siguiente estructura de carpetas:

```
proyecto/
├── .vscode/
│   └── settings.json
├── src/
│   ├── __init__.py
│   └── ejercicio1.py
└── tests/
    ├── __init__.py
    └── test_ejercicio1.py
```

Nótese que tanto en `/src` como en `/tests` debe haber un archivo (vacío) `__init__.py` para que unittest lo considere un paquete Python válido.

Además, para lograr la correcta importación de los módulos dentro de los tests, debemos hacerla de la siguiente manera:

```python
from src.ejercicio1 import funcion
```

Es muy importante cerrar los archivos de test con:

```python
if __name__ == "__main__":
    unittest.main()
```

#leoblau
