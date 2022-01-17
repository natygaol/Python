
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
      # if(element == "last_name"):
      #   ""
      
    #first_name - Michael, last_name - Jordan


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
# def iterateDictionary2(key_name, some_list):
#   for dictionary in some_list:
#     # {'first_name': 'Michael', 'last_name': 'Jordan'} me da key/value
#     for key_name in dictionary:
#       print(dictionary[key_name])


# iterateDictionary2("first_name", estudiantes1)
