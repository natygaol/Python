# Escribe una función llamada numerosPrimos. Esta función recibe como parámetro
# un número entero positivo. La función se encarga de crear un arreglo con los
# números primos desde el 1 hasta el número proporcionado. La función retorna
# el arreglo como resultado.
# 30 => [ 1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29 ]

def esPrimo(num2):
  cont = 0
  if num2 == 1:
    return True
  for x in range(1, num2 + 1):
    if num2 % x == 0:
      cont += 1
  if cont == 2:
    return True
  else:
    return False

def numerosPrimos(num1):
  array_numeros_primos = []
  for i in range(1, num1 + 1):
    if(num1 % i != 0):
      array_numeros_primos.append(i)
    # elif(num1 / num1 == 0):
    #   array_numeros_primos.append(num1)
  return array_numeros_primos

# cuando hay un return, capturo ese return en una variable
resultado_final = numerosPrimos(11)
print(resultado_final)

def numerosPrimos(num1):
  array_numeros_primos = []
  for i in range(1, num1 + 1):
    if esPrimo(i) == True:
      array_numeros_primos.append(i)
  return array_numeros_primos

resultado = numerosPrimos(30)
print(resultado)