def teclado_calculadora(self, num):

    if self.var_screen.get() == "0" and self.tecla == 0:
        self.var_screen.set(num)
    elif self.var_screen.get() != "" and self.tecla == 1:
        self.var_screen.set(num)
    elif self.tecla == 3:
        self.memory.clear()
        self.var_screen.set(num)
    elif self.var_screen.get() == "0" and self.tecla == 4:
        self.var_screen.set(self.var_screen.get()+".")
    else:
        self.var_screen.set(self.var_screen.get()+num)

    self.tecla = 0



def opera(self, opr):
        
        result = 0
        result_sn = 0

        #coma
        if opr == ",":
            self.tecla = 4
            coma_once(self)
            return


        if self.var_screen.get() != "" and self.tecla == 0 and self.var_screen.get() != "0":
            self.memory.append(self.var_screen.get())

        #print(self.memory)

        if len(self.memory) == 2:
            result = self.ops[self.operacion](float(self.memory[0]), float(self.memory[1]))
            result_sn = scientific_notation(self, result)
            if result.is_integer():
                self.var_screen.set(result_sn)
                if opr != "=":
                    self.var_operaciones.set(self.var_screen.get()+ " " +opr)
                else:
                    self.var_operaciones.set(self.memory[0] + " " + self.operacion + " " + self.memory[1] + " " + opr)
            else:
                self.var_screen.set(result_sn)
                if opr != "=":
                    self.var_operaciones.set(self.var_screen.get()+ " " +opr)
                else:
                    self.var_operaciones.set(self.memory[0] + " " + self.operacion + " " + self.memory[1] + " " + opr)
                
            self.memory.clear()
            self.memory.append(self.var_screen.get())
            #print(self.memory)
        
        else:
            self.var_operaciones.set(self.var_screen.get()+" "+opr)

        if opr == "ce":
            self.var_screen.set("0")
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

    for i in self.var_screen.get():
        if i == "." :
            return
    self.var_screen.set(self.var_screen.get()+".")


def scientific_notation(self, result):
    try:
        # Intentamos mostrarlo como decimal (con redondeo)
        for dec in range(9, -1, -1):  # desde 9 decimales hasta 0
            txt = f"{result:.{dec}f}"
            if len(txt) <= 10:
                return txt

        # Si no cabe, usamos notación científica con redondeo
        for dec in range(6, 0, -1):  # hasta encontrar una que quepa
            sci = f"{result:.{dec}e}"
            if len(sci) <= 10:
                return sci

        # Último recurso: recortar simplemente a 10
        return f"{result:.6e}"[:10]

    except Exception as e:
        return "Error"

