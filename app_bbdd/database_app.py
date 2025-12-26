import sqlite3
import ttkbootstrap
from ttkbootstrap.dialogs import Messagebox
import tkinter as tk
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox


class Connect_BBDD():

    def __init__(self):

        self.conexion = None
        
        try:
            self.conexion = sqlite3.connect('App_Data/dat_bbdd.db')
            self.cursor = self.conexion.cursor()
        except sqlite3.Error as e:
            CTkMessagebox(message="Failed to create the database: {e}",
                  icon="cancel", option_1="Ok")



    def create_conexion(self):

        try:
        
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS DATA (
                    ID INTEGER PRIMARY KEY,
                    NAME VARCHAR(50),
                    INITIAL_VALUE REAL,
                    FINAL_VALUE REAL,
                    VARIATION REAL,
                    COMMENTS TEXT
                )'''
            )

            CTkMessagebox(message="Connected to database successfully",
                  icon="check", option_1="Ok")
            
        except sqlite3.Error as e:
            CTkMessagebox(message="Error connecting to database: {e}",
                  icon="warning", option_1="Ok")
            

        

    def insert_data(self, list):
        
        self.cursor.execute("INSERT INTO DATA VALUES (?, ?, ?, ?, ?, ?)", list)
        self.conexion.commit()
        CTkMessagebox(message="Data record has been inserted.",
                  icon="check", option_1="Ok")
        

    def read_data(self, param, get_value):

        self.new_data_list = []


        if param == "ID" and get_value != "":
            query = "SELECT * FROM DATA WHERE ID = ?"
            value = (get_value,)

        elif param == "Name" and get_value != "":
            query = "SELECT * FROM DATA WHERE NAME = ?"
            value = (get_value,)

        elif (param == "Name" and get_value == "") or (param == "ID" and get_value == ""):
            query = "SELECT * FROM DATA"
            value = ""

        else:
            CTkMessagebox(message="Record is not found.",
                  icon="warning", option_1="Ok")
            return
        
        self.cursor.execute(query, value)

        self.output = self.cursor.fetchall()

    
        if not self.output:
            CTkMessagebox(message="Record is not found.",
                  icon="warning", option_1="Ok")
            return
    
        else:
            self.new_data_list = [list(i) for i in self.output]
            return self.new_data_list
        
        
        
        
    def verify_id(self, id):

        query = "SELECT * FROM DATA WHERE ID = ?"
        value = (id,)
        self.cursor.execute(query, value)
        self.output_id = self.cursor.fetchall()

        if self.output_id:
            CTkMessagebox(message="ID already exists.",
                icon="warning", option_1="Ok")
            return False
        else:
            return True

    

    def update_data(self, name, value, param, comments, id):
        variation = round((float(param)-float(value))/float(value)*100, 3)
        self.cursor.execute("""
                            UPDATE DATA SET NAME = ?, INITIAL_VALUE = ?, FINAL_VALUE = ?, VARIATION = ?, COMMENTS = ? WHERE ID = ? """
                            ,(name, value, param, variation, comments, id))
        self.conexion.commit()
        CTkMessagebox(message="Data record has been updated.",
                  icon="check", option_1="Ok")
        


    def delete_data(self, id):
        self.cursor.execute("""DELETE FROM DATA WHERE ID = ?""", (id,))
        self.conexion.commit()
        CTkMessagebox(message="Data record has been deleted.",
                  icon="check", option_1="Ok")
        


    def sort_data(self, value):
        self.sort_list = []
        self.cursor.execute(f"SELECT * FROM DATA ORDER BY {value} DESC")

        self.sort_list = [list(i) for i in self.cursor.fetchall()]
        return self.sort_list
    

    def get_column(self):

        self.cursor.execute("SELECT VARIATION FROM DATA")

        self.output_column = self.cursor.fetchall()
        self.column_var = [self.output_column[i][0] for i in range(len(self.output_column))]
        return self.column_var



        #Comprobar conexión a la base de datos
        def avaible_bbdd(self):

            pass


        


        

