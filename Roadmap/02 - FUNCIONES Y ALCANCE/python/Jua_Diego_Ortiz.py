
""""
    Funciones Definidas por el usuario
"""

#Simple: sintaxis completa

def saludo():
    print("hOLA")
saludo()

#Con retorno:

def saludo():
    return "Hola"
print(saludo())

#Con un argumento: pasar parametros a la funcion

def arg(name,saludo):
    return (f"{saludo}, {name}")
print(arg("Hola","Juan"))

#Con argumentos predeterminado:

def saludo(name='python'):
    return (f"Hola, {name}")
print(saludo("Juan"))

#argumentos con return

def saludo(greet,name):
    return f"{greet},{name}"
print(saludo("Hola","Sapa"))

#Funciones con un numero variable de argumentos

def variable_greet(*names):
    for name in names:
        print(f"Hola, {name}")
variable_greet("Juan","Pedro","Maria")

#Funciones con numero de variable con una palabra clave

def variable_greet(**names):
    for key,values in names.items():
        print(f"{values}({key})")
variable_greet(language="python",name="Pedro",alias="Care-picha", edad=26)

#Funciones, dentro de funciones

def saludo():
    def function():
        print("Holaa")
    function() #SE TIENE QUE DEJAR EL CIERRO ANIDAD CON LA FUNCION
saludo()

#fUNCIONES DE LENGUAJES

print(len("Juan Diego"))
print(type(25))
print(type("Pedro"))
print("Juan".upper())

#Variables Locales y Globales

v_global = "python"
print(v_global)

def hello_python():
    return f"hola, {v_global}"
print(hello_python())

#Funcion Extra

def print_number(text1,text2)->int:
    count = 0
    for number in range(1,101):
        if number % 3 == 0 and number % 5 == 0:
            print(text1 + text2)
        elif number % 3 == 0:
            print(text1)
        elif number % 5 == 0:
            print(text2)
        else:
            print(number)
            count += 1
    return count
print(print_number("par","impar"))

