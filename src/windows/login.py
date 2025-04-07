# type: ignore
from tkinter import *
from src.assets.colors import *
from database.SqliteConnection import SqliteConnection
from src.windows.home import Home

db = SqliteConnection()

class Login():
    
    def __init__(self, root):
        self.root = root
        self.build()
    
    def build(self):
        loginFrame = Frame(self.root, background=MAIN_COLOR, width=600, height=300)
        loginFrame.pack(expand=True)
        loginFrame.pack_propagate(False)

        labelTitle = Label(loginFrame, text="Horario Semanal", font=(
            "Arial Bold", 24), fg="white", bg=MAIN_COLOR, pady=2)
        labelTitle.pack(anchor="center")

        labelEmail = Label(loginFrame, text="Email: ", font=(
            "Arial Bold", 14), fg="white", bg=MAIN_COLOR, pady=2).pack(anchor="w")
        entryEmail = Entry(loginFrame, font=("Arial Bold", 12), background="#CCC")
        entryEmail.pack(fill="x", ipady=2)

        labelSenha = Label(loginFrame, text="Senha: ", font=(
            "Arial Bold", 14), fg="white", bg=MAIN_COLOR, pady=2).pack(anchor="w")
        entrySenha = Entry(loginFrame, show="*", font=("Arial Bold", 12))
        entrySenha.pack(fill="x", ipady=2)

        loginButton = Button(loginFrame, text="Login", font=("Arial Bold", 14), fg="white", background="green", command=lambda: self.loginUser(entryEmail.get(), entrySenha.get()))
        loginButton.pack(fill="x", pady=20)

        self.messageBox = Label(loginFrame, text="", font=(
            "Arial Bold", 14), fg="red", bg=MAIN_COLOR, pady=2)
        self.messageBox.pack(anchor="center", fill="x")


    def loginUser(self, email, password):
        if not email or not password:
            self.messageBox.config(text="Email and password are required")
        else:
            self.messageBox.config(text="")
            try:
                login = db.verify_login(email, password)
                
                if login:
                    for widget in self.root.winfo_children():
                        widget.destroy()
                    
                    Home(self.root)
            except:
                pass
                
