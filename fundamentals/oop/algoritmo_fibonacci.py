# Escribe una función llamada fibonacci. Esta función recibe como parámetro un 
# número entero positivo. La función se encarga de imprimir la serie de fibonacci.
# El número recibido como parámetro es la cantidad de números a imprimir.
# 30 => [ 1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29 ]


def fibonacci(num):
  x1 = 0
  x2 = 1
  for i in range(0, num):
    if(i % 2 == 0):
      print(x1)
      x1 += x2
    else:
      print(x2)
      x2 += x1


fibonacci(10)