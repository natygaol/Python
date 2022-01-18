# Escribe una función llamada numerosPrimos. Esta función recibe como parámetro
# un número entero positivo. La función se encarga de crear un arreglo con los
# números primos desde el 1 hasta el número proporcionado. La función retorna
# el arreglo como resultado.
# 30 => [ 1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29 ]

def numerosPrimos(num1):
  array_numeros_primos = []
  for i in range(1, num1):
    if(num1 % i > 0):
      array_numeros_primos.append(i)
    # elif(num1 / num1 == 0):
    #   array_numeros_primos.append(num1)
  print(array_numeros_primos)
  return array_numeros_primos


numerosPrimos(11)