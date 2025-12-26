from tkinter import*
import tkinter as tk
from ttkbootstrap import ttk
from ttkbootstrap import*
import create
import read_data
import updat_data
import delete_dat
import connect_bbdd
from ttkbootstrap.dialogs import Messagebox

class User_Interface():

    def __init__(self, window_user):
        
        #Add root
        self.root_gui = window_user
        style = Style("darkly")
        self.root_gui.title("Data Base")
        # bg_color = style.colors.bg
        # print("Color de fondo del tema:", bg_color)

        
        #Variables widgets
        self.id = IntVar()
        self.name = StringVar()
        self.value = DoubleVar()
        self.param = DoubleVar()  

        #Menubar
        self.menu_bar = Menu(self.root_gui)
        self.root_gui.config(menu=self.menu_bar)
        self.menu_bbdd = tk.Menu(self.menu_bar, tearoff=0)        
        self.menu_bbdd.add_command(label="Connect", command=lambda:create_bbdd_conexion(self))
        self.menu_bbdd.add_command(label="Exit", command=lambda:exit_app(self))
        self.menu_bbdd.add_command(label="Close")

        #Add menuroot
        self.menu_bar.add_cascade(menu=self.menu_bbdd, label="BBDD")

        #Container of windows
        self.notebook = ttk.Notebook(self.root_gui, height=900, width=800)
        self.notebook.pack(fill="both", expand=True)

        #Create conexion
        def create_bbdd_conexion(self):
            self.conexion_bbdd = connect_bbdd.Connect_BBDD()
            self.conexion_bbdd.create_conexion()


        def exit_app(self):

            self.answer = Messagebox.show_question(
                            title="Exit",
                            message="¿Are you sure you want to exit the application?",
                            buttons=["Yes", "No"],  # Texto de botones personalizado
                            alert=True)
            
            if self.answer:
                self.root_gui.destroy()

        # #First window frame
        create_data_bbdd = create.Create_Data(self.notebook)  
    

        #Second window frame
        read_data_bbddd = read_data.Read_Data(self.notebook)

        #Third window frame
        update_data_bbdd = updat_data.Update_Data(self.notebook)

        #Fourth window frame
        delete_data_bbdd = delete_dat.Delete_Data(self.notebook)

        

       

        self.root_gui.mainloop()

        
        

    
root_using_gui = Window()
User_Interface(root_using_gui)