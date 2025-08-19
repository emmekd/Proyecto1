Usuarios = {}
print("Cajero Automatico")

def NuevoUsuario(Nombre, ID, PIN, MontoI):
    print(f"Nombre: {Nombre}, su ID es: {ID}, Pin: ****")
    Usuarios[Nombre] = {"Id": ID, "Pin": PIN, "Monto": MontoI}

def IniciarSesion():
    buscar = input("ingrese el nombre de usuario").title()
    if buscar in Usuarios:
        contraseña = int(input("ingrese su pin"))
        if contraseña == Usuarios[buscar]["Pin"]:
            print("Se pudo iniciar sesion")
            return buscar

def ConsultarSaldo():
    usuario = IniciarSesion()
    if usuario:
        print(f"Su saldo es {Usuarios[usuario]['Monto']}")

def CambiarPin(NuevoPin):
    usuario = IniciarSesion()
    if usuario:
        Usuarios[usuario]['Pin'] = NuevoPin

def IngresarMonto(NuevoMonto):
    usuario = IniciarSesion()
    if usuario:
        Usuarios[usuario]['Monto'] += NuevoMonto

def RetirarMonto(Retirar):
    usuario = IniciarSesion()
    if usuario:
        Usuarios[usuario]['Monto'] -= Retirar
        print(f"Ha retirado {Retirar}, su saldo actual es: {Usuarios[usuario]['Monto']}")

while True:
    print("Ingrese una opcion")
    print("1 = Retirar dinero")
    print("2 = Ingresar dinero")
    print("3 = Consultar Saldo")
    print("4 = Cambiar pin")
    print("5 = ingresar nuevo usuario")
    print("6 = Salir")
    opcion = int(input())

    if opcion == 1:
        retiro = int(input("Ingrese el monto que desea retirar"))
        RetirarMonto(retiro)
    elif opcion == 2:
        MontoNuevo = int(input("Ingrese el monto que desea ingresar"))
        IngresarMonto(MontoNuevo)
    elif opcion == 3:
        ConsultarSaldo()
    elif opcion == 4:
        NuevoPin = int(input("Ingrese su nuevo Pin: "))
        CambiarPin(NuevoPin)
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