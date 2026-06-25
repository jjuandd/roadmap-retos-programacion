"""
    Operadores
"""
print("------------------------------------------------------")
print("Operadores aritmeticos: ")
print(f"Suma: 10+3 es {10+3}")
print(f"Resta: 25-5 es {25-5}")
print(f"mul: 4*5 es {4*5}")
print(f"divi: 40/2 es {40/2}")
print(f"modulo: 15%5 es {15%5}")
print(f"expo: 2**4 es {2**4}")

print("------------------------------------------------------")

print("Operadores de comparacion: ")

print(f"Igualdad: 10==3 es {10==3}")
print(f"Desigualdad: 10!=3 es {10!=3}")
print(f"Desigualdad: 10>3 es {10>3}")
print(f"Desigualdad: 10<3 es {10<3}")
print(f"Desigualdad: 10>=3 es {10>=3}")
print(f"Desigualdad: 10<=3 es {10<=3}")
print("------------------------------------------------------")

print("Operadores Logicos: ")

print(f"AND &&: 10+3 == 13 and 5-1 == 4 es {10+3 == 13 and 5-1 == 4}")
print (f"O or: 5 *4 == 20 or 20 < 10 es {5*4 == 20 or 20 < 10}")
print (f"Not !: not 10+3 == 14 es {not 10 - 13 == 14}")
print("------------------------------------------------------")

print("Operadores de asignacion: ")

my_number = 11 #asignacion
print(my_number)

my_number += 5 #Suma y asignacion
print(my_number)

my_number -= 5 #Resta y asignacion
print(my_number)

my_number *= 5 #Multiplicacion y asignacion
print(my_number)

my_number /= 5 #Division y asignacion
print(my_number)

my_number //= 5 #Divicion entera y asignacion
print(my_number)

my_number %= 5 #Modulo y asignacion
print(my_number)

my_number **= 5 #Exponente y asignacion
print(my_number)
print("------------------------------------------------------")

print("Operadores de identidad")
#Valor de la posicion de memoria

my_new_number = my_number
print(f"my_number is my_new_number es {my_number is my_new_number}")
print("------------------------------------------------------")

Variable_uno = 5
Variable_dos = "Hola"
print(Variable_uno is not Variable_dos)
print("------------------------------------------------------")

print("Operadores de pertenencia: ")
name = "Juan"
print('u' in name)
name1= "Yoha"
print("M" in name1)
print("----------------------------------------------------")
print(f"'u' in 'Juan' = {'u' in 'Juan'}")
print(f"'u' not in 'Juan' = {'u' not in 'Juan'}")
print("------------------------------------------------------")

print("Operadores bit: ")

a= 10
b= 3
print(a & b, a ^ 3, a | b)

print("------------------------------------------------------")
print(f"And: 10 & 3 = {10 & 3}")
print(f"OR: 10 & 3 = {10 | 3}") # ALT 124 
print(f"XOR: 10 & 3 = {10 ^ 3}" ) # alt 94
print(f"NOT: ~10 = {~10}")
print(f"Dezplazamiento a la derecha: 10 >> 2 es = {10 >> 2}")
print(f"Dezplazamiento a la derecha: 10 << 2 es = {10 << 2}")

print("------------------------------------------------------")

print("Condicionales: ")

my_string = "Juan"

if my_string == "Juan":
    print("Exacto")
else:
    print("Para nada")

password = 12345678
intento = int(input("Coloca tu contraseña: "))
if intento == password:
    print("Bienvenido")
else:
    print("No eres adminitdo")
    
print("------------------------------------------------------")

print("iterativo: ")

for i in range(11):
    print(i)

i = 0
while i <= 10:
    print(1)
    i+=1

print("------------------------------------------------------")

print("Manejo de Excepciones: ")

try:
    print(10/0)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")

print("------------------------------------------------------")

print("EXTRA: ")


for number in range(10,56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)












