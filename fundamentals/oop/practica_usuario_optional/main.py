# from => archivo import => la clase
from Usuario import Usuario

guido = Usuario("Guido van Rossum", "guido@python.com")
monty = Usuario("Monty Bronx", "monty@python.com")
naty = Usuario("Naty García","natygaol@gmail.com")
print(guido)
print(monty)
print(naty)

guido.hacer_deposito(500)
guido.hacer_deposito(300)
guido.hacer_deposito(200)
guido.hacer_retiro(150)
print("User: " + guido.name + "," + " Balance: " + str(guido.balance_cuenta) )

monty.hacer_deposito(200)
monty.hacer_deposito(700)
monty.hacer_retiro(150)
monty.hacer_retiro(25)
print(f"User: {monty.name}, Balance: {monty.balance_cuenta}")

naty.hacer_deposito(1000)
naty.hacer_retiro(50)
naty.hacer_retiro(30)
naty.hacer_retiro(150)
print(f"User: {naty.name}, Balance: {naty.balance_cuenta}")

naty.transferir_dinero(280, monty)

print(f"User: {naty.name}, Balance: {naty.balance_cuenta}")
print(f"User: {monty.name}, Balance: {monty.balance_cuenta}")

naty.imprimir_balance()
# funciones o métodos siempre llevan paréntesis
# atributos: como naty.name -> se dejan sin parentesis