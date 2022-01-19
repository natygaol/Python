# Escribe una función llamada reverseString. Esta función recibe como parámetro
# un string. La función se encarga de retornar el string recibido pero en orden
# de atrás hacia adelante.
# "Hola como estas" => "satse omoc aloH"

def reverseString(texto):
  reverse_word = ""
  for i in range(len(texto) - 1, -1, -1):
    reverse_word += texto[i]
  return reverse_word

print(reverseString("Hola como estas"))
