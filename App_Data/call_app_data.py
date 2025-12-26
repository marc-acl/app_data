from tkinter import*
import customtkinter as ctk
from ttkbootstrap import*
from . import gui_app_create
from . import app_data_base


class User_Interface():

    def __init__(self, root_gui):

        self.root_gui = root_gui
        self.root_gui.configure(fg_color="#333333")
                       
        ctk.set_appearance_mode("dark") 
        self.width = 1350
        self.height = 700      
        
        self.screen_width = self.root_gui.winfo_screenwidth()
        self.screen_height = self.root_gui.winfo_screenheight()
        x = (self.screen_width // 2) - (self.width // 2)
        y = (self.screen_height // 2) - (self.height // 2)
        self.root_gui.geometry(f"{self.width}x{self.height}+{x}+{y}")
        
        gui_app_create.Create_Data(self.root_gui, self.gui_window_name)

    
    def gui_window_name(self, new_window_name):
        self.root_gui.title(new_window_name)



def main(): 
    root_using_gui = ctk.CTk()
    User_Interface(root_using_gui)
    root_using_gui.mainloop()

if __name__ == "__main__":
    main()