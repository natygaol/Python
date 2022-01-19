# Escribe una función llamada reverseString. Esta función recibe como parámetro
# un string. La función se encarga de retornar el string recibido pero en orden
# de atrás hacia adelante.
# "Hola como estas" => "satse omoc aloH"

def reverseString(string):
  reverse_word = ""
  for i in range(0, len(string), 1):
    reverse_word.join(string[i])
  
  return reverse_word

word = reverseString("Hola")
print(word)