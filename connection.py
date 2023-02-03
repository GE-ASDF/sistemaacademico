import mysql.connector
from mysql.connector import errorcode
import pyautogui as p

class connection:

    def __init__(self):
        try:
            self.db_connection = mysql.connector.connect(host='192.168.1.10', user='prepcurso', password='ke7@ch%', database='preparaadm', port='3307')
            self.db_connection
        except mysql.connector.Error as error:
            if error.errno == errorcode.ER_BAD_DB_ERROR:
                p.alert("Database doesn't exist")
            elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                p.alert("Username or password is wrong")
            else:
                p.alert(error, "Error")

    def selectUser(self, CodigoContrato):
        cursor = self.db_connection.cursor()
        query = "SELECT * FROM loginagendamentoaluno as L, pr_perfilalunos as P WHERE L.CodigoContrato = %s OR P.CodigoContrato = %s"
        cursor.execute(query, (CodigoContrato,))
        return cursor.fetchone()
    
    def closedb(self):
        self.db_connection.close()
