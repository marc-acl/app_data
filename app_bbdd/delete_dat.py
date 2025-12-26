from tkinter import*
import tkinter as tk
from ttkbootstrap import ttk
from ttkbootstrap import*
import connect_bbdd
from ttkbootstrap.dialogs import Messagebox
import read_data
import updat_data
import create

class Delete_Data(read_data.Read_Data):

    def __init__(self, notebook):
        super().__init__(notebook)
         
        self.frame_window_delete = self.frame_window_read
        self.label_search_id.config(text="Search by ID")
        self.notebook.add(self.frame_window_delete, text="Delete")

        for w in [self.label_search_name, self.entry_search_name, self.button_searchb]:
            if hasattr(w, "destroy"):
                w.destroy()
        

        self.button_delete = Button(self.frame_window_delete, text= "Delete", bootstyle="success")
        self.button_delete.configure(takefocus=0)
        self.button_delete.grid(row=1, column=0, columnspan=3, pady=(5, 25))
        

        self.button_search.config(command=lambda: self.search_id_name("ID", self.id.get(), ""))

        def delete_item(self, id):
            pass
        
    