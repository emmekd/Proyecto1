#Flujo Principal

#Diccionario de Usuario
Usuarios = {}
contador_id = 1000000  # ID inicial

print("--- Cajero Automático ---")

def NuevoUsuario(nombre, id, pin, montoI=0):
    if nombre in Usuarios:
        print("El usuario ya existe.")
    else:
        Usuarios[nombre] = {"Id": id, "Pin": pin, "Saldo": montoI}
        print(f"Usuario creado: {nombre}, ID: {id}, Pin: ****, Saldo inicial: Q{montoI:.2f}")

while True:
    print("\nOpciones:")
    print("1 = Retirar dinero")
    print("2 = Ingresar dinero")
    print("3 = Consultar saldo")
    print("4 = Cambiar PIN")
    print("5 = Crear nuevo usuario")
    print("6 = Salir")

    try:
        opcion = int(input("Opción: "))
    except ValueError:
        print("Debe ingresar un número del 1 al 6.")
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

        if opcion == 1:  # Retirar
            try:
                monto = float(input("Monto a retirar: "))
                if monto <= 0:
                    print("El monto debe ser positivo.")
                elif monto > Usuarios[nombre]["Saldo"]:
                    print("Fondos insuficientes.")
                else:
                    Usuarios[nombre]["Saldo"] -= monto
                    print(f"Retiro exitoso. Saldo actual: Q{Usuarios[nombre]['Saldo']:.2f}")
            except ValueError:
                print("Monto inválido.")

        elif opcion == 2:  # Ingresar
            try:
                monto = float(input("Monto a depositar: "))
                if monto <= 0:
                    print("El monto debe ser positivo.")
                else:
                    Usuarios[nombre]["Saldo"] += monto
                    print(f"Depósito exitoso. Saldo actual: Q{Usuarios[nombre]['Saldo']:.2f}")
            except ValueError:
                print("Monto inválido.")

        elif opcion == 3:  # Consultar saldo
            print(f"Saldo de {nombre}: Q{Usuarios[nombre]['Saldo']:.2f}")

        elif opcion == 4:  # Cambiar PIN
            try:
                nuevo_pin = int(input("Ingrese nuevo PIN (4 dígitos): "))
                if len(str(nuevo_pin)) != 4:
                    print("El PIN debe tener 4 dígitos.")
                else:
                    Usuarios[nombre]["Pin"] = nuevo_pin
                    print("PIN actualizado correctamente.")
            except ValueError:
                print("PIN inválido.")

    elif opcion == 5:  # Crear usuario
        nombre = input("Ingrese su nombre: ").title()
        try:
            pin = int(input("Ingrese un PIN (4 dígitos): "))
            if len(str(pin)) != 4:
                print("El PIN debe tener 4 dígitos.")
                continue
        except ValueError:
            print("PIN inválido.")
            continue

        try:
            montoI = float(input("Ingrese monto inicial: "))
            if montoI < 0:
                print("El monto inicial no puede ser negativo.")
                continue
        except ValueError:
            print("Monto inicial inválido.")
            continue

        NuevoUsuario(nombre, contador_id, pin, montoI)
        contador_id += 1  # Incrementa ID automáticamente

    elif opcion == 6:
        print("Saliendo del cajero.")
        break

    else:
        print("Opción no válida. Intente otra vez.")