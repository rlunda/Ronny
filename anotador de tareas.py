def menu():
    print("1_ agregar tarea")
    print("2_ marcar tarea")
    print("3_ listar")
    print("4_ salir")
    try:
        sel=int(input("ingresa una opcion: "))
        return sel
    except ValueError:
        print("datos incorrectos")

def agrega_tarea(lista):
    print("Agregar nueva tarea a la lista")
    x=input("ingrese nueva tarea: ")
    lista.append(x)
    print(f"la tarea {x} fue agregada exitosamente")

def lis_tarea(lista):
    for tarea in lista:
        print(f"_ {tarea}\n")

def marcar_tarea(lista):
    tarea=input("ingrese tarea a marcar: ")
    if tarea in lista:
        lista[lista.index(tarea)]= "V" + tarea
    else:
        print("La tarea ingresada no existe")

lis = []


while True:
    x=menu()
    if x==1: agrega_tarea(lis)
    elif x==2: marcar_tarea(lis)
    elif x==3: lis_tarea(lis)
    elif x==4:
        print("SALIENDO DE LA APP")
        break
    else:
        print("OPCION INCORRECTA...")

