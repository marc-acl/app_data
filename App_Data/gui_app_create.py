from tkinter import*
from ttkbootstrap import*
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from CTkTable import *
from CTkTableRowSelector import *
from . import app_data_base
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from App_Data import api_stocks as st
import ctkdlib  
import threading
from matplotlib.figure import Figure
import matplotlib as mpl
import numpy as np
import os
from matplotlib.patches import Rectangle

INTER_FONT = os.path.join(os.path.dirname(__file__), "InterVariable.ttf")



class Create_Data(ctk.CTkFrame):

    

    def __init__(self, root_gui, *args, **kwargs):
        super().__init__(root_gui, *args, **kwargs)

        self.id = StringVar()
        self.name = StringVar()
        self.value = StringVar()
        self.param = StringVar()
        self.search = StringVar()
        self.optinomenu_var = StringVar()
        self.ticker = StringVar()
        self.toplevel_window = None
        self.toplevel_window_picker = None
        ctk.set_appearance_mode("dark")
        self.bind("<Configure>", self.on_resize)
        self.radio_var = IntVar(value=0)
        self.list_table=[["ID", "Name", "Final Value", "Initial Value", "Variation", "Comment"]]
        self.column_num = 6
        self.current_date_str = StringVar()
        self.last_date_str = StringVar()
        

        ctk.FontManager.load_font("App_Data/Inter.ttc")

        #First window frame
        self.root_gui = root_gui
        self.frame_create = ctk.CTkFrame(root_gui, fg_color="#333333")
        self.frame_create.pack(fill="both", expand=True, padx=5, pady=5)
        

        self.set_frame_left(self.frame_create)
        self.set_frame_right(self.frame_create)
        self.center_top_frame(self.frame_create)
        self.center_bottom_framel(self.frame_create)
        self.center_bottom_framer(self.frame_create)
        self.set_table(self.list_table, self.column_num)
        
        
        # Entry widgets for create window
        # empty labels for spacing
    def set_frame_left(self, frame_create):

        self.frame_left = ctk.CTkFrame(frame_create, width=300)
        self.frame_left.grid_propagate(False)
        self.frame_left.pack(fill="both", expand=False, padx=5, pady=5, side="left")

        for i in range(1):
            self.frame_left.grid_columnconfigure(i, weight=1)
        for j in range(11):
            self.frame_left.grid_rowconfigure(j, weight=1)


        self.empty_label = ctk.CTkLabel(self.frame_left, text="Create Record", font = ("Inter ExtraBold", 20), fg_color="transparent")
        self.empty_label.grid(row=0, column=0, columnspan=3, pady=(25, 10))

        self.label_id = ctk.CTkLabel(self.frame_left, text="ID", font = ("Inter ExtraBold", 15), fg_color="transparent")
        self.label_id.grid(row=1, column=0, padx=30, pady=10, sticky="ew")

        self.entry_id = ctk.CTkEntry(self.frame_left,  textvariable=self.id)
        self.entry_id.grid(row=2, column=0, padx=30, pady=10, sticky="ew")
        self.id.trace_add('write', lambda *args: self.id.set(self.id.get()[:30]) if len(self.id.get()) > 30 else None)


        self.entry_name = ctk.CTkEntry(self.frame_left, textvariable=self.name)
        self.entry_name.grid(row=4, column=0, padx=30, pady=10, sticky="ew")
        self.name.trace_add('write', lambda *args: self.name.set(self.name.get()[:50]) if len(self.name.get()) > 50 else None )

        
        #current = self.last_date_str.get() selected date = comparable date
        self.button_current_price = ctk.CTkButton(self.frame_left, text="Current Price", command=lambda:self.date_pick(0, 340, self.entry_value, self.value, self.name.get(), self.current_date_str, last = self.last_date_str.get()),
                                        font=ctk.CTkFont(family="Inter ExtraBold", size=15), width=100)
        self.button_current_price.grid(row=5, column=0, padx=30, pady=10)

        self.entry_value = ctk.CTkEntry(self.frame_left, textvariable=self.value)
        self.entry_value.grid(row=6, column=0, padx=30, pady=10, sticky="ew")
        self.value.trace_add('write', lambda *args: self.value.set(self.value.get()[:10]) if len(self.value.get()) > 10 else None)

        self.button_last_price = ctk.CTkButton(self.frame_left, text="Last Price", command=lambda:self.date_pick(0, 340, self.entry_param, self.param, self.name.get(), self.last_date_str, current = self.current_date_str.get()),
                                        font=ctk.CTkFont(family="Inter ExtraBold", size=15), width=100)
        self.button_last_price.grid(row=7, column=0, padx=30, pady=10)

        self.entry_param = ctk.CTkEntry(self.frame_left, textvariable=self.param)
        self.entry_param.grid(row=8, column=0, padx=30, pady=10, sticky="ew")
        self.param.trace_add('write', lambda *args: self.param.set(self.param.get()[:10]) if len(self.param.get()) > 10 else None)

        self.label_comments = ctk.CTkLabel(self.frame_left, text="Comments", font = ("Inter ExtraBold", 15), fg_color="transparent")
        self.label_comments.grid(row=9, column=0, pady=10, padx=30, sticky="ew")

        self.entry_comments = ctk.CTkTextbox(self.frame_left, height=80)
        self.entry_comments.grid(row=10, column=0, pady=10, padx=30, sticky="ew")
        self.entry_comments.bind("<KeyRelease>", self.limit_text)
         
        self.button_ticker = ctk.CTkButton(self.frame_left, text="Ticker", command=lambda:st.create_ticker(self.name.get(), self.value, self.param, self.entry_comments, self.current_date_str, self.last_date_str),
                                        font=ctk.CTkFont(family="Inter ExtraBold", size=15), width=100)
        self.button_ticker.grid(row=3, column=0, padx=30, pady=10)
        
        self.button_create = ctk.CTkButton(self.frame_left, text="Create", command=lambda:self.run_in_thread(self.get_data_list, self.id, self.name, self.value, self.param, self.entry_comments),
                                        font=ctk.CTkFont(family="Inter ExtraBold", size=15), width=100)
        self.button_create.grid(row=11, column=0, columnspan=3, pady=30)



    # #Frame right
    def set_frame_right(self, frame_create):
        
        self.frame_right = ctk.CTkFrame(frame_create, width=300)
        self.frame_right.grid_propagate(False)
        self.frame_right.pack(fill="both", expand=False, padx=5, pady=5, side="right")

        for i in range(1):
            self.frame_right.grid_columnconfigure(i, weight=1)
        for j in range(11):
            self.frame_right.grid_rowconfigure(j, weight=1)

        self.label_dba = ctk.CTkLabel(self.frame_right, text="Database Administrator", font = ("Inter ExtraBold", 20), fg_color="transparent")
        self.label_dba.grid(row=0, column=0, pady=(16, 10), padx=30)

        self.button_read = ctk.CTkButton(self.frame_right, text= "Get Data ",command=lambda:self.get_all_data(),
                                        font=ctk.CTkFont(family="Inter ExtraBold", size=15), width=100)
        self.button_read.grid(row=1, column=0, pady=(10, 10), padx=30)
        
        self.optionmenu = ctk.CTkOptionMenu(self.frame_right, values=["ID", "Name"], width=100,
                                            font=ctk.CTkFont(family="Inter ExtraBold", size=15), variable=self.optinomenu_var)
        self.optionmenu.set("ID")
        self.optionmenu.grid(row=2, column=0, pady=(10, 5), padx=30)

        self.entry_search = ctk.CTkEntry(self.frame_right, textvariable=self.search)
        self.entry_search.grid(row=3, column=0, padx=30, pady=(5, 5), sticky='ew')

        self.button_search = ctk.CTkButton(self.frame_right, text= "Search",command=lambda:self.search_id_name(self.optinomenu_var.get(), self.search.get()),
                                        font=ctk.CTkFont(family="Inter ExtraBold", size=15), width=100)
        self.button_search.grid(row=4, column=0, pady=(5, 10), padx=30)
        

        self.button_update = ctk.CTkButton(self.frame_right, text= "Update", command=lambda:self.open_toplevel(self.row_selector.get()),
                                        font=ctk.CTkFont(family="Inter ExtraBold", size=15), width=100)
        self.button_update.grid(row=5, column=0, pady=10, padx=30)
        

        self.button_delete = ctk.CTkButton(self.frame_right, text= "Delete", command=lambda:self.ask_delete(self.row_selector.get()),
                                        font=ctk.CTkFont(family="Inter ExtraBold", size=15), width=100)
        self.button_delete.grid(row=6, column=0, pady=10, padx=30)

        self.button_delete = ctk.CTkButton(self.frame_right, text= "Graph", command=lambda:self.open_toplevel_graph(),
                                        font=ctk.CTkFont(family="Inter ExtraBold", size=15), width=100)
        self.button_delete.grid(row=7, column=0, pady=10, padx=30)

        self.button_create_bbdd = ctk.CTkButton(self.frame_right, text= "Connect", command=lambda:self.open_toplevel_connect(),
                                        font=ctk.CTkFont(family="Inter ExtraBold", size=15), width=100)
        self.button_create_bbdd.grid(row=10, column=0, pady=10, padx=30)

        self.button_create_bbdd = ctk.CTkButton(self.frame_right, text= "Close", command=lambda:self.exit_app(),
                                        font=ctk.CTkFont(family="Inter ExtraBold", size=15), width=100)
        self.button_create_bbdd.grid(row=11, column=0, pady=(10, 30), padx=30)


    
    def deco_function(parameter_function):
        def internal_function(self, *args, **kwargs):
            status = app_data_base.Connect_BBDD()
            if not status.connection_status():
                CTkMessagebox(title="Info", message="Please, create a connexion to database", icon="info")
                return
            else:
                parameter_function(self, *args, **kwargs)

        return internal_function
   
    

    def run_in_thread(self, func, *args, **kwargs):
        threading.Thread(target=func, args=args, kwargs=kwargs, daemon=True).start()
    


    def date_pick(self, x, y, entry_variable, get_date_stock, stock, current_last_date, **kwargs):

        if stock == "":
            CTkMessagebox(title="Info", message="Please, insert a ticker code", icon="info")
            return

        if self.toplevel_window_picker is None or not self.toplevel_window_picker.winfo_exists():
            
            self.one_date_entry = entry_variable
            self.toplevel_window_picker = CTkDatePicker(self.one_date_entry, get_date_stock, stock, kwargs)
    

        self.toplevel_window_picker.toggle(x, y, entry_variable, stock, get_date_stock, current_last_date, kwargs)
        
    

    def center_top_frame(self, frame_create):
        
        self.frame_center_top = ctk.CTkScrollableFrame(frame_create,
                                            fg_color=ctk.ThemeManager.theme["CTkFrame"]["fg_color"],
                                            bg_color=ctk.ThemeManager.theme["CTkFrame"]["fg_color"],
                                            height=400)

        self.frame_center_top.pack(fill='both', expand= False, padx=5, pady=5, side="top")

    

    def center_bottom_framel(self, frame_create):

        self.frame_center = ctk.CTkFrame(frame_create, fg_color=ctk.ThemeManager.theme["CTkFrame"]["fg_color"],
                                         width=500)
        self.frame_center.grid_propagate(False)
        self.frame_center.pack(fill='both', expand= False, padx=5, pady=5, side="left")


        

    def center_bottom_framer(self, frame_create):

        self.frame_center_bottom = ctk.CTkFrame(frame_create, fg_color=ctk.ThemeManager.theme["CTkFrame"]["fg_color"],
                                                width=300)
        self.frame_center_bottom.grid_propagate(False)
        self.frame_center_bottom.pack(fill='both', expand= False, padx=5, pady=5, side="right")

        for i in range(1):
            self.frame_center_bottom.grid_columnconfigure(i, weight=1)
        for j in range(4):
            self.frame_center_bottom.grid_rowconfigure(j, weight=1)


        radiobutton_1 = customtkinter.CTkRadioButton(self.frame_center_bottom, text="Final Value", font = ("Inter ExtraBold", 15),
                                            variable= self.radio_var, value=1, radiobutton_width=15, radiobutton_height=15)
        radiobutton_1.grid(row=0, column=0, pady=(27, 18), sticky = 'n')

        radiobutton_2 = customtkinter.CTkRadioButton(self.frame_center_bottom, text="Initial Value", font = ("Inter ExtraBold", 15),
                                            variable= self.radio_var, value=2, radiobutton_width=15, radiobutton_height=15)
        radiobutton_2.grid(row=1, column=0, pady=18, sticky = 'n')

        radiobutton_3 = customtkinter.CTkRadioButton(self.frame_center_bottom, text="Variation  ", font = ("Inter ExtraBold", 15),
                                            variable= self.radio_var, value=3, radiobutton_width=15, radiobutton_height=15)
        radiobutton_3.grid(row=2, column=0, pady=18, sticky = 'n')

        self.button_sort = ctk.CTkButton(self.frame_center_bottom, text= "Sort", command=lambda:self.sort_table(self.radio_var.get()),
                                        font=ctk.CTkFont(family="Inter ExtraBold", size=15), width=100)
        self.button_sort.grid(row=4, column=0, pady=(18, 30), sticky="n")



    @deco_function
    def sort_table(self, value):

        if value != 0:
            self.value_list = ["", "INITIAL_VALUE", "FINAL_VALUE", "VARIATION"]
            self.column_sort = self.value_list[value]
            self.sort_bbdd = app_data_base.Connect_BBDD()
            self.sort_output_data = self.sort_bbdd.sort_data(self.column_sort)

            #delete last table
            rows = len(self.table_output.get())
            for j in reversed(range(1, rows)):
                try:
                    self.table_output.delete_row(j)
                except Exception as e:
                    print(f"Warning deleting row {j}: {e}")
            #set new data
            if self.sort_output_data:
                for row in self.sort_output_data:
                    self.table_output.add_row(row)

        else:
            return




    def on_resize(self, event):
        if hasattr(self, "_resize_after_id"):
            self.after_cancel(self._resize_after_id)
        self._resize_after_id = self.after(200, lambda: self.table_output.update_idletasks())


    
    def set_table(self, list_table, column_num):
        
        self.table_output = CTkTable(self.frame_center_top, column=column_num, values=list_table, anchor="center",
                                    font=ctk.CTkFont(family="Inter", size=14), text_color="#C0C0C0")
        self.table_output.pack()
        self.row_selector = CTkTableRowSelector(self.table_output, can_select_headers=False, max_selection=True)



    @deco_function
    def open_toplevel(self, row_selector_list):

        if row_selector_list:
        
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = ToplevelWindow(self, self)
                self.toplevel_window.set_data_window(self.row_selector.get())
            elif self.open_toplevel_connect:
                self.toplevel_window.set_data_window(self.row_selector.get())
                return
            else:
                self.toplevel_window.focus()
                self.toplevel_window.set_data_window(self.row_selector.get())
        else:
            CTkMessagebox(title='Database Warning', message="Please select a row.",
                          icon="warning", option_1="Ok")
            return



    def open_toplevel_connect(self):
        
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindowI(self)  # create window if its None or destroyed
        elif self.open_toplevel:
            return            
        else:
            self.toplevel_window.focus()  # if window exists focus it


    @deco_function
    def open_toplevel_graph(self):
        
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindowII(self, self)  # create window if its None or destroyed
            self.toplevel_window.tickers_option()
        elif self.open_toplevel:
            return            
        else:
            self.toplevel_window.focus()  # if window exists focus it
            self.toplevel_window.tickers_option()



    @deco_function
    def get_data_list(self, id, name, value, param, comments):
        
        if self.validate_entry(num_id = id.get(), str_name = name.get(), num_current_price = value.get(), num_last_price = param.get()):
            self.variation = round((float(value.get())-float(param.get()))/float(param.get())*100, 3)
            self.comments = comments.get('1.0', 'end-1c').strip()
            self.list_create_register = [id.get(), name.get(), float(value.get()), float(param.get()), self.variation, self.comments]
            
            bbdd = app_data_base.Connect_BBDD()

            def task(): 
                success = False
                if bbdd.verify_id(id.get()):
                    success = bbdd.insert_data(self.list_create_register)
                    
                
                def gui_update():
                    if success:
                        msg = CTkMessagebox(message="Data record has been inserted.",
                        icon="check", option_1="Ok")                        
                        self.cleaner_data(id, name, value, param, comments)
                        response = msg.get()
                        if response == 'Ok':
                            self.get_all_data()
                            
                    else:
                        CTkMessagebox(message="Error inserting data.", icon="warning", option_1="Ok")
                        return
                self.root_gui.after(0, gui_update)
                

            threading.Thread(target=task, daemon=True).start()

                    
    
    def cleaner_data(self, *args):

        for i in args:
            if type(i) == ctk.CTkTextbox:
                i.delete("1.0", ctk.END)
            else:
                i.set("")
       


    @deco_function
    def search_id_name(self, option, search):

        option_menu = ("num_" if option == "ID" else "str_")+option
        if  self.validate_entry(**{option_menu:search}):
            search_id_bbdd = app_data_base.Connect_BBDD()
            self.output_list = search_id_bbdd.read_data(option, search)

            try:
                self.row_selector.clear_selection()
            except Exception as e:
                pass
            
            rows = len(self.table_output.get())
            for j in reversed(range(1, rows)): 
                try:
                    self.table_output.delete_row(j)
                except Exception as e:
                    print(f"Warning deleting row {j}: {e}")  
            if self.output_list:
                for i in self.output_list:
                    self.table_output.add_row(i)
            else:
                CTkMessagebox(title="Info", message="No data available.", icon="info")
                
                

    @deco_function
    def get_all_data(self):
        get_all = app_data_base.Connect_BBDD()
        self.output_get_data = get_all.read_data("Name", "")

        try:
            self.row_selector.clear_selection()
        except Exception as e:
            pass
        # delete last table
        rows = len(self.table_output.get())
        for j in reversed(range(1, rows)):
            try:
                self.table_output.delete_row(j)
            except Exception as e:
                print(f"Warning deleting row {j}: {e}")
         #set new data
        if self.output_get_data:
            for row in self.output_get_data:
                self.table_output.add_row(row)
        else:
            CTkMessagebox(title="Info", message="No data available.", icon="info")

        self.current_date_str.set("")
        self.last_date_str.set("")



    @deco_function
    def update_data_table(self, name, value, param, comments, id):
        if self.validate_entry(num_id = id, str_name = name, num_value = value, num_param = param):
            self.update_bbdd = app_data_base.Connect_BBDD()

            def task(): 
                success = False
                success = self.update_bbdd.update_data(name, value, param, comments, id)

                def gui_update():
                    if success:
                        msg = CTkMessagebox(message="Data record has been updated.",
                            icon="check", option_1="Ok")
                        response = msg.get()
                        if response == 'Ok':
                            self.get_all_data()
                    else:
                        CTkMessagebox(message="Error updating data.", icon="warning", option_1="Ok")
                        return
                self.root_gui.after(0, gui_update)

            threading.Thread(target=task, daemon=True).start()   
    


    @deco_function
    def delete_data(self, row_selector_list):
        if row_selector_list:
            id_delete = row_selector_list[0][0]
            delete_data_bbdd = app_data_base.Connect_BBDD()
            delete_data_bbdd.delete_data(id_delete)

            if delete_data_bbdd.delete_data(id_delete):
                msg = CTkMessagebox(message="Data record has been deleted.",
                            icon="check", option_1="Ok")
                response = msg.get()
                if response == 'Ok':
                    self.get_all_data()              
        else:
            CTkMessagebox(title='Database Warning', message="Please select a row.",
                          icon="warning", option_1="Ok")
            return
        
        

    def ask_delete(self, row_selector_list):
        
        if row_selector_list:
            msg = CTkMessagebox(title="Warning", message=f"¿Do you want to delete the record {row_selector_list[0][0]} ?",
                                icon="question", option_1="Cancel", option_2="No", option_3="Yes")
            response = msg.get()

            if response=="Yes":
                self.delete_data(row_selector_list)     
            else:
                return
        else: 
            CTkMessagebox(title='Database Warning', message="Please select a row.",
                          icon="warning", option_1="Ok")

    #graphic analysis
    @deco_function
    def variation_ratio(self, list):

        if len(list) > 5:
            CTkMessagebox(title='Database Warning', message="Please select only five tickers.",
                          icon="warning", option_1="Ok")
            return
        
        elif len(list) == 0:
            CTkMessagebox(title='Database Warning', message="No data available in the table.",
                          icon="warning", option_1="Ok")
            return

        else:

            #get data      
            tickers_list = [i[0] for i in list]
            tickers_var = [i[1] for i in list]


            fig = Figure(figsize=(7, 4), facecolor= '#2b2b2b') 
            ax = fig.add_subplot()
            ax.set_facecolor('#2b2b2b')

            # Marco alrededor de todas las barras
            for spine in ax.spines.values():
                spine.set_edgecolor("#333333")  # color del marco
                spine.set_linewidth(2)        # grosor

            gradient = np.linspace(0, 1, 256).reshape(1, -1) 
            for i, (label, value) in enumerate(zip(tickers_list, tickers_var)):
                ax.imshow(
                gradient,
                aspect='auto',
                cmap=mpl.cm.viridis,
                alpha=0.4, 
                extent=[0, value, i - 0.4, i + 0.4]
        )
                
                ax.add_patch(
                Rectangle(
                    (0, i - 0.4),
                    value,
                    0.8,
                    linewidth=2,
                    edgecolor="none",
                    facecolor="none"
                )
        )

            ax.set_yticks(np.arange(len(tickers_list)))
            ax.set_yticklabels(tickers_list, color="white")
            ax.set_xlabel("Variation %", color="white")
            ax.set_title("AVG Percentage Change", color="white")
            ax.invert_yaxis()
            ax.tick_params(colors="white")
            fig.subplots_adjust(bottom=0.15)
            x_min = min(tickers_var) * 1.1 if min(tickers_var) < 0 else 0
            x_max = max(tickers_var) * 1.1
            ax.set_xlim(x_min, x_max)

         

            #clean frame
            for widget in self.frame_center.winfo_children():
                widget.destroy()

            #insert fig
            canvas = FigureCanvasTkAgg(fig, self.frame_center)
            canvas.draw()
            canvas.get_tk_widget().pack(fill="both", expand=False)

            

    def validate_entry(self, **kwargs):
        verify_result = False
        for key, value in kwargs.items():
            if key.__contains__("num"):
                try:
                    isinstance(float(value), float)
                    verify_result= True
                except:
                    CTkMessagebox(title='Database', message=f"{key.split("_", 1)[1]}: Please enter a numeric value.",
                                                            icon="warning", option_1="Ok")
                    return
                    
            elif key.__contains__("str"):
                try:
                    isinstance(float(value), float)
                    CTkMessagebox(title='Database Warning', message=f"{key.split("_", 1)[1]}: Please enter some text.",
                                            icon="warning", option_1="Ok")
                    return
                    
                except:
                    verify_result = True
        
        return verify_result
        


    def validate_entry_read(self, param, value):
    
        if param == "ID" and value != "":
            try:
                isinstance(int(value), int)
                return True
            except:
                CTkMessagebox(title='Database', message="Please enter a numeric value.",
                                                   icon="warning", option_1="Ok")
                return False
                
        elif param == "Name" and value != "":
            try:
                isinstance(int(value), int)
                CTkMessagebox(title='Database', message="Please enter some text.",
                                                   icon="warning", option_1="Ok")
                return False
            
            except:
                
                return True
        
        else:
            return True
        


    def limit_text(self, event):
        content_comments = self.entry_comments.get("1.0", "end-1c")
        if len(content_comments) > 300:
            self.entry_comments.delete("1.0", "end")
            self.entry_comments.insert("1.0", content_comments[:300])



    def exit_app(self):

        msg = CTkMessagebox(title="Exit", message="¿Do you want to close the database?",
                            icon="question", option_1="Cancel", option_2="No", option_3="Yes")
        response = msg.get()

        if response=="Yes":
            self.close_connection = app_data_base.Connect_BBDD()
            self.close_connection.close()
            try:
                self.row_selector.clear_selection()
            except Exception as e:
                pass
            rows = len(self.table_output.get())
            for j in reversed(range(1, rows)):
                try:
                    self.table_output.delete_row(j)
                except Exception as e:
                    print(f"Warning deleting row {j}: {e}")

            for widget in self.frame_center.winfo_children():
                widget.destroy()  
        else:
            return
            

        

