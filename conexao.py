import os
import pymysql
from dotenv import load_dotenv

load_dotenv()

def conectar():
    try:
        conexao = pymysql.connect(
            host=os.getenv("DB_HOST", "127.0.0.1"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_DATABASE"),
            connect_timeout=5
        )
        return conexao
    except pymysql.Error as err:
        print(f"Erro ao conectar ao banco: {err}")
        return None

if __name__ == "__main__":
    print("Iniciando teste de conexão...")
    try:
        minha_conexao = conectar()
        if minha_conexao:
            print("Sucesso: Banco de Dados conectou!")
            minha_conexao.close()
        else:
            print("Falha: Não foi possível conectar")
    except Exception as e:
        print(f"Erro ao conectar: {e}")
