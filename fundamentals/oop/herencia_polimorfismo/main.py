from Persona import Persona
from Estudiante import Estudiante

# nombre = input( "Proporciona tu nombre:")

# print( f"Bienvenido: {nombre}" )

naty = Estudiante("Naty", "García", 12345, "Python")
naty.informacion()
naty.asignaCalificacion(9.6)

#naty.informacionEstudiante()

print("*****Menu*******")
print("1. Agregar una persona: ")
print("2. Mostrar listas de personas: ")
print("3. Agregar un estudiante: ")
print("4. Mostrar listas de estudiantes: ")
print("5. Terminar el Programa: ")


opcion = input( "Opcion a elegir: ")

while opcion != "5":
  if opcion == "1":
    nombre = input("Dame el nombre de la persona: ")
    apellido = input("Dame el apellido de las personas: ")
    nueva_persona = Persona(nombre, apellido)
  elif opcion == "2":
    print("lista de personas")
    Persona.imprime_lista_personas()
  elif opcion == "3":
    nombre = input("Dame el nombre del estudiante: ")
    apellido = input("Dame el apellido del estudiante: ")
    id = input("Dame el id del estudiante: ")
    curso = input("Dame el curso del estudiante: ")
    nuevo_estudiante = Estudiante(nombre, apellido, id, curso)
  elif opcion == "4":
    print("lista de estudiantes")
    Estudiante.imprime_lista_estudiantes()
  else:
    print("Opción incorrecta")
  print("*****Menu*******")
  print("1. Agregar una persona: ")
  print("2. Mostrar listas de personas: ")
  print("3. Agregar un estudiante: ")
  print("4. Mostrar listas de estudiantes: ")
  print("5. Terminar el Programa: ")
  
  opcion = input( "Opcion a elegir: ")