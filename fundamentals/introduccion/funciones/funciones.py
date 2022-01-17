#acá por ejemplo estamos poniendo valores por default = 0
def suma_dos_numeros(num1 = 0, num2 = 0):
  return num1 + num2

n1 = 10
n2 = 20

resultado = suma_dos_numeros()
resultado1 = suma_dos_numeros(n1, n2)
print(resultado)
print(resultado1)