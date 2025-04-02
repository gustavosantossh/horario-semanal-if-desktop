from tkinter import *

root = Tk()

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
        loginFrame = Frame(root, bd=4)
        
        loginFrame.place(relx=0.5, rely=0.5, anchor="center" , relheight=0.5, relwidth=0.4)
        
        # ---------------------------
        
        loginTextLabel = Label(loginFrame, text="Email").place(relx=0.4, rely=0.2, anchor="e")
        
        loginInputEmail = Entry(loginFrame, ).place(relx=0.5, rely=0.3, anchor="center")
        
        #  ----------------------------
        
        loginTextLabelSenha = Label(loginFrame, text="Senha").place(relx=0.4, rely=0.5, anchor="e")
        
        loginInputSenha = Entry(loginFrame, ).place(relx=0.5, rely=0.6, anchor="center")
        
App()