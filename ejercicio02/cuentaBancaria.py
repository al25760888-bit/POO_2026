class CuentaBancaria:
    def __init__(self, titular,numeroCuenta,saldo):
        self.titular=titular
        self.numeroCuenta=numeroCuenta
        self.saldo=saldo
        
    def depositar(self,cantidad):
        self.saldo=self.saldo+cantidad
        
    def retirar(self,cantidad):
        if cantidad <=self.saldo:
            self.saldo=self.saldo-cantidad
            return cantidad
        else:
          print ("saldo insuficiente")
        
    def consultarSaldo(self):
        
        return self.saldo
    def mostrarInformacion(self):
        return f"{self.titular} tienes {self.saldo}"
    
    # Crear una cuenta
cuenta1 = CuentaBancaria("Juan Pérez", "001234567", 1000.0)
cuenta2 = CuentaBancaria("Garritas Gomez", "1749925", 20000.0)

# Realizar operaciones
cuenta1.depositar(500.0)
print(cuenta1.mostrarInformacion())  # Titular: Juan Pérez, Saldo: $1500.0

cuenta1.retirar(250.0)
print(f"Saldo actual: ${cuenta1.consultarSaldo()}")  # Saldo actual: $1300.0



print("------------------------------------")


cuenta2.depositar(600.0)
print(cuenta2.mostrarInformacion())  

cuenta2.retirar(500.0)
print(f"Saldo actual: ${cuenta2.consultarSaldo()}")  

