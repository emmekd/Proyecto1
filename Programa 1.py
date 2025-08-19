Usuarios = {}
print("Cajero Automatico")

def NuevoUsuario(Nombre, ID, PIN, MontoI):
    print(f"Nombre: {Nombre}, su ID es: {ID}, Pin: ****")
    Usuarios[Nombre] = {"Id": ID, "Pin": PIN, "Monto": MontoI}

def IniciarSesion():
    try:
        buscar = input("ingrese el nombre de usuario").title()
    except ValueError:
        print("Ingrese un nombre valido")
    if buscar in Usuarios:
        contraseña = int(input("ingrese su pin"))
        if contraseña == Usuarios[buscar]["Pin"]:
            print("Se pudo iniciar sesion")
            return buscar
    else: 
        print("El usuario no existe")

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
    def retirar():
            Usuarios[usuario]['Monto'] -= Retirar
            print(f"Ha retirado {Retirar}, su saldo actual es: {Usuarios[usuario]['Monto']}")

    if usuario:
        if Retirar <= Usuarios[usuario]['Monto']:
            retirar()
        else:
            while True:
                Retirar = float(input("Ingrese un monto valido para retirar: "))
                if Retirar <= Usuarios[usuario]['Monto']:
                    retirar()
                    break
                else:
                    print("Saldo insuficiente")

while True:
    print("Ingrese una opcion")
    print("1 = Retirar dinero")
    print("2 = Ingresar dinero")
    print("3 = Consultar Saldo")
    print("4 = Cambiar pin")
    print("5 = ingresar nuevo usuario")
    print("6 = Salir")
    try:
        opcion = int(input())
    except ValueError:
        print("Ingrese una opcion valida")

    if opcion == 1:
        while True:
            retiro = float(input("Ingrese el monto que desea retirar"))
            if retiro > 0:
                break
            else:
                print("Ingrese un monto valido")
        RetirarMonto(retiro)

    elif opcion == 2:
        while True:
            MontoNuevo = int(input("Ingrese el monto que desea ingresar"))
            if MontoNuevo > 0:
                break
            else: print("Ingrese un monto valido")
        IngresarMonto(MontoNuevo)
    elif opcion == 3:
        ConsultarSaldo()
    elif opcion == 4:
        while True:
            try:
                NuevoPin = input("Ingrese su nuevo Pin: ")
                
            except ValueError:
                print("El pin solo puede estar conformado por numeros")
            if len(NuevoPin) == 4 and NuevoPin.isdigit():
                NuevoPin = int(NuevoPin)
                break
            else:
                print("El pin dee tener 4 digitos")
        CambiarPin(NuevoPin)
    elif opcion == 5:
        import random
        id = random.randint(1000000, 9999999)

        print("Ingrese su nombre")
        try:
            nombre = input().title()
        except ValueError:
            print("Ingrese un nombre valido")

        print("ingrese un pin")
        while True:
            try:
                pin = input("Ingrese un pin: ")
            except ValueError:
                print("El pin solo puede estar conformado por numeros")
            if len(pin) == 4 and pin.isdigit():
                pin = int(pin)
                break
            else:
                print("El pin debe tener 4 digitos")

        print("Ingrese su monto inicial")
        while True:
            try:
                montoI = float(input())
            except ValueError:
                print("ingrese un monto valido")
                continue
            if montoI > 0:
                break
            else:
                print("ingrese un monto valido")

        NuevoUsuario(nombre, id, pin, montoI)
    elif opcion == 6:
        break
    else:
        print("Opcion Invalida")