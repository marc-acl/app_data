from tkinter import*
import tkinter as tk
from ttkbootstrap import ttk
from ttkbootstrap import*
from PIL import Image, ImageTk
import connect_bbdd
from ttkbootstrap.dialogs import Messagebox
import create

class Update_Data(create.Create_Data):

    def __init__(self, notebook):
        super().__init__(notebook)
        self.frame_window_update = self.frame_window_create
        self.notebook.add(self.frame_window_create, text="Update")
        self.button_create.config(text="Update")
        self.button_update = self.button_create
        self.button_update.config(command=lambda:self.update_data())
        self.empty_label.config(text="Update")


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
        update_bbdd = connect_bbdd.Connect_BBDD()
        if self.validate_entry():
            update_bbdd.update_data(self.id.get(), self.name.get(), self.value.get(), self.param.get(), comments)


        
        