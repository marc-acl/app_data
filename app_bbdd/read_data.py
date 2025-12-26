from tkinter import*
import tkinter as tk
from ttkbootstrap import ttk
from ttkbootstrap import*
import connect_bbdd
from ttkbootstrap.dialogs import Messagebox

class Read_Data():

    def __init__(self, notebook):
        #Second window frame
        #Variables widgets
        self.id = StringVar()
        self.name = StringVar()
        self.value = DoubleVar()
        self.param = DoubleVar()
        self.comments = "" 

        self.notebook = notebook
        self.frame_window_read = Frame(self.notebook)
        self.frame_window_read.pack(fill="both", expand=True)

        # Configurar grid
        self.frame_window_read.grid_columnconfigure(0, weight=0)  # columna labels
        self.frame_window_read.grid_columnconfigure(1, weight=1)  # columna entries
        for j in range(2):
            self.frame_window_read.grid_rowconfigure(j, weight=1) 
        
        self.frame_window_read.grid_rowconfigure(2, weight=10)

        self.notebook.add(self.frame_window_read, text="Read")


        #create label
        #empty labels for spacing
        self.label_search_id = tk.Label(self.frame_window_read, text="Search by ID", font = ("Arial", 12, "bold"), fg="#B4AB9E")
        self.label_search_id.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

        self.entry_search_id = Entry(self.frame_window_read, bootstyle = "default", width=30, textvariable=self.id)
        self.entry_search_id.grid(row=0, column=1, padx=160, pady=5, sticky="ew")
        self.id.trace_add('write', lambda *args: self.id.set(self.id.get()[:10]) if len(self.id.get()) > 10 else None)
        

        self.label_search_name = tk.Label(self.frame_window_read, text="Search by Name", font = ("Arial", 12, "bold"), fg="#B4AB9E")
        self.label_search_name.grid(row=1, column=0, padx=30, pady=5, sticky="ew")

        self.entry_search_name = Entry(self.frame_window_read, bootstyle = "default", width=30, textvariable=self.name)
        self.entry_search_name.grid(row=1, column=1, padx=160, pady=5, sticky="ew")
        self.name.trace_add('write', lambda *args: self.id.set(self.id.get()[:50]) if len(self.id.get()) > 50 else None )
    


        # Crear Treeview (tabla)
        self.table_output = Treeview(self.frame_window_read, columns=("Col1", "Col2", "Col3", "Col4", "Col5"), show="headings")
        self.table_output.heading("Col1", text="ID")
        self.table_output.heading("Col2", text="Name")
        self.table_output.heading("Col3", text="Value")
        self.table_output.heading("Col4", text="Param")
        self.table_output.heading("Col5", text="Comments")

        #configurar el tamaño de las columnas
        self.table_output.column("Col1", width=50, anchor='center')
        self.table_output.column("Col2", width=150, anchor='center')
        self.table_output.column("Col3", width=100, anchor='center')
        self.table_output.column("Col4", width=50, anchor='center')
        self.table_output.column("Col5", width=260, anchor='center')

        # Ubicar elementos
        self.table_output.grid(row=2, column=0, columnspan=2, sticky="nsew")
        

        self.comments_scroll = ttk.Scrollbar(self.frame_window_read, command=self.table_output.yview, bootstyle="round")
        self.table_output.config(yscrollcommand=self.comments_scroll.set)
        self.comments_scroll.grid(row=2, column=0, columnspan=2, sticky="nse")


        img_path = Image.open("app_bbdd/search.png")
        img_path = img_path.resize((37, 37), Image.LANCZOS)
        tk_img = ImageTk.PhotoImage(img_path)

        self.button_searchb = tk.Button(
            self.frame_window_read,
            borderwidth=0,
            highlightthickness=0,
            relief='flat', image=tk_img,
            command=lambda:self.search_id_name("NAME", "", self.name.get()))
        self.button_searchb.config(bg="#222222", activebackground="#222222") 
        self.button_searchb.image = tk_img  # Keep a reference to avoid garbage collection
        self.button_searchb.grid(row=1, column=1, pady=5, padx=110, sticky="e")


        self.button_search = tk.Button(
            self.frame_window_read,
            borderwidth=0,
            highlightthickness=0,
            relief='flat', image=tk_img,
            command=lambda:self.search_id_name("ID", self.id.get(), ""))
        self.button_search.config(bg="#222222", activebackground="#222222")
        # self.button_search = Button(self.frame_window_update, image=tk_img, takefocus=0)
        # self.button_search.configure(style="Link.TButton", state="active")
        self.button_search.image = tk_img  # Keep a reference to avoid garbage collection
        self.button_search.grid(row=0, column=1, pady=5, padx=110, sticky="e")


    def search_id_name(self, param, id, name):
       if  self.validate_entry_read(param, id, name):
            search_id_bbdd = connect_bbdd.Connect_BBDD()
            search_id_bbdd.read_data(param, id, name, self.table_output)


    def validate_entry_read(self, param, id, name):
    
        if param == "ID" and id != "":
            try:
                isinstance(int(id), int)
                return True
            except:
                Messagebox.show_warning("Please enter a numeric value.", title='Database', parent=None, alert=True)
                return False
                
        
        elif param == "NAME" and name != "":
            try:
                isinstance(int(name), int)
                Messagebox.show_warning("Please enter some text.", title='Database', parent=None, alert=True)
                return False
            
            except:
                
                return True
        
        else:
            return True







