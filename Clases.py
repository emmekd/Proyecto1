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
