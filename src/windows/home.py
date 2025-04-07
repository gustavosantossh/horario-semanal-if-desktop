from tkinter import *
from src.assets.colors import *
from database.SqliteConnection import SqliteConnection

db = SqliteConnection()

class Home():
    
    def __init__(self, root):
        self.root = root
        self.build()
    
    def build(self):
        homeFrame = Frame(self.root, background=MAIN_COLOR, width=600, height=300)
        homeFrame.pack(expand=True)
        homeFrame.pack_propagate(False)

        labelTitle = Label(homeFrame, text="Home", font=(
            "Arial Bold", 24), fg="white", bg=MAIN_COLOR, pady=2)
        labelTitle.pack(anchor="center")