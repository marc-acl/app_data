from tkinter import*
import operator

#***********************************Raíz o panel**********************************
root_root = Tk()
root_root.title("Calculadora")
root_root.config(bg="#151630")

#********************Creamos la viariable que guarda las operaciones*****************************
operacion = "0"+"0"
memory = []
tecla = 0 #0 numero 1 signo



#************************************Frame de la pantalla***************************
frame_screen = Frame(root_root, bg="#151630")
frame_screen.config(height=100, width=400)
frame_screen.pack_propagate(False) #evita que el frame se ajuste al contenido
#Empaquetamos el frame
frame_screen.pack(fill="x")

#*************************************Variable asociada a la pantalla*******************
var_pantalla = StringVar()
var_pantalla.set("0")

#**************************************Ponemos la pantalla***************************
entry_screen = Entry(frame_screen, text="0", bg="white", fg="black", font=("Calibri", 40), justify="right", textvariable=var_pantalla)
entry_screen.config(state="disabled") #para que no se pueda escribir en la pantalla
#Empaquetamos la pantalla
entry_screen.pack(fill="both", expand=True, padx=3, pady=3)


#**************************************Función eventos teclas*******************************************
def teclado_calculadora(num):

    global tecla
    global memory

    if var_pantalla.get() == "0":
        var_pantalla.set(num)
    elif var_pantalla.get() != "" and tecla == 1:
        var_pantalla.set("")
        var_pantalla.set(var_pantalla.get()+num)
    else:
        var_pantalla.set(var_pantalla.get()+num)

    tecla = 0


#**************************************OPERACIONES***********************************************************
#Para usar la variable operaciones de la clase, la que está arriba, es necesario poner antes global
#Si no se pone python asume que se crea otra dentro de función con el mismo nombre

#La memoria sólo se usa cuando se presionan signos

ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv, "=": operator.eq}

def opera(opr):
    
    global ops
    global operacion
    global tecla
    global memory

    if var_pantalla.get() != "" and tecla == 0 and var_pantalla.get() != "0":
        memory.append(var_pantalla.get())

    print(memory)

    if len(memory) == 2:
        var_pantalla.set("")
        var_pantalla.set(str(ops[operacion](float(memory[0]), float(memory[1]))))
        memory.clear()
        memory.append(var_pantalla.get())
        print(memory)

    if opr != "=":
        operacion = opr
    else:
        operacion = ""
    tecla = 1
   

#*************************************Creamos el frame de los números*******************************
frame_numeros = Frame(root_root, width=400)
frame_numeros.config(bg="#1D1E41", width=400)

#*************************Configurar las 4 columnas del grid para que se expandan*********************
for i in range(4):
    frame_numeros.grid_columnconfigure(i, weight=1)

#Configurar las filas (tienes 4 filas de botones)
for j in range(4):
    frame_numeros.grid_rowconfigure(j, weight=1)


#***********************************Empaquetamos el frame****************************************
frame_numeros.pack(expand=True, fill="both")

#************************************Primera fila números******************************************
#se introduce el lambda porque funciona como un evento
buttons_list = ["1","2","3","4","5","6","7","8","9","0"]
r = list(reversed(buttons_list))
 # Excluye el "0" para que no se coloque en la cuadrícula
 


def put_numbers(num, row, column):
        btn_num = Button(frame_numeros, text=num, command=lambda:teclado_calculadora(str(num)))
        btn_num.grid(row=row, column=column, sticky="nsew")#nsew para que ocupe todo el espacio
        btn_num.config(bg="#26273D", fg="white", font=("Calibri", 20,), relief="flat", borderwidth=2, activebackground="#3E405A", activeforeground="white")

#patrón para colocar los botones en una cuadrícula
#7 row = 0, column = 0
#8 row = 0, column = 1
#9 row = 0, column = 2      
#4 row = 1, column = 0
#5 row = 1, column = 1
#6 row = 1, column = 2
#1 row = 2, column = 0
#2 row = 2, column = 1
#3 row = 2, column = 2
#0 row = 3, column = 0

for idx, num in enumerate(buttons_list):
    row = 2 - (idx // 3)
    column = 0 + (idx % 3)
    put_numbers(num, row, column)

# for idx, num in enumerate(buttons_list):
#     row = idx // 3
#     column = idx % 3
#     put_numbers(num, row, column)

# for i in range(7, 10):
#     j = i - 7
#     buttons_list[i] = Button(frame_numeros, text=str(i), command=lambda:teclado_calculadora(buttons_list[i]))
#     buttons_list[i].grid(row=0, column=j, sticky="nsew")#nsew para que ocupe todo el espacio
#     buttons_list[i].config(bg="#26273D", fg="white", font=("Calibri", 20,), relief="flat", borderwidth=2, activebackground="#3E405A", activeforeground="white")



# for i in range(4, 7):
#     j = i - 4
#     btn_i = Button(frame_numeros, text=str(i), command=lambda:teclado_calculadora(str(i)))
#     btn_i.grid(row=1, column=j, sticky="nsew")#nsew para que ocupe todo el espacio
#     btn_i.config(bg="#26273D", fg="white", font=("Calibri", 20,), relief="flat", borderwidth=2, activebackground="#3E405A", activeforeground="white")



# for i in range(1, 4):
#     j = i - 1
#     btn_i = Button(frame_numeros, text=str(i), command=lambda:teclado_calculadora(str(i)))
#     btn_i.grid(row=2, column=j, sticky="nsew")#nsew para que ocupe todo el espacio
#     btn_i.config(bg="#26273D", fg="white", font=("Calibri", 20,), relief="flat", borderwidth=2, activebackground="#3E405A", activeforeground="white")


#*****************************************función coma***************************************

def coma_once():
    
    for i in var_pantalla.get():
        if i == ",":
            return
    var_pantalla.set(var_pantalla.get()+",")

#***********************************signos*****************************************************
def put_sign(opr, row, column, command):
    btn_sign = Button(frame_numeros, text=opr, command=command)
    btn_sign.grid(row=row, column=column, sticky="nsew")
    btn_sign.config(bg="#FEAD3B", fg="white", font=("Calibri", 20,), relief="flat", borderwidth=2, activebackground="#FFB84D", activeforeground="white")
    return btn_sign

put_sign("÷", 0, 3, command=lambda:opera("/"))
put_sign("-", 1, 3, command=lambda:opera("-"))
put_sign("+", 2, 3, command=lambda:opera("+"))
put_sign("x", 3, 3, command=lambda:opera("*"))
put_sign("=", 3, 2, command=lambda:opera("="))
put_sign(",", 3, 1, command=lambda:coma_once())



#****************************************cuarta fila de números**************************************
btn_cero = Button(frame_numeros, text="0", command=lambda:teclado_calculadora("0"))
btn_cero.grid(row=3, column=0, sticky="nsew")
btn_cero.config(bg="#26273D", fg="white", font=("Calibri", 20,), relief="flat", borderwidth=2, activebackground="#3E405A", activeforeground="white")



root_root.mainloop()