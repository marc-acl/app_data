from CTkMessagebox import CTkMessagebox
import customtkinter as ctk
from tkinter import*

tup = [(-84.64,), (34066.667,), (-0.075,)]

list_app = []
column_var = [tup[i][0]for i in range(len(tup))]
print(column_var)


def verify(**kwargs):
    verify_result = False
    for key, value in kwargs.items():
        if key.__contains__("num"):
            try:
                isinstance(float(value), float)
                verify_result= True
            except:
                CTkMessagebox(title='Database', message="{key}: Please enter a numeric value.",
                                                          icon="warning", option_1="Ok")
                verify_result = False
                
        else:
            try:
                isinstance(float(value), float)
                CTkMessagebox(title='Database Warning', message="{key}: Please enter some text.",
                                          icon="warning", option_1="Ok")
                verify_result = False
                
            except:
                verify_result = True
    
    return verify_result



prueba = verify(num_id="125", num_value="44f", str_name = "hola", str_name2 = "123")
prueba2 = verify(num_id="125", num_value="44", str_name = "hola", str_name2 = "123H")

print('----------------------------------')
if prueba:
    print(":)")
else:
    print(":(")

if prueba2:
    print(":)")
else:
    print(":(")



def analizar(valor):
    match valor:
        case {"tipo": "usuario", "id": int(uid)}:
            return f"Usuario con ID {uid}"
        case [x, y] if x < y:
            return "Lista ordenada ascendente"
        case str(s):
            return f"Cadena: {s}"
        case _:
            return "Desconocido"


print(analizar({"tipo": "usuario", "id": 123}))

option = "ID"
option_menu = ("num_" if option == "ID" else "str_")+option
print(option_menu)
str(option_menu)

def valuer(**kwargs):
    for key, value in kwargs.items():
        print(key)

valuer(option_menu=5)


def print_a(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

print_a(last=25)


def print_b(laster = None, **kwargs):
    print(laster)
    print(kwargs)

print_b(hola=5, laster=55)


diccionario = {'ada':5}
for key, value in diccionario.items():
    if value == '':
        print('lleno')
    else:
        print('vacio')

list = ['ana', 2, 5, 'Dad']
lista2 = []
variable = []
var = ''

for i in range(len(list)):
    var = StringVar(value="off")
    variable.append(var)
    lista2.append(list[i])
print(variable)

print('dict')
dict = {'hola':'anda'}
print(dict["hola"])

print('probe list')
list_trio = [('hola', 'ola'), 5, 2]

print(len(list_trio))

