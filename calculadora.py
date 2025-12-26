from tkinter import*
import operator

#*********************************************Raíz o panel**************************************
root_root = Tk()
root_root.title("Calculadora")
root_root.config(bg="#151630")

#********************Creamos la viariable que guarda las operaciones*****************************
operacion = ""
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
entry_screen = Entry(frame_screen, text="0", bg="white", fg="black", font=("Calibri", 45), justify="right", textvariable=var_pantalla)
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

ops = {"+": operator.add, "-": operator.sub, "x": operator.mul, "/": operator.truediv, "=": operator.eq}

def opera(opr):
    
    global ops
    global operacion
    global tecla
    global memory
    resultado = 0

    if var_pantalla.get() != "" and tecla == 0 and var_pantalla.get() != "0":
        memory.append(var_pantalla.get())

    print(memory)

    if len(memory) == 2:
        resultado = ops[operacion](float(memory[0]), float(memory[1]))
        if resultado.is_integer():
            var_pantalla.set(str(int(resultado)))
        else:
            var_pantalla.set(str(resultado))
        #var_pantalla.set(str(ops[operacion](float(memory[0]), float(memory[1]))))
        memory.clear()
        memory.append(var_pantalla.get())
        print(memory)

    if opr == "ce":
        var_pantalla.set("0")
        memory.clear()
        operacion = ""

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
#se introduce el lambda porque funciona como un evento y hay que pasar parametros
#si no usaramos el lambda, no se pasaría el parámetro y se ejecutaría la función al crear el botón
#el lambda crea una función anónima que llama a la función con el parámetro
#command sin lambda funciona como evento pero no usa parámetros

btn_siete = Button(frame_numeros, text="7", command=lambda:teclado_calculadora("7"))
btn_siete.grid(row=0, column=0, sticky="nsew")#nsew para que ocupe todo el espacio
btn_siete.config(bg="#26273D", fg="white", font=("Calibri", 20,), relief="flat", borderwidth=2, activebackground="#3E405A", activeforeground="white")

btn_ocho = Button(frame_numeros, text="8", command=lambda:teclado_calculadora("8"))
btn_ocho.grid(row=0, column=1, sticky="nsew")
btn_ocho.config(bg="#26273D", fg="white", font=("Calibri", 20,), relief="flat", borderwidth=2, activebackground="#3E405A", activeforeground="white")

btn_nueve = Button(frame_numeros, text="9", command=lambda:teclado_calculadora("9"))
btn_nueve.grid(row=0, column=2, sticky="nsew") 
btn_nueve.config(bg="#26273D", fg="white", font=("Calibri", 20,), relief="flat", borderwidth=2, activebackground="#3E405A", activeforeground="white")

btn_div = Button(frame_numeros, text="÷", command=lambda:opera("/"))
btn_div.grid(row=0, column=3, sticky="nsew")
btn_div.config(bg="#FEAD3B", fg="white", font=("Calibri", 20,), relief="flat", borderwidth=2, activebackground="#FFB84D", activeforeground="white")

#***************************************Segunda fila números*****************************************
btn_cuatro = Button(frame_numeros, text="4", command=lambda:teclado_calculadora("4"))
btn_cuatro.grid(row=1, column=0, sticky="nsew")
btn_cuatro.config(bg="#26273D", fg="white", font=("Calibri", 20,), relief="flat", borderwidth=2, activebackground="#3E405A", activeforeground="white")

btn_cinco = Button(frame_numeros, text="5", command=lambda:teclado_calculadora("5"))
btn_cinco.grid(row=1, column=1, sticky="nsew")
btn_cinco.config(bg="#26273D", fg="white", font=("Calibri", 20,), relief="flat", borderwidth=2, activebackground="#3E405A", activeforeground="white")

btn_seis = Button(frame_numeros, text="6", command=lambda:teclado_calculadora("6"))
btn_seis.grid(row=1, column=2, sticky="nsew") 
btn_seis.config(bg="#26273D", fg="white", font=("Calibri", 20,), relief="flat", borderwidth=2, activebackground="#3E405A", activeforeground="white")

btn_menos = Button(frame_numeros, text="-", command=lambda:opera("-"))
btn_menos.grid(row=1, column=3, sticky="nsew")
btn_menos.config(bg="#FEAD3B", fg="white", font=("Calibri", 28,), relief="flat", borderwidth=2, activebackground="#FFB84D", activeforeground="white")

#*****************************************Tercera fila de números*****************************************
btn_uno = Button(frame_numeros, text="1", command=lambda:teclado_calculadora("1"))
btn_uno.grid(row=2, column=0, sticky="nsew")
btn_uno.config(bg="#26273D", fg="white", font=("Calibri", 20,), relief="flat", borderwidth=2, activebackground="#3E405A", activeforeground="white")

btn_dos = Button(frame_numeros, text="2", command=lambda:teclado_calculadora("2"))
btn_dos.grid(row=2, column=1, sticky="nsew")
btn_dos.config(bg="#26273D", fg="white", font=("Calibri", 20,), relief="flat", borderwidth=2, activebackground="#3E405A", activeforeground="white")

btn_tres = Button(frame_numeros, text="3", command=lambda:teclado_calculadora("3"))
btn_tres.grid(row=2, column=2, sticky="nsew") 
btn_tres.config(bg="#26273D", fg="white", font=("Calibri", 20,), relief="flat", borderwidth=2, activebackground="#3E405A", activeforeground="white")

btn_mas = Button(frame_numeros, text="+", command=lambda:opera("+"))
btn_mas.grid(row=2, column=3, sticky="nsew")
btn_mas.config(bg="#FEAD3B", fg="white", font=("Calibri", 20,), relief="flat", borderwidth=2, activebackground="#FFB84D", activeforeground="white")

#****************************************cuarta fila de números**************************************
btn_cero = Button(frame_numeros, text="0", command=lambda:teclado_calculadora("0"))
btn_cero.grid(row=3, column=0, sticky="nsew")
btn_cero.config(bg="#26273D", fg="white", font=("Calibri", 20,), relief="flat", borderwidth=2, activebackground="#3E405A", activeforeground="white")


def coma_once():
    
    for i in var_pantalla.get():
        if i == ".":
            return
    var_pantalla.set(var_pantalla.get()+".")


btn_coma = Button(frame_numeros, text=",", command=coma_once)
btn_coma.grid(row=3, column=1, sticky="nsew") 
btn_coma.config(bg="#FEAD3B", fg="white", font=("Calibri", 20,), relief="flat", borderwidth=2, activebackground="#FFB84D", activeforeground="white")

btn_igual = Button(frame_numeros, text="=", command=lambda:opera("="))
btn_igual.grid(row=3, column=2, sticky="nsew") 
btn_igual.config(bg="#FEAD3B", fg="white", font=("Calibri", 20,), relief="flat", borderwidth=2, activebackground="#FFB84D", activeforeground="white")

btn_multip = Button(frame_numeros, text="x", command=lambda:opera("x"))
btn_multip.grid(row=3, column=3, sticky="nsew")
btn_multip.config(bg="#FEAD3B", fg="white", font=("Calibri", 20,), relief="flat", borderwidth=2, activebackground="#FFB84D", activeforeground="white")

#*************************************barra CE*********************************************
btn_ce = Button(frame_numeros, text="CE", command=lambda:opera("ce"))
btn_ce.grid(row=4, column=0, columnspan=4, sticky="nsew")
btn_ce.config(bg="#676665", fg="white", font=("Calibri", 20,), relief="flat", borderwidth=2, activebackground="#FFB84D", activeforeground="white")

root_root.mainloop()

