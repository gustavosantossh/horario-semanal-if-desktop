from tkinter import *
from src.assets.colors import *
from src.windows.login import Login
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
        self.loginScreen = Login(root)
              
        
App()








# import tkinter as tk

# # Criar a janela principal
# janela = tk.Tk()
# janela.title("Tabela de Dados")

# # Dados da tabela (primeira linha são os títulos das colunas)
# dados = [
#     ["Nome", "Idade", "Cidade"],
#     ["Ana", 25, "São Paulo"],
#     ["Bruno", 30, "Rio de Janeiro"],
#     ["Carlos", 28, "Belo Horizonte"],
#     ["Daniela", 35, "Curitiba"]
# ]

# # Criar os elementos da tabela com grid()
# for i, linha in enumerate(dados):
#     for j, valor in enumerate(linha):
#         label = tk.Label(janela, text=valor, borderwidth=1, relief="solid", padx=10, pady=5)
#         label.grid(row=i, column=j, sticky="nsew")

# # Iniciar o loop da janela
# janela.mainloop()
