"""PARTE 4"""
"""imprima el nombre de cada clave junto con el tamaño de su lista, 
y luego imprima los valores asociados dentro de la lista de cada clave.
"""

def printInfo(list):
  for key,value in list.items():
    print(f"{len(value)} {key.upper()}")
    for i in range(0, len(value)):
      print(value[i])



dojo = {
  'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
  'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)