class ToplevelWindow(ctk.CTkToplevel):
    
    def __init__(self, parent, data_instance):
        super().__init__(parent)

        self.withdraw()
        self.configure(fg_color="#333333")

        self.geometry("300x685")
        self.resizable(False, False)
        self.transient(parent)
        self.lift()

        self.id = StringVar()
        self.name = StringVar()
        self.value = StringVar()
        self.param = StringVar()
        self.current_date_str = StringVar()
        self.last_date_str = StringVar()

        self.window_data_entry(data_instance)

        self.after(470, self.deiconify)


    def window_data_entry(self, data_instance):

        for i in range(1):
            self.grid_columnconfigure(i, weight=1)
        for j in range(11):
            self.grid_rowconfigure(j, weight=1)


        self.empty_label = ctk.CTkLabel(self, text="Update Record", font = ("Inter ExtraBold", 20), fg_color="transparent")
        self.empty_label.grid(row=0, column=0, columnspan=3, pady=(25, 10))

        self.label_id = ctk.CTkLabel(self, text="ID", font = ("Inter ExtraBold", 15), fg_color="transparent")
        self.label_id.grid(row=1, column=0, padx=30, pady=10, sticky="ew")

        self.entry_id = ctk.CTkEntry(self,  textvariable=self.id, state="readonly")
        self.entry_id.grid(row=2, column=0, padx=30, pady=10, sticky="ew")
        self.id.trace_add('write', lambda *args: self.id.set(self.id.get()[:30]) if len(self.id.get()) > 30 else None)

        self.entry_name = ctk.CTkEntry(self, textvariable=self.name)
        self.entry_name.grid(row=4, column=0, padx=30, pady=10, sticky="ew")
        self.name.trace_add('write', lambda *args: self.name.set(self.name.get()[:50]) if len(self.name.get()) > 50 else None )
        
        self.button_current_price = ctk.CTkButton(self, text="Current Price", command=lambda:data_instance.date_pick(0, 340, self.entry_value, self.value, self.name.get(), self.current_date_str, last = self.last_date_str.get()),
                                        font=ctk.CTkFont(family="Inter ExtraBold", size=15), width=100)
        self.button_current_price.grid(row=5, column=0, padx=30, pady=10)

        self.entry_value = ctk.CTkEntry(self, textvariable=self.value)
        self.entry_value.grid(row=6, column=0, padx=30, pady=10, sticky="ew")
        self.value.trace_add('write', lambda *args: self.value.set(self.value.get()[:10]) if len(self.value.get()) > 10 else None )
        
        self.button_last_price = ctk.CTkButton(self, text="Last Price", command=lambda:data_instance.date_pick(0, 340, self.entry_param, self.param, self.name.get(), self.last_date_str, current = self.current_date_str.get()),
                                        font=ctk.CTkFont(family="Inter ExtraBold", size=15), width=100)
        self.button_last_price.grid(row=7, column=0, padx=30, pady=10)

        self.entry_param = ctk.CTkEntry(self, textvariable=self.param)
        self.entry_param.grid(row=8, column=0, padx=30, pady=10, sticky="ew")
        self.param.trace_add('write', lambda *args: self.param.set(self.param.get()[:10]) if len(self.param.get()) > 10 else None )
        
        self.label_comments = ctk.CTkLabel(self, text="Comments", font = ("Inter ExtraBold", 15), fg_color="transparent")
        self.label_comments.grid(row=9, column=0, pady=10, padx=30, sticky="ew")

        self.entry_comments = ctk.CTkTextbox(self, height=80)
        self.entry_comments.grid(row=10, column=0, pady=10, padx=30, sticky="ew")
        self.entry_comments.bind("<KeyRelease>", data_instance.limit_text)

        self.button_ticker = ctk.CTkButton(self, text="Ticker", command=lambda:st.create_ticker(self.name.get(), self.value, self.param, self.entry_comments, self.current_date_str, self.last_date_str),
                                        font=ctk.CTkFont(family="Inter ExtraBold", size=15), width=100)
        self.button_ticker.grid(row=3, column=0, padx=30, pady=10)
        
        self.button_create = ctk.CTkButton(self, text="Update", command=lambda:data_instance.run_in_thread(data_instance.update_data_table, self.name.get(), self.value.get(), self.param.get(), self.entry_comments.get('1.0', 'end-1c').strip(), self.id.get()),
                                        font=ctk.CTkFont(family="Inter ExtraBold", size=15))
        self.button_create.grid(row=11, column=0, columnspan=3, pady=30)
                                                                


    def set_data_window(self, list_data):
        self.id.set(list_data[0][0] if len(list_data)>0 else "")
        self.name.set(list_data[0][1] if len(list_data)>0 else "")
        self.value.set(list_data[0][2] if len(list_data)>0 else "")
        self.param.set(list_data[0][3] if len(list_data)>0 else "")
        self.entry_comments.delete("1.0", ctk.END)
        self.entry_comments.insert("1.0", list_data[0][5] if len(list_data)>0 else "")


        
        
