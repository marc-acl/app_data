from tkinter import*
#Raiz
raiz = Tk()

#Título
raiz.title("First Window")

#Método que limita la redimensión de las ventanas (horizontal, vertical)
#raiz.resizable(0, 0)#0, 0 para no redimensionar

#Icono la imagen debe tener extensión .ico
raiz.iconbitmap(r"C:\Users\dmarc\Downloads\21967fc9\1-e5184d13.ico")

#Darle dimensión, no es necesario si usamos config con width y height
#raiz.geometry("700x400")

#cambiar color de fondo
raiz.config(bg="red")#también coge el códio del color

#Creamos el frame
miFrame = Frame()

#Empaquetamos frame, como el panel en java
miFrame.pack()

miFrame.config(bg = "green")

miFrame.config(width="650", height="350")

#podemos mover el frame dentro de la raíz, bottom abajo
#miFrame.pack(side="bottom")

#moverlo junto con anchor, en este caso sería abajo a la derecha
miFrame.pack(side="bottom", anchor="e")

#Rellenar el eje x
#miFrame.pack(fill="x")

#Rellena rel eje y
#miFrame.pack(fill="y", expand="True")

#Expandir en x y en y
miFrame.pack(fill="both", expand="True")


#Loop que mantiene la ventana
raiz.mainloop()