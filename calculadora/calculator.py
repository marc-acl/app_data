from tkinter import*
import operator
import buttons


class Calculator():

    def __init__(self, ventana):

        self.operacion = ""
        self.memory = []
        self.tecla = 0 #0 numero 1 signo 3 igual
        self.ops = {"+": operator.add, "-": operator.sub, "×": operator.mul, "÷": operator.truediv, "=": operator.eq}
        #variables
        self.var_screen = StringVar()
        self.var_operaciones = StringVar()


        #Agregamos raíz
        self.root_root = ventana
        self.root_root.title("Calculadora")
        self.root_root.iconbitmap(r"C:\Users\dmarc\Downloads\calculadora.ico")
        self.root_root.config(bg="#151630")

        #Agregamos screen o display
        #Si usas pack(), el tamaño de cada frame dependerá de sus widgets internos y cómo usas fill, expand.
        self.frame_screen = Frame(self.root_root, bg="#151630")
        self.frame_screen.config(height=100, width=400)
        self.frame_screen.pack_propagate(False)
        self.frame_screen.pack(fill="x")

        #Screen operaciones
        self.var_operaciones.set("0")
        self.entry_opscreen = Entry(self.frame_screen, text="0", bg="white", fg="black", font=("Calibri", 12), justify="right",
                                     textvariable=self.var_operaciones, borderwidth=0)
        self.entry_opscreen.config(state="disabled") #para que no se pueda escribir en la pantalla
        #Empaquetamos la pantalla
        self.entry_opscreen.pack(fill="both", expand=True, padx=3, ipady=0)

        #Pantalla
        self.var_screen.set("0")
        self.entry_screen = Entry(self.frame_screen, text="0", bg="white", fg="black", font=("Calibri", 45), justify="right",
                                  textvariable=self.var_screen, borderwidth=0)
        self.entry_screen.config(state="disabled") #para que no se pueda escribir en la pantalla
        #Empaquetamos la pantalla
        self.entry_screen.pack(fill="both", expand=True, padx=3, pady=0)

        #Frame números, el tamaño del grid depende de las filas y columnas que tenga
        self.frame_numeros = Frame(self.root_root)
        self.frame_numeros.config(bg="#1D1E41")
        self.frame_numeros.pack(expand=True, fill="both")

        #Configurar las 4 columnas del grid para que se expandan
        for i in range(4):
            self.frame_numeros.grid_columnconfigure(i, weight=1)

        #Configurar las filas (tienes 4 filas de botones)
        for j in range(4):
            self.frame_numeros.grid_rowconfigure(j, weight=1)

        #Números, filas = 4, columnas = 4
        self.buttons_list = ["0", ",", "=", "×", #fila 1
                             "1", "2", "3", "+", #fila 2
                             "4", "5", "6", "-", #fila 3
                             "7", "8", "9", "÷" ] #fila 4
        buttons.put_keys(self, self.buttons_list, 4, 4, self.root_root)
        buttons.put_ce(self, self.root_root)


root_poo = Tk()
root_poo.config()
calculadora_poo = Calculator(root_poo)



root_poo.mainloop()
        