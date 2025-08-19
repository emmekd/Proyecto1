Usuarios = {}
print("Cajero Automatico")

def NuevoUsuario(Nombre, ID, PIN):
    if nombre in Usuarios: #Validacion de usuarios repetitivos
        print("Este usuario ya existe")
    else:
        print(f"Nombre: {nombre}, ID: {id}, Pin: ****")
        Usuarios[nombre] = {"Id" : id, "Pin": pin}

while True:
    print("Ingrese una opcion")
    print("1 = Retirar dinero")
    print("2 = Ingresar dinero")
    print("3 = Consultar Saldo")
    print("4 = Cambiar pin")
    print("5 = ingresar nuevo usuario")
    print("6 = Salir")

    try:
        opcion = int(input("Seleccione una opcion "))
    except ValueError:
        print("Opción invalida. Ingrese un número de 1 a 6")
        continue
    if opcion in [1, 2, 3, 4]:
        if not Usuarios:
            print("No hay usuarios registrados.")
            continue

        nombre = input("Ingrese su nombre: ").title()
        if nombre not in Usuarios:
            print("Usuario no encontrado.")
            continue

        try:
            pin = int(input("Ingrese su PIN: "))
        except ValueError:
            print("El PIN debe ser numérico.")
            continue

        if Usuarios[nombre]["Pin"] != pin:
            print("PIN incorrecto.")
            continue

    if opcion == 1:
        try:
            monto = float(input("Ingrese un monto a retirar "))
            if monto <= 0:
                print("El monto debe ser positivo.")
            elif monto > Usuarios[nombre]["Saldo"]:
                print("Fondos insuficientes.")
            else:
                Usuarios[nombre]["Saldo"] -= monto
                print(f"Retiro exitoso. Saldo {Usuarios[nombre]['Saldo']}")
        except ValueError:
            print("El monto debe se numérico")

    elif opcion == 2:
        try:
            monto = float(input("Ingrese monto a depositar: "))
            if monto <= 0:
                    print("El monto debe ser positivo.")
            else:
                Usuarios[nombre]["Saldo"] += monto
                print(f"Depósito exitoso. Saldo: {Usuarios[nombre]['Saldo']}")
        except ValueError:
            print("El monto debe ser numérico.")

    elif opcion == 3:
        print(f"Saldo de {nombre}: {Usuarios[nombre]} Saldo")
    
    elif opcion == 4:
         try:
                nuevo_pin = int(input("Ingrese nuevo PIN (4 dígitos): "))
                if len(str(nuevo_pin)) != 4:
                    print("El PIN debe tener 4 dígitos.")
                else:
                    Usuarios[nombre]["Pin"] = nuevo_pin
                    print("PIN actualizado correctamente.")
         except ValueError:
                print("El PIN debe ser numérico.")

    elif opcion == 5:
        import random
        id = random.randint(1000000, 9999999)

        nombre = input("Ingrese su nombre: ").title()

        try:
            pin = int(input("Ingrese su PIN (4 dijitos.)"))
            if len(str(pin)) !=4:
                print("El PIN debe tener 4 díjitos")
                continue
        except ValueError:
            print("El PIN debe ser numerico")
            continue

        NuevoUsuario(nombre, id, pin)
    elif opcion == 6:
        print("Saliendo del cajero")
        break
    else:
        print("Opcion no valida intente de nuevo")