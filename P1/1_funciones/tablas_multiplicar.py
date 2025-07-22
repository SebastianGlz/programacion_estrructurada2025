'''Crear un programa que calcule e imprima cualquier tabla de multiplicar
con funciones que regrese valor y utilice parametros'''
numero=int(input("dame el numero de la tabla de multiplicar: "))
multi=numero*(1)
print("Tabla de multiplicar del 2")
print(f"{numero} x 1 ={multi}")
print(f"{numero} x 2 ={multi}")
print(f"{numero} x 3 ={multi}")
print(f"{numero} x 4 ={multi}")
print(f"{numero} x 5 ={multi}")
print(f"{numero} x 6 ={multi}")
print(f"{numero} x 7 ={multi}")
print(f"{numero} x 8 ={multi}")
print(f"{numero} x 9 ={multi}")
print(f"{numero} x 10 = {multi}")

numero=int(input("dame el numero de la tabla de multiplicar: "))
for i in range(1,11):
    multi=numero*i
    print(f"{numero} x {i} = {multi}")


numero=int(input("dame el numero de la tabla de multiplicar: "))
while i<=10:
    multi=numero*i
    print(f"{numero} x {i} = {multi}")
    i+=1

    '''Crear un programa que calcule e imprima cualquier tabla de multiplicar
con funciones que regrese valor y utilice parametros'''
def tabla_multiplicar(numero, limite=10):
    for i in range(1, limite + 1):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
    return resultado




