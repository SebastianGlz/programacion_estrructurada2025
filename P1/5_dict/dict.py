'''es un tipo de dato que se utiliza para almacenar datos de diferente tipo de datos pero en lugar de tener como las listas indices numericos tiene alfanumericos es decir: algo parecido como los objetos 
tambien se conoce como un arreglo asosiativo u objeto json
el diccionario es una coleccion ordenada y modificable no hay miembros duplicados.'''
import os
os.system("cls")


#Lista de paises
#paises=["Mexico", "Brasil", "Canada", "España"]

#Diccionario de paises

paises_mex={"nombre":"Mexico", 
        "capital":"CDMX", 
        "poblacion":"12600000",
        "idioma":"Español",
         "Status":True }


paises_bra={"nombre":"Brasil",
        "capital":"Brasilia", 
        "poblacion":"213000000",
        "idioma":"Portugues",
         "Status":True }


paises_can={"nombre":"Canada",
            "capital":"Ottawa",
            "poblacion":"38000000",
            "idioma":["Ingles y Frances"],
            "Status":False}

alumnos_1={
    "nombre":"Alondra",
    "Apellido1":"Gonzalez",
    "Apellido2":"Cabral",
    "Edad":"18",
    "Carrera":"Programacion",
    "Matricula":"3141240153",
    "Modalidas":"Bilingue",
    "Cuatrimestre":"2"}



for i in alumnos_1:
    print(f"{i}=alumnos_1[i]")

alumnos_1["telefono"]="6181234567"
for i in alumnos_1:
    print(f"{i}={alumnos_1[i]}")
print("--------------------------------------------------")