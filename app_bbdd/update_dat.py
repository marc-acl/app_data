from tkinter import*
import tkinter as tk
from ttkbootstrap import ttk
from ttkbootstrap import*
from PIL import Image, ImageTk
import connect_bbdd
from ttkbootstrap.dialogs import Messagebox
import create

class Update_Data():

    def __init__(self, notebook):       

        
        self.id = StringVar()
        self.name = StringVar()
        self.value = DoubleVar()
        self.param = DoubleVar()

        #First window frame
        self.notebook = notebook
        self.frame_window_update = Frame(self.notebook) 
        self.frame_window_update.pack(fill="both", expand=True)


        for i in range(2):
            self.frame_window_update.grid_columnconfigure(i, weight=1)
        for j in range(6):
            self.frame_window_update.grid_rowconfigure(j, weight=1)
            
        self.notebook.add(self.frame_window_update, text="Update")
        
        self.empty_label = tk.Label(self.frame_window_update, text="  Update Register", font = ("Arial", 14, "bold"), fg="#B4AB9E")
        self.empty_label.grid(row=0, column=0, columnspan=3, pady=5, sticky="nsew")

        self.label_id = tk.Label(self.frame_window_update, text="ID", font = ("Arial", 12, "bold"), fg="#B4AB9E")
        self.label_id.grid(row=1, column=0, padx=30, pady=5, sticky="nsew")

        self.entry_id = Entry(self.frame_window_update, bootstyle = "default", width=30, textvariable=self.id)
        self.entry_id.grid(row=1, column=1, padx=160, pady=5, sticky="ew")

        img_path = Image.open("app_bbdd/search.png")
        img_path = img_path.resize((37, 37), Image.LANCZOS)
        tk_img = ImageTk.PhotoImage(img_path)
        self.button_search = tk.Button(self.frame_window_update, borderwidth=0,
                                    highlightthickness=0,
                                    relief='flat', image=tk_img,
                                    command=lambda:self.search_id(self.id.get()))
        self.button_search.config(bg="#222222", activebackground="#222222")
        # self.button_search = Button(self.frame_window_update, image=tk_img, takefocus=0)
        # self.button_search.configure(style="Link.TButton", state="active")
        self.button_search.image = tk_img  # Keep a reference to avoid garbage collection
        self.button_search.grid(row=1, column=1, pady=5, padx=110, sticky="e")

        self.label_name = tk.Label(self.frame_window_update, text="Name", font = ("Arial", 12, "bold"), fg="#B4AB9E")
        self.label_name.grid(row=2, column=0, padx=30, pady=5, sticky="nsew")

        self.entry_name = Entry(self.frame_window_update, bootstyle = "default", width=30, textvariable=self.name)
        self.entry_name.grid(row=2, column=1, padx=160, pady=5, sticky="ew")

        self.label_value = tk.Label(self.frame_window_update, text="Value", font = ("Arial", 12, "bold"), fg="#B4AB9E")
        self.label_value.grid(row=3, column=0, padx=30, pady=5, sticky="nsew")

        self.entry_value = Entry(self.frame_window_update, bootstyle = "default", width=30, textvariable=self.value)
        self.entry_value.grid(row=3, column=1, padx=160, pady=5, sticky="ew")

        self.label_param = tk.Label(self.frame_window_update, text="Param", font = ("Arial", 12, "bold"), fg="#B4AB9E")
        self.label_param.grid(row=4, column=0, padx=30, pady=5, sticky="nsew")

        self.entry_param = Entry(self.frame_window_update, bootstyle = "default", width=30, textvariable=self.param)
        self.entry_param.grid(row=4, column=1, padx=160, pady=5, sticky="ew")

        self.label_comments = tk.Label(self.frame_window_update, text="Comments", font = ("Arial", 12, "bold"), fg="#B4AB9E")
        self.label_comments.grid(row=5, column=0, padx=30, pady=5, sticky="nsew")

        self.entry_comments = Text(self.frame_window_update, width=30, height=5)
        self.entry_comments.grid(row=5, column=1, pady=35, padx=160, sticky="nsew")

        self.comments_scroll = ttk.Scrollbar(self.frame_window_update, command=self.entry_comments.yview, bootstyle="round")
        self.entry_comments.config(yscrollcommand=self.comments_scroll.set)
        self.comments_scroll.grid(row=5, column=1, pady=35, padx=160, sticky="nse")

        self.button_update = Button(self.frame_window_update, text= "Update Register", bootstyle="success", command=lambda:self.update_data())
        self.button_update.configure(takefocus=0)
        self.button_update.grid(row=6, column=0, columnspan=3, pady=(5, 25), sticky="ns")


    def search_id(self, id):
        if self.validate_entry_id():
            list = connect_bbdd.Connect_BBDD()

            try:

                output_list = list.update_data_output(id)
                self.name.set(output_list[1])
                self.value.set(output_list[2])
                self.param.set(output_list[3])
                self.entry_comments.delete("1.0", "end")
                self.entry_comments.insert("1.0", output_list[4])

            except:
                return



    def validate_entry_id(self):

        if self.id.get() == "":
            Messagebox.show_warning("Please make sure the 'ID' field are not empty.", title='Database', parent=None, alert=True)
            return False
        else:
            try:
                isinstance(int(self.id.get()), int)
                return True
            except:
                Messagebox.show_warning("ID: Please enter a numeric value.", title='Database', parent=None, alert=True)
                return False
            

  


    def update_data(self):
        comments = self.entry_comments.get('1.0', 'end-1c').strip()
        validate_data = create.Create_Data(self)
        update_bbdd = connect_bbdd.Connect_BBDD()
        if validate_data.validate_entry(self):
            update_bbdd.update_data(self.id.get(), self.name.get(), self.value.get(), self.param.get(), comments)


        
        