# from => archivo import => la clase
from Estudiante import Estudiante


naty = Estudiante("Naty", "García", 45551110)
print(naty.nombre)

naty.imprime_informacion()

naty.set_id = (30890)
naty.imprime_informacion()

# así puedo imprimir un atributo de instancia
print("Naty", Estudiante.programa)

Estudiante.programa = "Python"

print("Naty", naty.programa)