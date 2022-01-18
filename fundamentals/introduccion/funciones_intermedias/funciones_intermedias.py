x = [ [5,2,3], [10,8,9] ]

estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]


"""PARTE 1"""
# Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].
x[1][0] = 15
print(x)

# Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
estudiantes[0]["last_name"] = "Bryant"
print(estudiantes)

# En el directorio_deportes, cambia "Messi" por "Andrés".
directorio_deportes["fútbol"][0] = "Andrés"
print(directorio_deportes)

# Cambia el valor 20 en z a 30.
z[0]["y"] = 30
print(z)


"""PARTE 2"""

"""Crea una función iterateDictionary(some_list)para que, dada una lista de diccionarios, 
la función recorra cada diccionario de la lista e 
imprima cada llave y el valor asociado. """

def iterateDictionary(some_list):
  for dictionary in some_list:
    names = ""
    for element in dictionary:
      names += element + ' - ' +  dictionary[element]
      if(names == "last_name"):
        names += ""
      else:
        names += ","
    print(names)

estudiantes1 = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(estudiantes1)



"""PARTE 3"""

""" dada una lista de diccionarios y un nombre de clave, 
la función imprima el valor almacenado en esa clave para cada diccionario. 
Por ejemplo, iterateDictionary2('name', estudiantes) 
Michael
John
Mark
KB"""
def iterateDictionary2(key_name, some_list):
  for i in range(0, len(some_list)):
    # some_list[i] == {'first_name': 'KB', 'last_name': 'Tonel'}
    for key,value in some_list[i].items():
      # acá como estoy dentro del array, print(some_list[i].items()) => dict_items([('first_name', 'KB'), ('last_name', 'Tonel')])
      if(key == key_name):
        print(value)

iterateDictionary2('first_name', estudiantes1)
iterateDictionary2('last_name', estudiantes1)


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