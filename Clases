Usuarios = {}

contador_id = 1000000  # ID inicial

class Cuenta:
    def __init__(self, Nombre, Id, Pin, Saldo):
        self.Nombre = Nombre
        self.Id = Id
        self.__Pin = Pin
        self.__Saldo = Saldo
    def NuevoUsuario(self):
        Usuarios[self.Nombre] = {
            "ID": self.Id,
            "Pin": self.__Pin,
            "Saldo": self.__Saldo}
    def get(self):
        print(f"Saldo: {self.__Saldo}")
    def set(self):
        def retirar(nuevo):
            self.__Saldo -= nuevo
            print(f"saldo: {self.__Saldo}")
        def depositar(nuevo):
            self.__Saldo += nuevo
            print(f"saldo: {self.__Saldo}")

        monto = int(input("Ingrese el monto"))
        opcion = int(input("Desea depositar o retirar?(1 = R, 2 = D)"))
        if opcion == 1:
            retirar(monto)
        if opcion == 2:
            depositar(monto)

C = Cuenta("Juan", 123456, 1234, 1000)
C.NuevoUsuario()
C.get()
C.set()

