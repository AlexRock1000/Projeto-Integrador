from conexao import conectar

def realizar_login_instituicao():
    print("""
    -------------------------
    LOGIN INSTITUIÇÃO DE ENSINO
    -------------------------
    """)
    cnpj = input("Digite o CNPJ da instituição: ").strip()
    senha = input("Digite a senha: ").strip()

    conexao = conectar()
    cursor = conexao.cursor()

    # Busca a instituição de ensino com o cnpj e senha correspondentes
    sql = "SELECT id_instituicao, nome_instituicao FROM instituicao_ensino WHERE cnpj = %s AND senha = %s"
    cursor.execute(sql, (cnpj, senha))
    instituicao = cursor.fetchone()

    cursor.close()
    conexao.close()

    if instituicao:
        print(f"\nLogin realizado com sucesso! Bem-vindo {instituicao[1]}.")
        return instituicao[0]
    else:
        print("\nErro: CNPJ ou senha incorretos.")
        return None
    
def cadastrar_curso(id_instituicao_logada):
    from cursos.menu_curso_instituicao import opçoes_menu_cursos_instituicao
    opçoes_menu_cursos_instituicao(id_instituicao_logada)
