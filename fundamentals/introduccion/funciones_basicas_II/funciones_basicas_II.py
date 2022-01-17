def lista_regresiva(numero):
  array = []
  for i in range(numero, 0, -1):
    print(i)
    array.append(i)
  return array

print(lista_regresiva(5))
