"""
Una pizzería vende empanadas por unidad o por docena.
Como primer paso, se pide al usuario que ingrese el precio por docena
y el precio por unidad del día. Si se compran empanadas que no se agrupen
en docenas, las adicionales se cobran por unidad.
Indicar el precio total a abonar, ingresando la cantidad de empanadas vendidas.
"""

precio_unitario = float(input("Precio unitario:"))
precio_docena = float(input("Precio por docena: "))

cantidad_empanadas = int(input("Cantidad de empanadas: "))

unidades = cantidad_empanadas % 12
docenas = cantidad_empanadas // 12

importe_final = precio_unitario * unidades + precio_docena * docenas

print(f"Importe a abonar: {importe_final}")
