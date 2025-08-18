Usuarios = {}
print("Cajero Automatico")

def NuevoUsuario(Nombre, ID, PIN, MontoI):
    print(f"Nombre: {nombre}, ID: {id}, Pin: ****")
    Usuarios[Nombre] = {"Id" : ID, "Pin": PIN, "Monto": MontoI}

while True:
    print("Ingrese una opcion")
    print("1 = Retirar dinero")
    print("2 = Ingresar dinero")
    print("3 = Consultar Saldo")
    print("4 = Cambiar pin")
    print("5 = ingresar nuevo usuario")
    print("5 = Salir")
    opcion = int(input())

    if opcion == 1:
        print()
    elif opcion == 2:
        print()
    elif opcion == 3:
        print()
    elif opcion == 4:
        print()
    elif opcion == 5:
        import random
        id = random.randint(1000000, 9999999)

        print("Ingrese su nombre")
        nombre = input().title()

        print("ingrese un pin")
        pin = int(input())

        print("Ingrese su monto inicial")
        montoI = float(input())

        NuevoUsuario(nombre, id, pin, montoI)
    elif opcion == 6:
        break