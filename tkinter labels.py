from tkinter import*

#Raiz
raiz = Tk()

#Título
raiz.title("Second Window")

#Constructor
miFrame = Frame(raiz, width=500, height=450)

#Empaquetar
miFrame.pack()

#creamos un label. El constructor admite parámetros indefinidos
label_uno = Label(miFrame, text="Hola, Mundo!")
#Se empaqueta el label
#label_uno.pack()#funciona pero hace que la raíz se adapte al tamaño del txt

#Entonces empaquetamos con place
label_uno.place(x=120, y=125)

#Ponemos color
label_uno.config(fg="red")

#modificamos fuente
label_uno.config(font=("Calibri", 36))

#Podemos prescindir de los dos pasos anteriores con esta línea
Label(miFrame, text="Hola, Mundo label 2!", fg="blue", font=("Courier", 20)).place(x=120, y=200)


#ponemmos una imagen
miImagen = PhotoImage(file=r"C:\Users\dmarc\Downloads\email_3894024.png")
miImagen = miImagen.subsample(5,5) #reduce la imagen a la mitad
Label(miFrame, image = miImagen).place(x=200, y=400, anchor=CENTER)
#resize image



#Creamos el loop
raiz.mainloop()


