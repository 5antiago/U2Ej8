from Conjunto import conjunto

def Salir(con1, con2):
    pass
def Sumar(con1, con2):
    print("El conjunto resultante es {}".format(con1+con2))

def Restar(con1, con2):
    print("El conjunto resultante es {}".format(con1-con2))
def Igualdad(con1, con2):
    if con1 == con2:
        print("Los conjuntos son iguales")
    else:
        print("Los conjuntos son distintos")


switcher = {
    0: Salir,
    1: Sumar,
    2: Restar,
    3: Igualdad,
}

if __name__ == '__main__':
    con1 = conjunto(list(map(int, input("Ingrese numeros del primero conjunto, separados por comas: ").split(","))))
    con2 = conjunto(list(map(int, input("Ingrese numeros del segundo conjunto, separados por comas: ").split(",")))) 
    opcion=1 
    while opcion != 0:
        print(" 1. Sumar conjuntos \n 2. Restar Conjuntos \n 3. Igualdad de conjuntos \n 0. Salir")
        opcion= int(input("Ingrese una opción: "))
        switcher.get(opcion, lambda: print("Opción incorrecta"))(con1, con2)