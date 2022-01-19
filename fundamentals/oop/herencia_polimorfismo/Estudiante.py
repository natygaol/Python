from Persona import Persona

# Para heredar debo poner como atributo la clase padre
class Estudiante(Persona):
  
  lista_estudiantes = []
  
  def __init__(self, nombre, apellido, id, curso):
    # estamos llamando al constructor de la clase padre 
    # para poder utilizar los metodos de la clase padre
    super().__init__(nombre, apellido)
    self.id = id
    self.curso = curso
    self.calificaciones = []
    Estudiante.lista_estudiantes.append(self)
    
  def asignaCalificacion(self, nota):
    self.calificaciones.append(nota)
  
  # sobre escritura del metodo padre, debo usar el mismo nombre del metodo
  def informacion(self):
    super().informacion()
    print("Calificaciones:")
    print(self.calificaciones)

  # sin sobre escritura, cambio de nombre de la funcion y coloco self, no super
  # def informacionEstudiante(self):
  #   self().informacion()
  #   print("Calificaciones:")
  #   print(self.calificaciones)

  @classmethod
  def imprime_lista_estudiantes(cls):
    for estudiante in cls.lista_estudiantes:
        estudiante.informacion()