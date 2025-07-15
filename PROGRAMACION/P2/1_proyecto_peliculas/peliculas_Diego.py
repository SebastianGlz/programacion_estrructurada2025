import os 
peliculas=[]

'''peliculas={
    "nombre":"",
    "Categoria":"",
    "Clasificacion":"",
    "Genero":"",
    "Idioma":""
}'''
pelicula={}
import os

# Asumo que estas variables están declaradas globalmente
pelicula = {}
peliculas = {}

import os

def borrarPantalla():
    os.system("cls")

def esperarTecla():
    input("\U0001F552 Presiona una tecla para continuar...")

def anadir_peliculas():
    borrarPantalla()
    print("\n\t🎬 \U0001F4DD ...::: Añadir Película :::... \U0001F4DD 🎬")
    pelicula.update({"nombre": input("\U0001F464 Ingrese el Nombre: ").upper().strip()})
    pelicula.update({"Categoria": input("\U0001F4C2 Ingrese la Categoría: ").upper().strip()})
    pelicula.update({"Clasificacion": input("\U0001F4DB Ingrese la Clasificación: ").upper().strip()})
    pelicula.update({"Genero": input("\U0001F4C2 Ingrese el Género: ").upper().strip()})
    pelicula.update({"Idioma": input("\U0001F5E3 Ingrese el Idioma: ").upper().strip()})
    print("\u2705 Se agregó una película correctamente")

def Modificar_peliculas():
    borrarPantalla()
    print(peliculas)
    nombre = input("\u2699 Ingrese el nombre de la película a modificar: ")
    print(peliculas)
    peliculas.replace(nombre)  

def Consultar_peliculas():
    borrarPantalla()
    print("\U0001F50D ..:: Películas ::..")
    if len(pelicula) > 0:
        for i in pelicula:
            print(f"\t\U0001F3A5 {i}: {pelicula[i]}")
    else:
        print("\u274C No hay películas en el sistema")

def Vaciar_peliculas():
    borrarPantalla()
    print("\n\t\U0001F4DB .:: Borrar todas las películas ::.")
    res = input("\u26A0 ¿Deseas borrar todas las películas del sistema? (si/no): ").lower()
    if res == "si":
        peliculas.clear()
        print("\u2705 Ya se vaciaron todas las películas")

def Buscar_peliculas():
    borrarPantalla()
    print("\n\t\U0001F50D .:: Buscar Películas ::.")
    pelicula_buscar = input("\U0001F4DD Ingrese el nombre de la película a buscar: ").upper().strip()
    encontro = 0
    if pelicula_buscar not in peliculas:
        print("\u274C ¡No se encuentra la película a buscar!")
    else:
        for i in range(len(peliculas)):
            if pelicula_buscar == peliculas[i]:
                print(f"\u2705 La película '{pelicula_buscar}' está en la casilla {i+1}")
                encontro += 1
        if encontro > 0:
            print(f"\U0001F389 Tenemos {encontro} película(s) con este título")
            input("\u2705 ¡La operación se realizó correctamente!")

def Eliminar_peliculas():
    borrarPantalla()
    print("\n\t\U0001F4DB ..:: Borrar una película ::..")
    nombre_eliminar = input("\U0001F4DD Ingrese el nombre de la película a eliminar: ").upper()
    encontro = 0
    if nombre_eliminar not in peliculas:
        print("\u274C ¡No se encuentra la película a buscar!")
    else:
        for i in range(len(peliculas)):
            if nombre_eliminar == peliculas[i]:
                print(f"\U0001F4C2 La película que se borrará es '{nombre_eliminar}' (casilla {i+1})")
                res = input("\u26A0 ¿Deseas eliminarla? (si/no): ").lower()
                if res == "si":
                    peliculas.remove(nombre_eliminar)
                    encontro += 1
    if encontro > 0:
        print(f"\u2705 Se borró {encontro} película(s) con este título")

def agregarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t\U0001F4DD .:: Agregar Característica a Películas ::.")
    atributo = input("\U0001F4DD Ingresa la nueva característica: ").lower().strip()
    valor = input("\U0001F4DD Ingresa el valor: ").upper().strip()
    peliculas.update({atributo: valor})
    print("\u2705 Característica agregada")

def modificarCaracteristicasPeliculas():
    borrarPantalla()
    print("\n\t\U0001F6E0 .:: Modificar Característica ::.")
    atributo = input("\U0001F9E9 ¿Qué atributo deseas modificar? ").lower().strip()
    if atributo in peliculas:
        nuevo_valor = input(f"\U0001F4DD Nuevo valor para '{atributo}': ").upper().strip()
        peliculas[atributo] = nuevo_valor
        print(f"\u2705 '{atributo}' actualizado a: {nuevo_valor}")
    else:
        print("\u274C El atributo ingresado no es válido")

def borrarCaracteristicas():
    borrarPantalla()
    print("\n\t\U0001F5D1 .:: Borrar Característica ::.")
    atributo = input("\U0001F50D Ingresa la característica que deseas borrar: ").lower().strip()
    if atributo in peliculas:
        del peliculas[atributo]
        print("\u2705 Característica eliminada con éxito")
    else:
        print("\u26A0 La característica no existe")
    input("\U0001F552 Presiona cualquier tecla para continuar...")

def eliminarPeliculas():
    borrarPantalla()
    print("\n\t\U0001F4DB .:: Eliminar Películas ::.")
    pelicula_buscar = input("\U0001F50D Ingrese el nombre de la película que desea eliminar: ").upper().strip()
    encontro = 0
    if pelicula_buscar not in peliculas:
        print("\u274C ¡No se encuentra la película!")
    else:
        resp = "si"
        while pelicula_buscar in peliculas and resp == "si":
            resp = input("\u26A0 ¿Deseas eliminarla? (si/no): ").lower()
            if resp == "si":
                posicion = peliculas.index(pelicula_buscar)
                peliculas.remove(pelicula_buscar)
                print(f"\u2705 '{pelicula_buscar}' fue eliminada (casilla {posicion+1})")
                encontro += 1
        print(f"\U0001F389 Se eliminaron {encontro} película(s) con ese título")

     