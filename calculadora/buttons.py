from tkinter import*
import math
import operations

def put_keys(self, buttons_list, n_columns, n_rows, root):   
    for idx, num in enumerate(buttons_list):
        row = int(math.fabs((n_rows - 1) - (idx // n_columns)))
        column = int(math.fabs(0 + (idx % n_columns)))
        if num in ["÷", "-", "+", "×", "=", ","]:
            put_sign(self, num, row, column, root)
        else:
            put_numbers(self, num, row, column, root)


def put_sign(self, opr, row, column, root):
    btn_sign = Button(self.frame_numeros,text=opr, command=lambda:operations.opera(self, opr))
    btn_sign.grid(row=row, column=column, sticky="nsew")
    btn_sign.config(bg="#FEAD3B", fg="white", font=("Calibri", 20,), relief="flat", borderwidth=2, activebackground="#FFB84D", activeforeground="white")
    # Mapear los signos a las teclas correspondientes
    key_map = { "÷": "/", "×": "*", "-": "-", "+": "+", "=": "<Return>", ",": "." }
    opr_key = key_map.get(opr)
    
    # Asignar evento del teclado, verifica que opr_key no esté vacío
    if opr_key:
        root.bind(opr_key if len(opr_key)>1 else opr_key, lambda event: operations.opera(self, opr))

def put_numbers(self, num, row, column, root):
    self.btn_num = Button(self.frame_numeros, text=num, command=lambda:operations.teclado_calculadora(self, str(num)))
    self.btn_num.grid(row=row, column=column, sticky="nsew")#nsew para que ocupe todo el espacio
    self.btn_num.config(bg="#26273D", fg="white", font=("Calibri", 20,), relief="flat", borderwidth=2, activebackground="#3E405A", activeforeground="white")
    # Asignar evento del teclado
    root.bind(str(num), lambda event: operations.teclado_calculadora(self, str(num)))

def put_ce(self, root):
    self.btn_ce = Button(self.frame_numeros, text="CE", command=lambda:operations.opera(self, "ce"))
    self.btn_ce.grid(row=4, column=0, columnspan=4, sticky="nsew")
    self.btn_ce.config(bg="#676665", fg="white", font=("Calibri", 20,), relief="flat", borderwidth=2, activebackground="#252525", activeforeground="white")
    # Asignar evento del teclado
    root.bind("<space>", lambda event: operations.opera(self, "ce"))
