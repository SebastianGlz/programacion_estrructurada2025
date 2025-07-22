
peliculas = []
import mysql.connector
from mysql.connector import Error
#DICT U OBJETO para almacenar los atributos (nombre, categoria, clasificacion, genero, idioma)

#            "nombre":"",
#           "categoria":"",
#            "clasificacion":"",
#            "genero":"idioma",
#            }

pelicula={}

def borrarpantalla():
    import os
    os.system("cls")


def esperartecla():
    input("\t Oprima cualquier tecla para continuar ...")

def conectar():
    try:
     conexion = mysql.connector.connect(
     host="localhost",
     user="root",
     password="",
      database="db_peliculas")
     return conexion
    except Error as e:
        print(f"\n\t \U0001F4A5 Error al conectar a la base de datos: {e}")
        return None

#agregar registro a la base de datos


def crearPeliculas():
    borrarpantalla()
    conexion = conectar()
    if conexion != None:
        print("\n\t.::\U0001F4DD Alta de Peliculas \U0001F4DD::. ")
    pelicula.update({"nombre":input("Ingresa el nombre: ".upper().strip())}) 
    pelicula.update({"categoria":input("Ingresa la categoria: ".upper().strip())}) 
    pelicula.update({"clasificacion":input("Ingresa la clasificacion: ".upper().strip())}) 
    pelicula.update({"genero":input("Ingresa el genero: ".upper().strip())}) 
    pelicula.update({"idioma":input("Ingresa el idioma: ".upper().strip())}) 
    input("\n\t\t :::\u2705 LA OPERACION SE REALIZO CON EXITO! \u2705:::")

    try:
        cursor=conexion.cursor()
        sql="insert into peliculas(id, nombre, categoria, clasificacion, genero, idioma) values(NULL, %s, %s, %s, %s, %s)"
        val=(pelicula["nombre"], pelicula["categoria"], pelicula["clasificacion"], pelicula["genero"], pelicula["idioma"])
        cursor.execute(sql,val)
        conexion.commit()
        print("\n\t \U0001F4DD Registro agregado correctamente a la base de datos")
    except Error as e:
        print("Error al insertar el registro en la base de datos: ", e)


def mostrarPeliculas():
    borrarpantalla()
    conexion = conectar()
    if conexion != None:
        print("\n\t .::\U0001F50D Mostrar Peliculas \U0001F50D::.\n")
        cursor = conexion.cursor()
        sql = "SELECT * FROM peliculas"
        cursor.execute(sql)
        registros = cursor.fetchall()
        if registros:
            print("\n\t\t .:: \U0001F4C8 Lista de Peliculas ::.\n")
            print(f"{'ID':<15} {'Nombre':<15} {'Categoria':<15} {'Clasificacion':<15} {'Genero':<15} {'Idioma':<15}")
            print("="*90)
            for fila in registros:
                print(f"{fila[0]:<15} {fila[1]:<15} {fila[2]:<15} {fila[3]:<15} {fila[4]:<15} {fila[5]:<15}")
                print("="*90)
        else:
            print("\n\t \U0001F4A5 No hay peliculas registradas en la base de datos.")

def modificarPeliculas():
    borrarpantalla()
    conexion = conectar()
    if conexion != None:
        print("\n\t .::\U0001F501 Modificar Peliculas \U0001F501::.\n")
        cursor = conexion.cursor()
        nombre= input("Dame el nombre de la pelicula a modificar: ").upper().strip()
        sql = "SELECT * FROM peliculas where nombre= %s"
        val=(nombre,)
        cursor.execute(sql,val)
        registros = cursor.fetchall()
        if registros:
            print("\n\t\t .:: \U0001F4C8 Lista de Peliculas ::.\n")
            print(f"{'ID':<15} {'Nombre':<15} {'Categoria':<15} {'Clasificacion':<15} {'Genero':<15} {'Idioma':<15}")
            print("="*90)
            for fila in registros:
                print(f"{fila[0]:<15} {fila[1]:<15} {fila[2]:<15} {fila[3]:<15} {fila[4]:<15} {fila[5]:<15}")
                print("="*90)
            resp=input(f"\n\t¿Deseas modificar la pelicula {nombre}? (Si/No): ").lower().strip()
            if resp == "si":
                atributo=input("Escribe el atributo que deseas modificar: ").lower().strip()
                valor=input("Escribe el nuevo valor del atributo: ").upper().strip()
                sql=f"UPDATE peliculas SET {atributo}= %s WHERE nombre= %s"
                val=(valor, nombre)
                cursor.execute(sql,val)
                conexion.commit()
                print("\n\t\t .:: \u2705 ¡LA OPERACION SE REALIZO CON EXITO! \u2705::.")
            else:
                print("\n\t\t .:: \U0001F4A5 No se realizo ninguna modificacion ::.")
        else:
            print("\n\t \U0001F4A5 No hay peliculas registradas en la base de datos.")

def buscarPeliculas():
    borrarpantalla()
    conexion = conectar()
    if conexion != None:
        print("\n\t .::\U0001F50D Mostrar Peliculas \U0001F50D::.\n")
        cursor = conexion.cursor()
        nombre= input("Dame el nombre de la pelicula a buscar: ").upper().strip()
        sql = "SELECT * FROM peliculas where nombre= %s"
        val=(nombre,)
        cursor.execute(sql,val)
        registros = cursor.fetchall()
        if registros:
            print("\n\t\t .:: \U0001F4C8 Lista de Peliculas ::.\n")
            print(f"{'ID':<15} {'Nombre':<15} {'Categoria':<15} {'Clasificacion':<15} {'Genero':<15} {'Idioma':<15}")
            print("="*90)
            for fila in registros:
                print(f"{fila[0]:<15} {fila[1]:<15} {fila[2]:<15} {fila[3]:<15} {fila[4]:<15} {fila[5]:<15}")
                print("="*90)
        else:
            print("\n\t \U0001F4A5 No hay peliculas registradas en la base de datos.")

def borrarPeliculas():
    borrarpantalla()
    conexion = conectar()
    if conexion != None:
        print("\n\t .::\U0001F50D Borrar Peliculas \U0001F50D::.\n")
        cursor = conexion.cursor()
        nombre= input("Dame el nombre de la pelicula a borrarr: ").upper().strip()
        sql = "SELECT * FROM peliculas where nombre= %s"
        val=(nombre,)
        cursor.execute(sql,val)
        registros = cursor.fetchall()
        if registros:
           resp=input(f"Deseas borrar la pelicula {nombre} del sistema? (Si/No): ").lower().strip()
           if resp == "si":
               sql="delete from peliculas where nombre = %s"
               val=(nombre,)
               cursor.execute(sql,val)
               conexion.commit()
        else:
            print("\n\t \U0001F4A5 No hay peliculas registradas en la base de datos.")