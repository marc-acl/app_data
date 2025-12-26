import sqlite3
from CTkMessagebox import CTkMessagebox
import os
from datetime import datetime
import threading


class Connect_BBDD():

    _instance = None


    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Connect_BBDD, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    

    def __init__(self):

        if self._initialized:
            return
        self.db_name = None
        self.connection = None
        self.cursor = None
        self._initialized = True
        self.lock = threading.Lock()
        


    def connection_status(self):
        if self.connection is None:
            return False
        else:
            return True



    def create_connection(self, name):
        with self.lock:

            if self.connection is None:
                self.connection = sqlite3.connect(f'App_Data/{name}.db', check_same_thread=False)
                self.cursor = self.connection.cursor()
                self.db_name = f'App_Data/{name}.db'
                

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
            else:
                CTkMessagebox(message="To create a new connection or database, close the current one.",
                        icon="warning", option_1="Ok")
                return 


        

    def insert_data(self, list):
        with self.lock:
        
            self.cursor.execute("INSERT INTO DATA VALUES (?, ?, ?, ?, ?, ?)", list)
            self.connection.commit()
            return True
            
        
    

    def read_data(self, search, get_value):

        with self.lock:

            self.new_data_list = []

            if get_value != "":
                query = f"SELECT * FROM DATA WHERE {search} = ?"
                value = (get_value,)

            elif get_value == "":
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

        with self.lock:

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
        with self.lock:
            variation = round((float(param)-float(value))/float(value)*100, 3)
            self.cursor.execute("""
                                UPDATE DATA SET NAME = ?, INITIAL_VALUE = ?, FINAL_VALUE = ?, VARIATION = ?, COMMENTS = ? WHERE ID = ? """
                                ,(name, value, param, variation, comments, id))
            self.connection.commit()
            return True
        


    def delete_data(self, id):
        self.cursor.execute("""DELETE FROM DATA WHERE ID = ?""", (id,))
        self.connection.commit()
        return True
        


    def sort_data(self, value):
        self.sort_list = []
        self.cursor.execute(f"SELECT * FROM DATA ORDER BY {value} DESC")

        self.sort_list = [list(i) for i in self.cursor.fetchall()]
        return self.sort_list
    


    def get_column(self):
        self.output_column = []
        self.cursor.execute('SELECT lower(NAME) AS NAME , avg(VARIATION) FROM DATA GROUP BY lower(NAME)')
        self.output_column = self.cursor.fetchall()
        
        return self.output_column
    


    def get_tickers(self):
        
        self.cursor.execute("SELECT lower(NAME) AS NAME FROM DATA GROUP BY lower(NAME)")

        self.output_tickers = self.cursor.fetchall()
        self.tickers_list = [self.output_tickers[i][0] for i in range(len(self.output_tickers))]
        
        return self.tickers_list
    


    def data_bases_list(self, directory):
        self.output_list = []


        for file in os.listdir(directory):
            self.path = os.path.join(directory, file)

            if os.path.isfile(self.path) and file.endswith((".db", ".sqlite", ".sqlite3")):
                self.date = datetime.fromtimestamp(os.path.getmtime(self.path))
                self.output_list.append((file, self.date))

        return self.output_list
    


    def delete_data_base(self, name):

        if os.path.exists(name):
            os.remove(name)
            name = name.split("/", 1)[1]
            CTkMessagebox(title="Info", message=f"Database {name} has been deleted.", icon="info")
            
        else:
            name = name.split("/", 1)[1]
            CTkMessagebox(title="Info", message=f"Database {name} does not exist.", icon="info")
            return



    def db_selected_status(self, name):
        #print(name, self.db_name)
        if self.db_name == name:
            return True
        else:
            return False
        

    def get_name_db(self):
        if self.db_name is None:
            return ""
        else:
            name = self.db_name.split("/", 1)[1]
            return name
    

    def set_name_db(self, name):
        self.db_name = name
            

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None
            self.db_name = None


        


        

