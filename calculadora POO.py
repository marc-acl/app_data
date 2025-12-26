from tkinter import*
import operator
import math

class Calculadora():

    def __init__(self, ventana):

        self.operacion = ""
        self.memory = []
        self.tecla = 0 #0 numero 1 signo 3 igual
        self.ops = {"+": operator.add, "-": operator.sub, "×": operator.mul, "÷": operator.truediv, "=": operator.eq}
        #variables
        self.var_pantalla = StringVar()
        self.var_operaciones = StringVar()
        
        
        #Agregamos raíz
        self.root_root = ventana
        self.root_root.title("Calculadora")
        self.root_root.iconbitmap(r"C:\Users\dmarc\Downloads\calculadora.ico")
        self.root_root.config(bg="#151630")

        #Agregamos screen o display
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
        self.var_pantalla.set("0")
        self.entry_screen = Entry(self.frame_screen, text="0", bg="white", fg="black", font=("Calibri", 45), justify="right",
                                  textvariable=self.var_pantalla, borderwidth=0)
        self.entry_screen.config(state="disabled") #para que no se pueda escribir en la pantalla
        #Empaquetamos la pantalla
        self.entry_screen.pack(fill="both", expand=True, padx=3, pady=0)

        #Frame números
        self.frame_numeros = Frame(self.root_root, width=700, height=1000)
        self.frame_numeros.config(bg="#1D1E41")
        self.frame_numeros.pack(expand=True, fill="both")

        #Configurar las 4 columnas del grid para que se expandan
        for i in range(4):
            self.frame_numeros.grid_columnconfigure(i, weight=1)

        #Configurar las filas (tienes 4 filas de botones)
        for j in range(4):
            self.frame_numeros.grid_rowconfigure(j, weight=1)

        
       
        #Números
        self.buttons_list = ["0", ",", "=", "×", "1", "2", "3", "+", "4", "5", "6", "-", "7", "8", "9", "÷" ]
        for idx, num in enumerate(self.buttons_list):
            row = int(math.fabs(3 - (idx // 4)))
            column = int(math.fabs(0 + (idx % 4)))
            print(row, column)
            if num in ["÷", "-", "+", "×", "=", ","]:
                self.put_sign(num, row, column)
            else:
                self.put_numbers(num, row, column)

        #CE
        self.put_ce()



    def limit_entry(self):
        pass
        
    #lo que se pase por parámetro no tiene que ser siempre igual al texto del entry
    #El botón puede pasar un * por parámetro y el texto tener "x"
    def put_sign(self, opr, row, column):
        btn_sign = Button(self.frame_numeros,text=opr, command=lambda:self.opera(opr))
        btn_sign.grid(row=row, column=column, sticky="nsew")
        btn_sign.config(bg="#FEAD3B", fg="white", font=("Calibri", 20,), relief="flat", borderwidth=2, activebackground="#FFB84D", activeforeground="white")
    
    

    def put_numbers(self, num, row, column):
        self.btn_num = Button(self.frame_numeros, text=num, command=lambda:self.teclado_calculadora(str(num)))
        self.btn_num.grid(row=row, column=column, sticky="nsew")#nsew para que ocupe todo el espacio
        self.btn_num.config(bg="#26273D", fg="white", font=("Calibri", 20,), relief="flat", borderwidth=2, activebackground="#3E405A", activeforeground="white")


    def put_ce(self):
        self.btn_ce = Button(self.frame_numeros, text="CE", command=lambda:self.opera("ce"))
        self.btn_ce.grid(row=4, column=0, columnspan=4, sticky="nsew")
        self.btn_ce.config(bg="#676665", fg="white", font=("Calibri", 20,), relief="flat", borderwidth=2, activebackground="#FFB84D", activeforeground="white")
    

    def teclado_calculadora(self, num):

        if self.var_pantalla.get() == "0" and self.tecla == 0:
            self.var_pantalla.set(num)
        elif self.var_pantalla.get() != "" and self.tecla == 1:
            self.var_pantalla.set(num)
        elif self.tecla == 3:
            self.memory.clear()
            self.var_pantalla.set(num)
        else:
            self.var_pantalla.set(self.var_pantalla.get()+num)

        self.tecla = 0



    def opera(self, opr):
            
            resultado = 0

            #coma
            if opr == ",":
                self.coma_once()
                return


            if self.var_pantalla.get() != "" and self.tecla == 0 and self.var_pantalla.get() != "0":
                self.memory.append(self.var_pantalla.get())

            print(self.memory)

            if len(self.memory) == 2:
                resultado = self.ops[self.operacion](float(self.memory[0]), float(self.memory[1]))
                if resultado.is_integer():
                    self.var_pantalla.set(str(int(resultado)))
                    if opr != "=":
                        self.var_operaciones.set(self.var_pantalla.get()+ " " +opr)
                    else:
                        self.var_operaciones.set(self.memory[0] + " " + self.operacion + " " + self.memory[1] + " " + opr)
                else:
                    self.var_pantalla.set(str(resultado))
                    if opr != "=":
                        self.var_operaciones.set(self.var_pantalla.get()+ " " +opr)
                    else:
                        self.var_operaciones.set(self.memory[0] + " " + self.operacion + " " + self.memory[1] + " " + opr)
                    
                self.memory.clear()
                self.memory.append(self.var_pantalla.get())
                print(self.memory)
            
            else:
                self.var_operaciones.set(self.var_pantalla.get()+" "+opr)

            if opr == "ce":
                self.var_pantalla.set("0")
                self.var_operaciones.set("0")
                self.memory.clear()
                self.operacion = ""

            
            if opr != "=":
                self.operacion = opr
                self.tecla = 1 
            else:
                self.operacion = ""
                self.tecla = 3

    

    def coma_once(self):
    
        for i in self.var_pantalla.get():
            if i == ".":
                return
        self.var_pantalla.set(self.var_pantalla.get()+".")


    def scientific_notation(self, num):
        pass

    

root_poo = Tk()
root_poo.config()
calculadora_poo = Calculadora(root_poo)



root_poo.mainloop()