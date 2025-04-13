from tkinter import *
from src.assets.colors import *
from src.windows.home import Home
from database.SqliteConnection import SqliteConnection

root = Tk()

class App:
    def __init__(self):
        self.window()

    def window(self):
        self.config()
        self.windowLogin()
        root.mainloop()

    def config(self):
        root.config(background=MAIN_COLOR)
        root.minsize(800, 500)
        root.title("Horário Semanal")

    def windowLogin(self):
        self.loginScreen = Home(root)

App()