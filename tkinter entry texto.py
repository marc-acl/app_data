from tkinter import*

#Creamos la raíz
raiz = Tk()

#Creamos el frame
miFrame = Frame(raiz, width=300, height=450)

#empquetamos el frame
miFrame.pack(side="top")

#creamos el cuadro de text, miFrame es su clase padre
#txtBox = Entry(miFrame)
#txtBox.place(x=180, y=110)


#Creamos label, si pongo las mismas coordenadas pone una a la izquierda de otra
#label_uno = Label(miFrame, text="Usuario ")
#label_uno.place(x=120, y=110)

#Implementamos el grid que funciona como una tabla. El grid invalida los parámetros iniciales del Frame
texto_Boxuno = StringVar()
txtBox_uno = Entry(miFrame, textvariable=texto_Boxuno)
txtBox_uno.grid(row=0, column=1, padx=15, pady=15)


label_dos = Label(miFrame, text="Usuario login ")
label_dos.grid(row=0, column=0)

#Creamos una variable de texto que almacena lo que se le introduzca



txtBox_dos = Entry(miFrame)
txtBox_dos.grid(row=1, column=1, padx=15, pady=15)

label_tres = Label(miFrame, text="Mail ", fg="green")
label_tres.grid(row=1, column=0)

#label_cuatro = Label(miFrame, text="Hola ")
#label_cuatro.grid(row=1, column=2)


txtBox_tres = Entry(miFrame)
txtBox_tres.grid(row=2, column=1, padx=15, pady=15)
txtBox_tres.config(fg="red")
#Ocultar carácteres escritos
txtBox_tres.config(show="•")

label_cinco = Label(miFrame, text="Log ")
#Alineación del texto con sticky
label_cinco.grid(row=2, column=0, sticky="w")

#Creamos cuadro de texto
label_seis = Label(miFrame, text="Comentarios " )
label_seis.grid(row=3, column=0)


#Cuadro de texto con 
cuadro_txt = Text(miFrame, width=25, height=20)
cuadro_txt.grid(row=3, column=1, padx=15, pady=15)
#cuadro_txt.config(width=40, height=25)

#Insertamos barra de desplazamiento
scroll = Scrollbar(miFrame, command=cuadro_txt.yview)

#con nsew se ve mejor
scroll.grid(row=3, column=2, sticky="nsew")
cuadro_txt.config(yscrollcommand=scroll.set)

#funcion botón enviar
from tkinter import messagebox as MessageBox
def funcion_enviar():
    #Ventana emergente  
    #MessageBox.showinfo("hola", "Estamos en python")
    #usamos la variable creada para introducir texto en el box text 1
    texto_Boxuno.set("Hola, Diana")

#Creamos un botón que se puede poner en la raíz o en el frame, funcina igual
#1. Agregamos en el frame
button_enviar = Button(miFrame, text="Enviar", fg="red", bg="blue", command=funcion_enviar)
#como miFrame ya está manejado con un grid, sólo deja posicionar cosas en él a partir del grid
#button_enviar.config(width=10, height=2, image="", compound="center")
button_enviar.grid(row=4, column=2)

def funcion_btnraiz():

    MessageBox.showinfo("Get Message", txtBox_dos.get() + " " + txtBox_tres.get())

#2. También podemos ponerlo en la raíz y que se ajuste a esta y no al grid de miFRame
button_raiz = Button(raiz, text="En la raiz", fg="blue", bg="green", command=funcion_btnraiz)
#Empaquetamos el botón
button_raiz.pack()


#3. Podemos ponerlo en la raíz con place
button_place = Button(raiz, text="raiz place", fg="blue", bg="green")
button_place.place(x=120, y=550)

#4. Podemos agregar otro frame a la raiz
frame_2 = Frame(raiz, width=500, height=700)
frame_2.pack(side="bottom")


def insertar_comentario():
    cuadro_txt.insert(INSERT, "HOLA, DIANAAAAAAAAAAAAAAA")

#Agregamos un botón al frame 2
button_2 = Button(frame_2, text="en el frame 2", fg="blue", bg="yellow", command=insertar_comentario)
button_2.place(x=120, y=0)






raiz.mainloop()
