#ejercicio 1
#for x in range(0,151):
  #print(x)

#ejercicio 2
#for x in range(5, 1001, 5):
  #print(x)

""" ejercicio 3: imprime números enteros del 1 al 100. 
Si es divisible por 5, imprime "Coding” en su lugar. Si es divisible por 10, imprime "Coding Dojo". """

for i in range(0,101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)


"""ejercicio 4: agrega los enteros impares del 0 al 500,000, e imprime la suma final."""
counter = 0

for i in range(1,500001,2):
  print(i)
  counter += i
  
"""imprime números positivos comenzando desde el 2018, en cuenta regresiva de 4 en 4."""

for i in range(2018, 0, -4):
  print(i)


"""establece tres variables: 
lowNum, 
highNum, 
mult. 
Comenzando en lowNum y pasando por highNum, imprime solo los enteros que sean múltiplos de mult. 
Por ejemplo, si lowNum=2, highNum=9 y mult=3. El bucle debe imprimir 3, 6, 9 (en líneas sucesivas). """

lowNum = 2
highNum = 9
mult = 3

for i in range(lowNum, highNum, 3):
  if i % mult == 0:
    print(i)