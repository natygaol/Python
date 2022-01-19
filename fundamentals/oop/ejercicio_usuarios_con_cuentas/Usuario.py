class Usuario:
  #constructor
  def __init__(self , name):
    self.name = name
    self.cuenta = CuentaBancaria(0.05, 1000 )

  def mostrar_balance_usuario(self):
    # le muestro cuanto dinero tiene actualmente llamando al balance
    return self.balance_cuenta

  def imprimir_balance(self):
    print(f"User: {self.name}, Balance: {self.cuenta.imprimir_todas_las_cuentas()}")

  def transferir_dinero(self, amount_to_transfer, user ):
    self.balance_cuenta -= amount_to_transfer
    user.balance_cuenta += amount_to_transfer
    
# self es referencia a la instancia - al objeto mismo
# cls es referencia a la clase

# ******* CUENTA BANCARIA************

class CuentaBancaria:
  todas_las_cuentas = []

  def __init__(self, tasa, balance ):
    self.tasa = tasa
    self.balance = balance
    CuentaBancaria.todas_las_cuentas.append(self)

  def deposito(self, amount):
    self.balance += amount
    return self

  def retiro(self, amount):
    if( self.balance - amount ) >= 0:
      self.balance += amount
    else:
      print("No tienes dinero en tu cuenta")
    return self

  def mostrar_info_cuenta(self):
    print(f"Balance: {self.balance}")
    return self

  def genera_interes(self):
    if(self.balance) > 0 :
      self.balance += (self.balance * self.tasa)
    return self
  
  @classmethod
  def imprimir_todas_las_cuentas(cls):
    for cuenta in cls.todas_las_cuentas:
        cuenta.mostrar_info_cuenta()