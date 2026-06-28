from conexao import conectar
from administrador.administrador import Administradores

def listar_administradores():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT * FROM administrador"
    cursor.execute(sql)

    administradores = []
    for id_administrador, nome_completo, cpf, email, telefone, cargo, nivel_acesso, senha, status_conta, data_cadastro in cursor.fetchall():

        administrador = Administradores(id_administrador=id_administrador, nome_completo=nome_completo, cpf=cpf, email=email, telefone=telefone, cargo=cargo, nivel_acesso=nivel_acesso, senha=senha, status_conta=status_conta, data_cadastro=data_cadastro)
        administradores.append(administrador)

    conexao.close()
    return administradores

def mostrar_administrador_por_codigo(id_administrador):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT * FROM administrador WHERE id_administrador = %s"
    cursor.execute(sql, (id_administrador,))

    resultado = cursor.fetchone()
    conexao.close()

    if resultado:
        id_administrador, nome_completo, cpf, email, telefone, cargo, nivel_acesso, senha, status_conta, data_cadastro = resultado

        return Administradores(id_administrador=id_administrador, nome_completo=nome_completo, cpf=cpf, email=email, telefone=telefone, cargo=cargo, nivel_acesso=nivel_acesso, senha=senha, status_conta=status_conta, data_cadastro=data_cadastro)

    return None