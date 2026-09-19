"""
Escribir un programa que pregunte
el nombre del usuario en la consola y
después de que el usuario lo introduzca muestre
por pantalla la cadena ¡Hola <nombre>!, donde <nombre>
es el nombre que el usuario haya introducido
"""

nombre_usuario = input("Ingresa tu nombre: ")
print(f"¡Hola {nombre_usuario}!")
edad = int(input("Ingresa tu edad: "))
print(f"Tu edad es: {edad}")
print(f"Pronto cumplirás {edad + 1} años")
