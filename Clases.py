import random

from datetime import datetime

#Clase Base, Operaciones. 

class Operaciones: 
    def _init_(self, descripción):
        self.descripción = descripción

    #Metodo para presentar la información
    def _str_(self):
        return self.descripción
    
#subclases

#Sub clase retiro
class Retiro(Operaciones):
    def _init_(self, monto):
        super()._init_(f"Retiro de Q{monto}")
        self.monto = monto

    def ejecutar(self, cuenta):
        if cuenta.get_saldo() >= self.monto:
            cuenta.set_saldo(cuenta.get_saldo())
            cuenta.historial.append(self)
            print(f"Retiro exitoso. Nuevo Saldo: Q{cuenta.get_saldo()}")

        else: 
            print("Fondos insuficientes.")

class Deposito(Operaciones):
    def _init_(self, monto):
        super()._init_(f"Depósito de Q{monto}")
        self.monto = monto

    def ejecutar(self, cuenta):
        cuenta.set_saldo(cuenta.get_saldo() + self.monto)
        cuenta.historial.append(self)
        print(f"Depósito exitoso. Nuevo saldo: Q{cuenta.get_saldo()}")

class ConsultarSaldo(Operaciones):
    def mostrar_info(self):
        self.cuenta.agregar_historial(f"Consultar saldo: {self.cuenta.saldo}  | {self.fecha}")
        return self.cuenta.saldo
    
class CambioPIN(Operaciones):
    def mostrar_info(self, nuevPIN):
        if not nuevPIN.isdigit() or len(nuevPIN) !=4:
            raise ValueError("El pin deve ser numerico de 4 dijitos")
        self.cuenta.pin = nuevPIN
        self.cuenta.agregar_historial = (f"Cambio el PIN el {self.nuevPIN} en la fecha {self.fecha}")


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
