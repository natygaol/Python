from Persona import Persona

# nombre = input( "Proporciona tu nombre:")

# print( f"Bienvenido: {nombre}" )

print("*****Menu*******")
print("1. Agregar una persona")
print("2. Mostrar listas de personas")
print("3. Terminar el Programa")


opcion = input( "Opcion a elegir:")

while opcion != "3":
  if opcion == "1":
    nombre = input("Dame el nombre de la persona: ")
    apellido = input("Dame el apellido de las personas: ")
    nueva_persona = Persona(nombre, apellido)
  elif opcion == "2":
    print("lista de personas")
    Persona.imprime_lista_personas()
  else:
    print("Opción incorrecta")
  print("*****Menu*******")
  print("1. Agregar una persona")
  print("2. Mostrar listas de personas")
  print("3. Terminar el Programa")
  
  opcion = input( "Opcion a elegir:")