class ToplevelWindowI(ctk.CTkToplevel):
    
    def __init__(self, parent):
        super().__init__(parent)

        self.withdraw()
        self.configure(fg_color="#333333")

        self.geometry("400x500")
        self.resizable(False, False)
        self.transient(parent)
        self.lift()

        self.name = StringVar()

        self.center_top_frame()
        self.center_bottom_frame()
        self.set_table()
        self.data_base_list(self.table_output, self.row_selector)
        self.after(470, self.deiconify)
        

    def center_top_frame(self):
        
        self.frame_center_top = ctk.CTkScrollableFrame(self, fg_color=ctk.ThemeManager.theme["CTkFrame"]["fg_color"],
                                            bg_color=ctk.ThemeManager.theme["CTkFrame"]["fg_color"],
                                            height=100)

        self.frame_center_top.pack(fill='both', expand= False, padx=5, pady=5, side="top")

       
    def center_bottom_frame(self):
        
        self.frame_bottom_frame = ctk.CTkFrame(self)

        self.frame_bottom_frame.pack(fill='both', expand= True, padx=5, pady=5, side="bottom")

        for i in range(1):
             self.frame_bottom_frame.grid_columnconfigure(i, weight=1)
        for j in range(5):
            self.frame_bottom_frame.grid_rowconfigure(j, weight=1)

        self.button_connection = ctk.CTkButton(self.frame_bottom_frame, text= "Connect",command=lambda:self.create_bbdd_connection(self.row_selector.get(), "", "connect"),
                                        font=ctk.CTkFont(family="Inter ExtraBold", size=15), width=100)
        self.button_connection.grid(row=5, column=0, pady=(10, 15), padx=30, sticky = "e")

        self.button_create_bbdd = ctk.CTkButton(self.frame_bottom_frame, text= "Create",command=lambda:self.create_bbdd_connection(self.row_selector.get(), self.name.get(), "create"),
                                        font=ctk.CTkFont(family="Inter ExtraBold", size=15), width=100)
        self.button_create_bbdd.grid(row=1, column=0, pady=5, padx=30, sticky = "e")

        self.create_database = ctk.CTkLabel(self.frame_bottom_frame, text="Create a new database", font = ("Inter ExtraBold", 20), fg_color="transparent")
        self.create_database.grid(row=0, column=0, pady=10, padx=30, sticky = "w")

        self.entry_new_bbdd = ctk.CTkEntry(self.frame_bottom_frame, textvariable=self.name)
        self.entry_new_bbdd.grid(row=1, column = 0, pady=5, padx= 30, sticky = "w")
        self.name.trace_add('write', lambda *args: self.name.set(self.name.get()[:10]) if len(self.name.get()) > 10 else None)

        self.button_delete_bbdd = ctk.CTkButton(self.frame_bottom_frame, text= "Delete",command=lambda:self.delete_data_base(self.row_selector.get()),
                                        font=ctk.CTkFont(family="Inter ExtraBold", size=15), width=100)
        self.button_delete_bbdd.grid(row=5, column=0, pady=(10, 15), padx=30, sticky = "w")
        

    def set_table(self):

        self.list_table=[["DataBase", "Modification Date"]]

        self.table_output = CTkTable(self.frame_center_top, column=2, values=self.list_table, anchor="center",
                                    font=ctk.CTkFont(family="Inter", size=14), text_color="#C0C0C0")
        self.table_output.pack(fill="both", expand=True)
        self.row_selector = CTkTableRowSelector(self.table_output, can_select_headers=False, max_selection=True)
       

    #Create connection
    def create_bbdd_connection(self, row_selector_bbdd, name, event):

        if row_selector_bbdd and event == "connect":
            self.name_bbdd = row_selector_bbdd[0][0].split(".", 1)[0]
            self.connection_bbdd = app_data_base.Connect_BBDD()
            self.connection_bbdd.create_connection(self.name_bbdd)
            self.data_base_list(self.table_output, self.row_selector)

        elif name != "" and event == "create":
            self.connection_bbdd = app_data_base.Connect_BBDD()
            self.name_db = (name+".db")

            for i in self.connection_bbdd.data_bases_list("App_Data/"):

                if self.name_db in i:
                    #print(i)
                    CTkMessagebox(title='Database Warning', message="Database already exist.",
                            icon="warning", option_1="Ok")
                    return

            else:
                self.connection_bbdd.create_connection(name)
                self.data_base_list(self.table_output, self.row_selector)

        elif name ==  ""  and event == "create":
            CTkMessagebox(title='Database Warning', message="Please write a database name.",
                          icon="warning", option_1="Ok")
            return

        else:
            CTkMessagebox(title='Database Warning', message="Please select a row.",
                          icon="warning", option_1="Ok")
            return
        


    def data_base_list(self, table_output, row_selector_bbdd):

        self.path = "App_Data/"
        self.get_db_list = app_data_base.Connect_BBDD()
        self.output_get_data = self.get_db_list.data_bases_list(self.path)

        try:
            row_selector_bbdd.clear_selection()
        except Exception as e:
            pass
        # delete last table
        rows = len(table_output.get())
        for j in reversed(range(1, rows)):
            try:
                table_output.delete_row(j)
            except Exception as e:
                print(f"Warning deleting row {j}: {e}")
         #set new data
        if self.output_get_data:
            for row in self.output_get_data:
                table_output.add_row(row)
        else:
            CTkMessagebox(title="Info", message="No data available.", icon="info")



    def delete_data_base(self, row_selector_bbdd):

        self.get_db_status = app_data_base.Connect_BBDD()

        if row_selector_bbdd and self.get_db_status.db_selected_status("App_Data/"+row_selector_bbdd[0][0]):

            CTkMessagebox(title="Info", message=f"Please make sure to close the database before deleting it.", icon="info")
            return

        if row_selector_bbdd:

            self.name_bbdd_delete = "App_Data/"+row_selector_bbdd[0][0]

            msg = CTkMessagebox(title="Delete database", message=f"¿Do you want to delete the {row_selector_bbdd[0][0]} database?",
                                icon="question", option_1="Cancel", option_2="No", option_3="Yes")
            response = msg.get()

            if response == "Yes":                
                print(self.name_bbdd_delete)
                self.delete_bbdd = app_data_base.Connect_BBDD()
                self.delete_bbdd.delete_data_base(self.name_bbdd_delete)
                self.data_base_list(self.table_output, self.row_selector)
            else:
                return
            
        else:
            CTkMessagebox(title='Database Warning', message="Please select a row.",
                          icon="warning", option_1="Ok")
            return



