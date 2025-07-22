'''es una coleccion desordenadam inmutable y no indexada, no hay miembros duplicados.'''
import os
os.system("cls")

personas= {"Ramiro", "Choche", "Lupe"}
print(personas)
personas.add("Peje")
print(personas)
personas.pop()
personas.clear()
print(personas)
print("-----------------------")
varios={3.1416, 3, True, "Hola"}
print(varios)

#crear un programa que solicite el correo de los alumnos y almacenarlas en una lista y posteriormente mostrarla en pantalla sin duplicados
os.system("cls")
opc="si"
while opc=="si":
    correo=input("Ingresa tu correo: ")
    print(correo)
    opc=input("Deseas ingresar otro correo? (si/no): ").lower()

    #imprimir los emails sin duplicados
    print(correo)
    set1=set(correo)
    print(set1)
    correo=list(set1)
    print(correo)
