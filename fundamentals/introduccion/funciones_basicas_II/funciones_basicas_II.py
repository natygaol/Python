# def lista_regresiva(numero):
#   array = []
#   for i in range(numero, 0, -1):
#     print(i)
#     array.append(i)
#   return array

# print(lista_regresiva(5))


# [2,3]
# def recibe_dos_numeros(lista):
#   print(lista[0])
#   return lista[1]

# array = [1,2]
# print(recibe_dos_numeros(array))


# array = [1,2,3,4,5]
# def recibe_array(array):
#   suma = array[0]
#   tamaño_array = len(array)
#   return suma + tamaño_array

# array = [1,2,3,4,5]
# print(recibe_array(array))


#def mayores_valores_que_el_seguno(lista_2):
  #acepto una lista
  #crear nueva lista x > 

""" La función debe crear y devolver una lista cuya longitud sea igual al tamaño dado, y cuyos valores sean todos el valor dado.
Ejemplo: length_and_value(4,7) debe devolver [7,7,7,7]
Ejemplo: length_and_value(6,2) debe devolver [2,2,2,2,2,2]"""

def repito_valores(tamaño, valor):
  array_numeros = []
  for i in range(0, tamaño):
    array_numeros.append(valor)
  return array_numeros

print(repito_valores(4,7))
