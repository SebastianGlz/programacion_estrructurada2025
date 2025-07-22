'''Crear un proyecto que permita adminsitrar peliculas.colocar un menu de opciones para agregar 
eliminar modificar y consultar peliculas

notas:
1._Utilizar funciones y mandar a llamar desde otros archivo
2._Utilizar listas para los nombres de peliculas

'''
import peliculas_dago
import os
os.system("cls")

def menu(op):
    match op:
        case 1:
            peliculas_dago.anadir_peliculas()
            peliculas_dago.esperarTecla()
        case 2:
            peliculas_dago.Eliminar_peliculas()
            peliculas_dago.esperarTecla()
        case 3:
            peliculas_dago.Consultar_peliculas()
            peliculas_dago.esperarTecla()
        case 4:
            peliculas_dago.agregarCaracteristicaPeliculas()
            peliculas_dago.esperarTecla()
        case 5:
            peliculas_dago.modificarCaracteristicasPeliculas()
            peliculas_dago.esperarTecla()
        case 6:
            peliculas_dago.borrarCaracteristicas()
            peliculas_dago.esperarTecla()
        case 7:
            print("\U0001F6AA Saliendo del programa...")
            global resp
            resp = False
        case _:
            print("\u274C Opción inválida.")

resp = True
while resp:
    print("\n\t\t\t...:::::MENÚ \U0001F3AC:::::...\n"
          "\t\t1. \U0001F4DD Añadir\n"
          "\t\t2. \U0001F4DB Eliminar\n"
          "\t\t3. \U0001F50D Mostrar\n"
          "\t\t4. \u2795 Agregar Características\n"
          "\t\t5. \U0001F501 Modificar Características\n"
          "\t\t6. \u274C Borrar Características\n"
          "\t\t7. \U0001F6AA Salir")
    try:
        op = int(input("\n\t\tIngresa una opción: "))
        menu(op)
    except ValueError:
        print("\u26A0 Ingresa un número válido.")


    
    
    
    
    








