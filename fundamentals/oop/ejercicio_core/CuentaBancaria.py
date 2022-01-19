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