import sqlite3


class User:
    def __init__(self):
        self.conn = sqlite3.connect("database/horario_semanal_if.db")
        
        self.cursor = self.conn.cursor()
      
    def searchHorario(self, ):
        query = f"SELECT * FROM horarios WHERE turma LIKE '%a%' OR curso LIKE '%%'"