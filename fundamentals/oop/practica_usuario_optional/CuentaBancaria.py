class CuentaBancaria:
  # atributo de clase
  nombre_banco = "Primer Dojo Nacional"
  todas_las_cuentas = []
  
  def __init__(self, tasa_int, balance):
    self.tasa_int = tasa_int
    self.balance = balance
    # llamo a la clase y hago un push de las instancias, por eso pongo self
    CuentaBancaria.todas_las_cuentas.append(self)
  
  # método de clase para cambiar el nombre del banco
  @classmethod
  # Para métodos de clase, debo pasar en vez de self, **cls**
  def cambiar_nombre_banco(cls, name):
    cls.nombre_banco = name
  
  # método de clase para obtener balance de todas las cuentas
  @classmethod
  def todos_los_balances(cls):
    sum = 0
    for cuenta in cls.todas_las_cuentas:
      sum += cuenta.balance
    return sum

  def re_tiro(self,amount):
    # podemos usar el método estático aquí para evaluar
    # si podemos retirar los fondos sin quedar con balance negativo
    if CuentaBancaria.puede_retirar(self.balance, amount):
        self.balance -= amount
    else:
        print("Fondos insuficientes")
    return self

  # los métodos estáticos no tienen acceso a ningún atributo
  # solo a lo que se le pasa
  @staticmethod
  def puede_retirar(balance,amount):
    if (balance - amount) < 0:
      return False
    else:
      return True


