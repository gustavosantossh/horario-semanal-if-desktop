from tkinter import *
from src.assets.colors import *
from database.SqliteConnection import SqliteConnection
from src.Models.Horario import Horario

db = SqliteConnection()
newHorario = Horario()

class AdicionarHorario():

    def __init__(self, root):

        self.root = root
        self.build()

    def build(self):
        homeFrame = Frame(self.root, background=MAIN_COLOR,
                          width=700)
        homeFrame.pack(expand=False, fill="y", padx=200, pady=5)
        homeFrame.pack_propagate(True)
        
        # TURMA
        labelTurma = Label(homeFrame, text="Turma: ", font=(
            "Arial Bold", 14), fg="white", bg=MAIN_COLOR, pady=3)
        labelTurma.pack(anchor="w")
        turmaEntry = Entry(homeFrame, width=200, font=("Arial Bold", 14))
        turmaEntry.pack(fill="x", pady=5, ipady=2)
        
        # CURSO
        labelCurso = Label(homeFrame, text="Curso: ", font=(
            "Arial Bold", 14), fg="white", bg=MAIN_COLOR, pady=3)
        labelCurso.pack(anchor="w")
        cursoEntry = Entry(homeFrame, width=200, font=("Arial Bold", 14))
        cursoEntry.pack(fill="x", pady=5, ipady=2)
        
        # DISCIPLINA
        labelDisciplina = Label(homeFrame, text="Disciplina: ", font=(
            "Arial Bold", 14), fg="white", bg=MAIN_COLOR, pady=3)
        labelDisciplina.pack(anchor="w")
        disciplinaEntry = Entry(homeFrame, width=200, font=("Arial Bold", 14))
        disciplinaEntry.pack(fill="x", pady=5, ipady=2)
        
        # DIA DA SEMANA
        labelDiaSemana = Label(homeFrame, text="Dia da semana: ", font=(
            "Arial Bold", 14), fg="white", bg=MAIN_COLOR, pady=3)
        labelDiaSemana.pack(anchor="w")
        diaSemanaEntry = Entry(homeFrame, width=200, font=("Arial Bold", 14))
        diaSemanaEntry.pack(pady=5, ipady=2)
        
        # HORARIO DA AULA
        labelHorarioAula = Label(homeFrame, text="Horario da aula: ", font=(
            "Arial Bold", 14), fg="white", bg=MAIN_COLOR, pady=3)
        labelHorarioAula.pack(anchor="w")
        horarioAulaEntry = Entry(homeFrame, width=200, font=("Arial Bold", 14))
        horarioAulaEntry.pack(pady=5, ipady=2)
        
        # SALA
        labelSala = Label(homeFrame, text="Sala: ", font=(
            "Arial Bold", 14), fg="white", bg=MAIN_COLOR, pady=3)
        labelSala.pack(anchor="w")
        salaEntry = Entry(homeFrame, width=200, font=("Arial Bold", 14))
        salaEntry.pack(pady=5, ipady=2)
        
        # PROFESSOR
        labelProfessor = Label(homeFrame, text="Professor (a): ", font=(
            "Arial Bold", 14), fg="white", bg=MAIN_COLOR, pady=3)
        labelProfessor.pack(anchor="w")
        professorEntry = Entry(homeFrame, width=200, font=("Arial Bold", 14))
        professorEntry.pack(pady=5, ipady=2)
        
        messageBox = Label(homeFrame, text="", font=(
            "Arial Bold", 14), fg="red", bg=MAIN_COLOR, pady=2)
        messageBox.pack(anchor="center", fill="x")

        addButton = Button(homeFrame, text="Adicionar Horario", font=(
            "Arial Bold", 14), fg="white", background="green", command=lambda: store())
        addButton.pack(fill="x", pady=20)
        
        backButton = Button(homeFrame, text="VOLTAR", font=(
            "Arial Bold", 14), fg="white", background="black", command=lambda: back())
        backButton.pack(fill="x")
        
        def back():
            from src.windows.home import Home
            for widget in self.root.winfo_children():
                widget.destroy()
            Home(self.root) 
            
        
        def store():
            turma = turmaEntry.get()
            curso = cursoEntry.get()
            disciplina = disciplinaEntry.get()
            diaSemana = diaSemanaEntry.get()
            horarioAula = horarioAulaEntry.get()
            sala = salaEntry.get()
            professor = professorEntry.get()
            
            if not all([turma, curso, disciplina, diaSemana, horarioAula, sala, professor]):
                messageBox.config(text="Preencha todos os dados do formulario!")
            else:
                messageBox.config(text=" ")
                try:
                    response = newHorario.create(turma, curso, disciplina, diaSemana, horarioAula, sala, professor)
                    
                    if response:
                        from src.windows.home import Home
                        for widget in self.root.winfo_children():
                            widget.destroy()
                        Home(self.root)                       
                except:
                    return False

                
