from tkinter import *
from teste import MySqlConnection

db = MySqlConnection()
root = Tk()

MAIN_COLOR = "#04030F"

class App:
    def __init__(self):
        self.window()
    
    def window(self):
        self.config()
        self.login()
        root.mainloop()
        
    def config(self):
        root.config(background="#04030F")
        root.minsize(800, 500)
        root.title("Horário Semanal")
        
    def login(self):
        loginFrame = Frame(root, background=MAIN_COLOR, width=600, height=300)
        loginFrame.pack(expand=True)
        loginFrame.pack_propagate(False)
        
        labelEmail = Label(loginFrame, text="Email: ", font=("Arial Bold", 14), fg="white", bg=MAIN_COLOR, pady=2).pack(anchor="w")
        entryEmail = Entry(loginFrame, font=("Arial Bold", 12))
        entryEmail.pack(fill="x", ipady=2) 
        
        labelSenha = Label(loginFrame, text="Senha: ", font=("Arial Bold", 14), fg="white", bg=MAIN_COLOR, pady=2).pack(anchor="w")
        entrySenha = Entry(loginFrame, show="*", font=("Arial Bold", 12))
        entrySenha.pack(fill="x", ipady=2)
        
        loginButton = Button(loginFrame, text="Login", font=("Arial Bold", 14), fg="white", background="green", command=lambda: db.verify_login(entryEmail.get(), entrySenha.get()))
        loginButton.pack(fill="x", pady=20) 
        
        
App()