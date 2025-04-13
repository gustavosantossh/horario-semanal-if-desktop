from tkinter import *
from src.assets.colors import *
from database.SqliteConnection import SqliteConnection
from src.Models.Horario import Horario
from src.windows.adicionarHorario import AdicionarHorario

db = SqliteConnection()

# Horario = Horario().searchAll()


class Home():

    def __init__(self, root):
        # global Horario
        self.root = root
        self.iHorario = Horario()
        self.response = self.iHorario.searchAll()
        self.build()

    def build(self):
        homeFrame = Frame(self.root, background=MAIN_COLOR, width=700, height=200)
        homeFrame.pack(expand=True)
        homeFrame.pack_propagate(False)
        
        labelTitle = Label(homeFrame, text="Horario Semanal", font=(
            "Arial Bold", 24), fg="white", bg=MAIN_COLOR, pady=2)
        labelTitle.pack(anchor="center")

        serachEntry = Entry(homeFrame, width=200, font=("Arial Bold", 14))
        serachEntry.pack(fill="x", pady=10, ipady=5)

        searchButton = Button(homeFrame, text="Buscar", font=(
            "Arial Bold", 14), fg="white", background="green", command=lambda: self.searchData(data=serachEntry.get(), frame=tableFrame))
        searchButton.pack(fill="x", pady=10)
        
        addButton = Button(homeFrame, text="Adicionar Horario", font=(
            "Arial Bold", 14), fg="white", background="orange", command=lambda: self.changeWindow() )
        addButton.pack(fill="x")

        tableFrame = Frame(self.root, background=MAIN_COLOR, width=700, height=200)
        tableFrame.pack(expand=True, fill="both", anchor="center", padx=250 )
        tableFrame.pack_propagate(False)
        
        self.atualizarTabela(tableFrame)
        
    def changeWindow(self):
        for widget in self.root.winfo_children():
            widget.destroy()
            
        AdicionarHorario(self.root)

    def searchData(self, data, frame):

        if data is not None:
            self.response = self.iHorario.searchHorario(data)
            
        else:
            print("Nenhum dado encontrado")
            
        self.atualizarTabela(frame)
        
    def atualizarTabela(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()
        # Criar os elementos da tabela com grid()
        if self.response is not None:
            for i, linha in enumerate(self.response):
                for j, valor in enumerate(linha):
                    
                    label = Label(frame, text=valor, borderwidth=1,
                                relief="solid", padx=10, pady=5, justify="center")
                    label.grid(row=i, column=j, sticky="nsew")
                    
                deleteButton = Button(frame, text="Apagar", font=("Arial Bold", 14), fg="white", background="red", command=lambda id=linha[0]: self.deletarHorario(id, frame))
                
                deleteButton.grid(row=i, column=len(linha), sticky="nsew")
        
        else:
            Label(frame, text="Nenhum dado encontrado").pack(anchor="center")
        
    def deletarHorario(self, registro_id, frame):
        try:
            self.iHorario.delete(registro_id)
            self.atualizarTabela(frame)
            return 
        except Exception as e:
            print(e)
                
                    
                    

