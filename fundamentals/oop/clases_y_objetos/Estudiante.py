# nombre del archivo y de la clase debe ser con la primera letra mayuscula
# class Estudiante
# Python debe tener solo 1 constructor, desde 3.9
# la clase es la estructura para el objeto
# el objeto es una instancia de la clase

class Estudiante:
  #constructor
  def __init__(self, nombre, apellido, id):
    # atributos -> son locales a la clase
    self.nombre = nombre
    self.apellido = apellido
    self.id = id
    
  def imprime_informacion(self):
    # para utilizar los atributos del constructor debemos poner self.
    print( self.nombre + " " + self.apellido + " " + str(self.id) )
    
  # metodo para actualizar nombre serían setters
  def set_nombre(self, nuevo_nombre):
    self.nombre = nuevo_nombre
    
  def set_apellido(self, nuevo_apellido):
    self.apellido = nuevo_apellido
    
  def set_id(self, nuevo_id):
    self.edad = nuevo_id
    
  # metodo para obtener/leer atributos, sería getters
  def get_nombre(self):
    return self.nombre
  
  def get_apellido(self):
    return self.apellido
  
  def get_edad(self):
    return self.edad
  
  def imprimeDos( self):
    self.imprime_informacion()
    print("mas datos aca")

