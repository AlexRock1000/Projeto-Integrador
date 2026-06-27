import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def conectar():
    try:
        return mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_DATABASE"),
        )
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao banco de dados: {err}")
        raise

try:
    conexao = conectar()
    online = conexao.is_connected()
except Exception:
    online = False
    print("Banco de Dados não conectou.")
else:
    print("Banco de Dados conectou.")