import sqlite3
import ttkbootstrap
from ttkbootstrap.dialogs import Messagebox
import tkinter as tk

class Connect_BBDD():

    def __init__(self):
        
        try:
            self.conexion = sqlite3.connect('app_bbdd/dat_bbdd.db')
            self.cursor = self.conexion.cursor()
        except sqlite3.Error as e:
            pass
            #Messagebox.showerror(f"Error connecting to database: {e}")



    def create_conexion(self):

        try:
        
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS DATA (
                    ID INTEGER PRIMARY KEY,
                    NAME VARCHAR(50),
                    VALUE REAL,
                    PARAM REAL,
                    VARIATION REAL,
                    COMMENTS TEXT
                )'''
            )

            Messagebox.ok("Connected to database successfully", title='DataBase', alert=False, parent=None)

        except sqlite3.Error as e:
            Messagebox.show_warning("Error connecting to database: {e}", title='Database', parent=None, alert=True)
            

        

    def insert_data(self, list):
        
        self.cursor.execute("INSERT INTO DATA VALUES (?, ?, ?, ?, ?, ?)", list)
        self.conexion.commit()
        Messagebox.ok("Register has been insert", title="DataBase Insert Register", alert=False, parent=None)


    def read_data(self, param, id, name, table):

        for item in table.get_children():
            table.delete(item)


        if param == "ID" and id != "":
            query = "SELECT * FROM DATA WHERE ID = ?"
            value = (id,)

        elif param == "NAME" and name != "":
            query = "SELECT * FROM DATA WHERE NAME = ?"
            value = (name,)

        elif (param == "NAME" and name == "") or (param == "ID" and id == ""):
            query = "SELECT * FROM DATA"
            value = ""

        else:
            Messagebox.show_warning("Register is not found", title='Database', parent=None, alert=True)
            return
        
        self.cursor.execute(query, value)

        self.output = self.cursor.fetchall()

    
        if not self.output:
            Messagebox.show_warning("No records found", title='Database', parent=None, alert=True)
            return
    
        else:
            for i in self.output:
                table.insert('', tk.END, values=i)
        
        
        
    def update_data_output(self, id):

        if id != "":
            query = "SELECT * FROM DATA WHERE ID = ?"
            value = (id,)
        else:
            Messagebox.show_warning("Register is not found", title='Database', parent=None, alert=True)
            return
        
        self.cursor.execute(query, value)

        self.output = self.cursor.fetchall()

        if not self.output:
            Messagebox.show_warning("No records found", title='Database', parent=None, alert=True)
            return

        else:
            list = [self.output[0][0], self.output[0][1], self.output[0][2], self.output[0][3], self.output[0][4]]
    
        return list
    

    def update_data(self, id, name, value, param, comments):

        self.cursor.execute("""
                            UPDATE DATA SET NAME = ?, VALUE = ?, PARAM = ?, COMMENTS = ? WHERE ID = ? """
                            ,(name, value, param, comments, id))
        self.conexion.commit()
        Messagebox.ok("Register has been update", title="DataBase Update Register", alert=False, parent=None)


    def delete_data(self, id):
        self.cursor.execute("""DELETE FROM DATA WHERE ID = ?""", (id))
        self.conexion.commit()
        Messagebox.ok("Register has been delete", title="DataBase Delete Register", alert=False, parent=None)




        #Comprobar conexión a la base de datos
        def avaible_bbdd(self):

            pass


        


        

