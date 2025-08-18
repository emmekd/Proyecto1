
Usuarios = {}
print("Cajero Automatico")

def NuevoUsuario(Nombre, ID, PIN):
    print(f"Nombre: {nombre}, ID: {id}, Pin: ****")
    Usuarios[nombre] = {"Id" : id, "Pin": pin}

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
        if pin in Usuarios.values():
            cantidad=int(input("Ingrese la cantidad que desea retirar"))
            if cantidad >= 0 and cantidad <= saldo:
                print(f"Cantidad retirada: {cantidad}")
        else:
            print("PIN incorrecto")
        
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
        
        NuevoUsuario(nombre, id, pin)
    elif opcion == 6:
        break