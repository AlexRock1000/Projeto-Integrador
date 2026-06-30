from conexao import conectar

def realizar_login_candidato():
    print("""
    -------------------------
          LOGIN CANDIDATO
    -------------------------
    """)
    cpf = input("Digite seu CPF: ").strip()
    senha = input("Digite a senha: ").strip()

    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT id_candidato, nome_completo FROM candidato WHERE cpf = %s AND senha = %s"
    cursor.execute(sql, (cpf, senha))
    candidato = cursor.fetchone()

    cursor.close()
    conexao.close()

    if candidato:
        print(f"\nLogin realizado com sucesso! Bem-vindo {candidato[1]}.")
        return candidato[0]

    else: print("\nErro: CPF ou senha incorretos.")

    return None    