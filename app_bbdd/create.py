from tkinter import*
import tkinter as tk
from ttkbootstrap import ttk
from ttkbootstrap import*
import connect_bbdd
from ttkbootstrap.dialogs import Messagebox

class Create_Data():

    def __init__(self, notebook):

        self.id = StringVar()
        self.name = StringVar()
        self.value = DoubleVar()
        self.param = DoubleVar()

        #First window frame
        self.notebook = notebook
        self.frame_window_create = Frame(self.notebook) 
        self.frame_window_create.pack(fill="both", expand=True)


        for i in range(2):
            self.frame_window_create.grid_columnconfigure(i, weight=1)
        for j in range(6):
            self.frame_window_create.grid_rowconfigure(j, weight=1)
            
        self.notebook.add(self.frame_window_create, text="Create")

        #Entry widgets for create window
        #empty labels for spacing
        self.empty_label = tk.Label(self.frame_window_create, text="  Enter Data",font = ("Arial", 14, "bold"), fg="#B4AB9E")
        self.empty_label.grid(row=0, column=0, columnspan=3, pady=5, sticky="nsew")

        self.label_id = tk.Label(self.frame_window_create, text="ID", font = ("Arial", 12, "bold"), fg="#B4AB9E")
        self.label_id.grid(row=1, column=0, padx=30, pady=5, sticky="nsew")

        self.entry_id = Entry(self.frame_window_create, bootstyle = "default", width=30, textvariable=self.id)
        self.entry_id.grid(row=1, column=1, padx=160, pady=5, sticky="ew")
        self.id.trace_add('write', lambda *args: self.id.set(self.id.get()[:10]) if len(self.id.get()) > 10 else None)


        self.label_name = tk.Label(self.frame_window_create, text="Name", font = ("Arial", 12, "bold"), fg="#B4AB9E")
        self.label_name.grid(row=2, column=0, padx=30, pady=5, sticky="nsew")

        self.entry_name = Entry(self.frame_window_create, bootstyle = "default", width=30, textvariable=self.name)
        self.entry_name.grid(row=2, column=1, padx=160, pady=5, sticky="ew")
        self.name.trace_add('write', lambda *args: self.id.set(self.id.get()[:50]) if len(self.id.get()) > 50 else None )

        self.label_value = tk.Label(self.frame_window_create, text="Value", font = ("Arial", 12, "bold"), fg="#B4AB9E")
        self.label_value.grid(row=3, column=0, padx=30, pady=5, sticky="nsew")

        self.entry_value = Entry(self.frame_window_create, bootstyle = "default", width=30, textvariable=self.value)
        self.entry_value.grid(row=3, column=1, padx=160, pady=5, sticky="ew")

        self.label_param = tk.Label(self.frame_window_create, text="Param", font = ("Arial", 12, "bold"), fg="#B4AB9E")
        self.label_param.grid(row=4, column=0, padx=30, pady=5, sticky="nsew")

        self.entry_param = Entry(self.frame_window_create, bootstyle = "default", width=30, textvariable=self.param)
        self.entry_param.grid(row=4, column=1, padx=160, pady=5, sticky="ew")

        self.label_comments = tk.Label(self.frame_window_create, text="Comments", font = ("Arial", 12, "bold"), fg="#B4AB9E")
        self.label_comments.grid(row=5, column=0, padx=30, pady=5, sticky="nsew")

        self.entry_comments = Text(self.frame_window_create, width=30, height=5)
        self.entry_comments.configure()
        self.entry_comments.grid(row=5, column=1, pady=35, padx=160, sticky="nsew")
        self.entry_comments.bind("<KeyRelease>", self.limit_text)
        
        self.comments_scroll = ttk.Scrollbar(self.frame_window_create, command=self.entry_comments.yview, bootstyle="round")
        self.entry_comments.config(yscrollcommand=self.comments_scroll.set)
        self.comments_scroll.grid(row=5, column=1, pady=35, padx=160, sticky="nse")
    

        self.button_create = Button(self.frame_window_create, text= "Create Register", bootstyle="success", command=lambda:self.get_data_list())
        self.button_create.configure(takefocus=0)
        self.button_create.grid(row=6, column=0, columnspan=3, pady=(5, 25), sticky="ns")


    def get_data_list(self):

        if self.validate_entry():
            comments = self.entry_comments.get('1.0', 'end-1c').strip()
            self.list_create_register = [self.id.get(), self.name.get(), self.value.get(), self.param.get(), comments]
            for i in self.list_create_register:
                    print(i)
            bbdd = connect_bbdd.Connect_BBDD()
            bbdd.insert_data(self.list_create_register)


    def validate_entry(self):
        
        if self.id.get() == "":
            Messagebox.show_warning("Please make sure the 'Name' and 'ID' fields are not empty.", title='Database', parent=None, alert=True)
            return False
        
        elif self.name.get() == "":
            Messagebox.show_warning("Please make sure the 'Name' and 'ID' fields are not empty.", title='Database', parent=None, alert=True)
            return False
    
        elif self.id.get() != "" or self.name.get() != "" or self.entry_value.get() != "":
            
            if self.id.get() != "":
                try:
                    isinstance(int(self.id.get()), int)
                    if self.name.get() != "":
                        try:
                            isinstance(int(self.name.get()), int)
                            Messagebox.show_warning("Name: Please enter some text.", title='Database', parent=None, alert=True)
                            return False
                        except:
                            if self.entry_value.get() != "":
                                try:
                                    isinstance(float(self.value.get()), float)
                                    if self.entry_param.get() != "":
                                        try:
                                            isinstance(float(self.entry_param.get()), float)
                                            return True
                                        except:
                                            Messagebox.show_warning("Param: Please enter a numeric value.", title='Database', parent=None, alert=True)
                                            return False
                                except:
                                    Messagebox.show_warning("Value: Please enter a numeric value.", title='Database', parent=None, alert=True)
                                    return False
                except:
                    Messagebox.show_warning("ID: Please enter a numeric value.", title='Database', parent=None, alert=True)
                    return False
                                 
        else:
            return True
        

    def limit_text(self, event):
        content_comments = self.entry_comments.get("1.0", "end-1c")
        if len(content_comments) > 300:
            self.entry_comments.delete("1.0", "end")
            self.entry_comments.insert("1.0", content_comments[:300])
        
        

        





        
        