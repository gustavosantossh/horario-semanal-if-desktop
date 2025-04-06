import mysql.connector

class MySqlConnection():
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="horario_semanal_if"
        )
        
        self.cursor = self.conn.cursor()

    def verify_login(self, email: str, senha: str) -> bool:
        cursor = self.cursor
        query = f'SELECT email from user WHERE email = "{email}" AND senha = "{senha}"'
        cursor.execute(query)
        resultado = cursor.fetchone()
        
        cursor.close()
        self.conn.close()
        
        print(resultado)
        
        if resultado:
            print("sucesso")
            return True
        print("error")
        return False

# cursor = conn.cursor()

# command = f'SELECT * FROM horarios'

# cursor.execute(command)

# r = cursor.fetchall()
# print(r)

# cursor.close()
# conn.close()
