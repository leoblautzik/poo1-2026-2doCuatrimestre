"""
Una panadería vende bolsas de pan a ARS 2000 cada una.
El pan que no es el día tiene un descuento del 60%.
Escribir un programa que comience leyendo el número de bolsas vendidas que no son del día.
Después el programa debe mostrar el precio habitual de una bolsa de pan,
el descuento que se le hace por no ser fresca y el coste final total.
"""

precio_habitual = 2000.00
bolsas_vendidas = int(input("Ingrese las bolsas vendidas: "))
print(f"Precio habitual: {precio_habitual} ")
print(f"Pprecio con descuento: {precio_habitual * 0.4}")
print(f"Importe total: {precio_habitual * 0.4 * bolsas_vendidas}")
