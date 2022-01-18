class Usuario:
  #constructor
  def __init__(self , name, email_address):
    self.name = name
    self.email = email_address
    self.balance_cuenta = 0
  
  def hacer_deposito(self, amount):
    # le sumo el dinero que solicita
    self.balance_cuenta += amount

  def hacer_retiro(self, amount):
    # le resto el dinero que solicita
    self.balance_cuenta -= amount

  def mostrar_balance_usuario(self):
    # le muestro cuanto dinero tiene actualmente llamando al balance
    return self.balance_cuenta
  
  def transferir_dinero(self, user_balance):
    