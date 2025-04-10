from tkinter import *
from src.assets.colors import *
from database.SqliteConnection import SqliteConnection

db = SqliteConnection()

class Home():
    
    def __init__(self, root):
        self.root = root
        self.build()
    
    def build(self):
        homeFrame = Frame(self.root, background="#ccc", width=700, height=400)
        homeFrame.pack(expand=True)
        homeFrame.pack_propagate(False)

        serachEntry = Entry(homeFrame, width=200)
        serachEntry.pack(fill="x", pady=10)
        
        searchButton = Button(homeFrame, text="Buscar", font=("Arial Bold", 14), fg="white", background="green")
        searchButton.pack(fill="x")