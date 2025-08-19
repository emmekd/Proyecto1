import random

Usuarios = {}
print("Cajero Automático")

def NuevoUsuario(nombre, id, pin):
    if nombre in Usuarios:
        print("El usuario ya existe")
    else:
        Usuarios[nombre] = {"Id": id, "Pin": pin, "Saldo": 0}  # saldo inicial
        print(f"Usuario creado: {nombre}, ID: {id}, Pin: ****")

while True:
    print("\nIngrese una opción")
    print("1 = Retirar dinero")
    print("2 = Ingresar dinero")
    print("3 = Consultar Saldo")
    print("4 = Cambiar PIN")
    print("5 = Ingresar nuevo usuario")
    print("6 = Salir")

    try:
        opcion = int(input("Opción: "))
    except ValueError:
        print("Debe ingresar un número (1-6).")
        continue

    # Opciones que requieren usuario
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

        # Acciones según opción
        if opcion == 1:  # Retirar
            try:
                monto = float(input("Ingrese monto a retirar: "))
                if monto <= 0:
                    print("El monto debe ser positivo.")
                elif monto > Usuarios[nombre]["Saldo"]:
                    print("Fondos insuficientes.")
                else:
                    Usuarios[nombre]["Saldo"] -= monto
                    print(f"Retiro exitoso. Saldo: {Usuarios[nombre]['Saldo']}")
            except ValueError:
                print("El monto debe ser numérico.")

        elif opcion == 2:  # Ingresar
            try:
                monto = float(input("Ingrese monto a depositar: "))
                if monto <= 0:
                    print("El monto debe ser positivo.")
                else:
                    Usuarios[nombre]["Saldo"] += monto
                    print(f"Depósito exitoso. Saldo: {Usuarios[nombre]['Saldo']}")
            except ValueError:
                print("El monto debe ser numérico.")

        elif opcion == 3:  # Consultar saldo
            print(f"Saldo de {nombre}: {Usuarios[nombre]['Saldo']}")

        elif opcion == 4:  # Cambiar PIN
            try:
                nuevo_pin = int(input("Ingrese nuevo PIN (4 dígitos): "))
                if len(str(nuevo_pin)) != 4:
                    print("El PIN debe tener 4 dígitos.")
                else:
                    Usuarios[nombre]["Pin"] = nuevo_pin
                    print("PIN actualizado correctamente.")
            except ValueError:
                print("El PIN debe ser numérico.")

    elif opcion == 5:  # Crear usuario
        id = random.randint(1000000, 9999999)
        nombre = input("Ingrese su nombre: ").title()

        try:
            pin = int(input("Ingrese un PIN (4 dígitos): "))
            if len(str(pin)) != 4:
                print("El PIN debe tener 4 dígitos.")
                continue
        except ValueError:
            print("El PIN debe ser numérico.")
            continue

        NuevoUsuario(nombre, id, pin)

    elif opcion == 6:
        print("Saliendo del cajero...")
        break

    else:
        print("Opción no válida. Intente otra vez.")
