import sqlite3


class User:
    def __init__(self):
        self.conn = sqlite3.connect("database/horario_semanal_if.db")
        
        self.cursor = self.conn.cursor()
      
    def searchHorario(self, turma='', curso=''):
        query = f"SELECT * FROM horarios WHERE turma LIKE '%{turma}%' OR curso LIKE '%{curso}%'"
        
    def create(self, turma: str, curso: str, disciplina: str, dia_semana: str, horario_aula: str, sala: str, professor: str):
        query = f"INSERT INTO horarios (nome_da_turma, curso, disciplina, dia_da_semana, horario_da_aula, sala, professor) VALUES (?, ?, ?, ?, ?, ?, ?)"