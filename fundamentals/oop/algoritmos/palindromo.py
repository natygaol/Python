# Escribe una función llamada palindromo. Esta función recibe como parámetro
# un string. La función se encarga de retornar True si el string es un palindromo
# False de lo contrario.
# Palíndromos: radar - oso - arañera - orejero - rayar - salas - seres - sometemos
# BONUS: "Anita lava la tina" - "No traces en ese carton" - "Son robos o sobornos"

def reverse_string(string):
  reserve_string = string[::-1]
  if (string == reverse_string):
    print(string, "Es palindrome")
  else:
    print(string, "No es palindrome")

word = reverse_string("oso")
print(word)