class CTkDatePicker(ctk.CTkToplevel):

    def __init__(self, master, set_date, stock, picked_date = None, **kwargs):
        super().__init__(master)

        #WINDOW
        self.configure(fg_color="#333333")
        self.geometry("200x200")
        self.resizable(False, False)
        self.transient(master)
        self.lift()
        self.overrideredirect(True)
        self.variable_date = set_date
        self.variable_stock = stock
        self.pick_date = ""
        self.picked_date = picked_date
        

        #CALENDAR WIDGET
        self.attach = master

        #CALENDAR FRAME
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(fill="both", expand=True)

        self.calendar = ctkdlib.CTkCalendar(self.frame, command=self._pass, **kwargs)
        self.calendar.pack(expand=True, fill="both")

        #HIDE
        self.withdraw()

        #INIT VALUE
        date = self.calendar.current_date()


        #BINDINGS
        if hasattr(self.attach, "_canvas"):
            self.attach._canvas.tag_bind("right_parts", "<Button-1>", lambda e: self.toggle(self.height_for_right, self.width_for_right))
            self.attach._canvas.tag_bind("dropdown_arrow", "<Button-1>", lambda e: self.toggle(self.height_for_arrow, self.width_for_arrow))

        #Close when move to principal window
        self.attach.bind("<Configure>", lambda e: self._auto_close(), add="+")
        self.attach.winfo_toplevel().bind("<Configure>", lambda e: self._auto_close(), add="+")
    
        
    def toggle(self, height, width, entry_variable, stock, set_date, current_last_date, picked_date):
        self.attach = entry_variable
        self.variable_date = set_date
        self.variable_stock = stock
        self.picked_date = picked_date
        self.current_last_date = current_last_date

        if self.attach.cget("state") == "disabled":
            return

        if self.winfo_ismapped():   #show → hide
            self.withdraw()
        else:                        #hide → show
            self.place_dropdown(height, width)
            self.deiconify()
            self.lift()



    def _auto_close(self):
        
        if self.winfo_ismapped():
            self.withdraw()



    def _pass(self, date):
        
        self.pick_date = (f"{date[0]}-{date[1]}-{date[2]}")
        self.withdraw()
        
        for key, value in self.picked_date.items():

            if value == "":
                st.data_historical(self.variable_stock, self.pick_date, self.variable_date)
                self.current_last_date.set(self.pick_date)
            elif self.date_verify_variation():
                st.data_historical(self.variable_stock, self.pick_date, self.variable_date)
                self.current_last_date.set(self.pick_date)



    def date_verify_variation(self):

        for key, value in self.picked_date.items():
            self.convert_picked_date = datetime.strptime(value, "%d-%m-%Y")
            self.convert_pick_date = datetime.strptime(self.pick_date, "%d-%m-%Y")
            if key == 'last' and self.convert_picked_date > self.convert_pick_date:
                CTkMessagebox(title="Info", message="The date of the initial price (last price) must be earlier than the date of the final price.", icon="info")
                return False
            elif key == 'current' and self.convert_picked_date < self.convert_pick_date:
                CTkMessagebox(title="Info", message="The date of the initial price (last price) must be earlier than the date of the final price.", icon="info")
                return False
            else:
                return True



    def place_dropdown(self, height, width):

        widget_x = self.attach.winfo_rootx()
        widget_y = self.attach.winfo_rooty()
    
        x = widget_x + width
        y = widget_y + height
            
        self.geometry(f"200x200+{x}+{y}")

    
