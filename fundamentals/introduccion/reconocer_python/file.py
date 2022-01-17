num1 = 42 #variable declaration , inicializo integer
num2 = 2.3 #variable declaration, inicializo float
boolean = True #variable declaration, inicializo boolean
string = 'Hello World' #variable declaration, inicializo string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, inicializo lista
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration, inicializo diccionario
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration, inicializo tupla
print(type(fruit)) #type check
print(pizza_toppings[1]) #Data types / Composite / List / access value
pizza_toppings.append('Mushrooms') #Data types / Composite / List / add value
print(person['name']) #Data types / Composite / Diccionario / access value
person['name'] = 'George' #Data types / Composite / Diccionario / change value
person['eye_color'] = 'blue' #Data types / Composite / Diccionario / add value
print(fruit[2]) # Data types / Composite / Tuples / access value

if num1 > 45:             # condicional / if
    print("It's greater")
else:                     # condicional / else
    print("It's lower")

if len(string) < 5:             # condicional / if
    print("It's a short word!")
elif len(string) > 15:          # condicional / else if
    print("It's a long word!")
else:                           # condicional / else
    print("Just right!")

for x in range(5): #for loop del 0 al 4
    print(x)
for x in range(2,5): # for loop del 2 al 4
    print(x)
for x in range(2,10,3): # for loop del 2 al 9 pero de 3 en 3 se corre
    print(x)

x = 0 #variable declaration
while(x < 5): #while loop start
    print(x)
    x += 1  #while loop / increment

pizza_toppings.pop() #Data types / Composite / List / delete value
pizza_toppings.pop(1) #Data types / Composite / List / delete value del indice 1

print(person) # imprimir valor de variable person
person.pop('eye_color') #Data types / Composite / Diccionario / delete key -> eye_color
print(person) # imprimir el diccionario luego de modificaciones

for topping in pizza_toppings: #for loop
    if topping == 'Pepperoni': # condicion
        continue #continue
    print('After 1st if statement') 
    if topping == 'Olives': #condicion
        break               #break

def print_hello_ten_times(): #funcion
    for num in range(10): #argumento
        print('Hello') 

print_hello_ten_times()

def print_hello_x_times(x): #funcion / parametro
    for num in range(x): #argumento
        print('Hello') 

print_hello_x_times(4) # imprime 4 veces

def print_hello_x_or_ten_times(x = 10): #funcion / parametro
    for num in range(x): #argumento
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3) -> NameError: name 'num3' is not defined
# num3 = 72
# fruit[0] = 'cranberry' -> TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) 
# print(pizza_toppings[7]) -> KeyError: 'favorite_team'
#   print(boolean) -> IndentationError: unexpected indent
# fruit.append('raspberry') -> AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) -> AttributeError: 'tuple' object has no attribute 'pop'