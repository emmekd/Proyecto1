import random

Usuarios = {}
class Cuenta:
    def __init__(self, Nombre, Id, Pin, Saldo):
        self.Nombre = Nombre
        self.Id = Id
        self.__Pin = Pin
        self.__Saldo = Saldo
    def NuevoUsuario(self):
        rand = random.randint(1000000, 9999999)

        self.Id = rand
        Usuarios[self.Nombre] = {
            "ID": self.Id,
            "Pin": self.__Pin,
            "Saldo": self.__Saldo}
    def get(self):
        print(f"Nombre: {self.Nombre}")
        print(f"Id: {self.Id}")
        print(f"Saldo: {self.__Saldo}")
    def set(self):
        def retirar(nuevo):
            self.__Saldo -= nuevo
            print(f"saldo: {self.__Saldo}")
        def depositar(nuevo):
            self.__Saldo += nuevo
            print(f"saldo: {self.__Saldo}")
        while True:
            try:
                monto = int(input("Ingrese el monto"))
            except ValueError:
                print("Ingrese un monto valido")
            if monto > 0:
                break
        while True:
            try:
                opcion = int(input("Desea depositar o retirar?(1 = R, 2 = D)"))
            except ValueError:
                print("ingrese una opcion valida")
            if opcion == 1 or opcion == 2:
                break
        if opcion == 1:
            retirar(monto)
        if opcion == 2:
            depositar(monto)

C = Cuenta("Juan", None, 1234, 1000)
C.NuevoUsuario()
C.get()
C.set()