class ToplevelWindowII(ctk.CTkToplevel):
    
    def __init__(self, parent, data_instance):
        super().__init__(parent)

        self.withdraw()
        self.configure(fg_color="#333333")

        self.geometry("400x500")
        self.resizable(False, False)
        self.transient(parent)
        self.lift()


        self.check_vars = {}
        self.ticker_list = []
        self.selected_tickers = []

        self.center_top_frame()
        self.center_bottom_frame(data_instance)
        
        self.after(470, self.deiconify)
        

    def center_top_frame(self):
        
        self.frame_center_top = ctk.CTkScrollableFrame(self, fg_color=ctk.ThemeManager.theme["CTkFrame"]["fg_color"],
                                            bg_color=ctk.ThemeManager.theme["CTkFrame"]["fg_color"],
                                            height=300)

        self.frame_center_top.pack(fill='both', expand= False, padx=5, pady=5, side="top")


    def center_bottom_frame(self, data_instance):
        
        self.frame_bottom_frame = ctk.CTkFrame(self)

        self.frame_bottom_frame.pack(fill='both', expand= True, padx=5, pady=5, side="bottom")

        for i in range(1):
             self.frame_bottom_frame.grid_columnconfigure(i, weight=1)
        for j in range(4):
            self.frame_bottom_frame.grid_rowconfigure(j, weight=1)

        self.button_create_bbdd = ctk.CTkButton(self.frame_bottom_frame, text= "Graph",command=lambda:data_instance.variation_ratio(self.selected_tickers),
                                        font=ctk.CTkFont(family="Inter ExtraBold", size=15), width=100)
        self.button_create_bbdd.grid(row=1, column=0, pady=5, padx=30, sticky = "w")

        self.create_database = ctk.CTkLabel(self.frame_bottom_frame, text="Create a new graph", font = ("Inter ExtraBold", 20), fg_color="transparent")
        self.create_database.grid(row=0, column=0, pady=10, padx=30, sticky = "w")


    
    def tickers_option(self):
        
        get_tickers = app_data_base.Connect_BBDD()
        for i in get_tickers.get_column():
            ticker_variable = ctk.StringVar(value="off")
            ticker = i
            self.check_vars[ticker] = ticker_variable  
                     
            self.checkbox = ctk.CTkCheckBox(self.frame_center_top, text= ticker[0], command=lambda t = ticker: self.checkbox_event(t),
                                        variable= ticker_variable, onvalue="on", offvalue="off")
            self.checkbox.pack(fill="both", expand=True)
            
            

    def checkbox_event(self, ticker):
        variable = self.check_vars[ticker].get()
        if variable == 'on':
            self.selected_tickers.append(ticker)
        elif variable == 'off' and ticker in self.selected_tickers:
            self.selected_tickers.remove(ticker)

        return self.selected_tickers

