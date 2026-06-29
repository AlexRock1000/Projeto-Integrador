from conexao import conectar

def realizar_login_empresa():
    print("""
    -------------------------
          LOGIN EMPRESA
    -------------------------
    """)
    cnpj = input("Digite o CNPJ da empresa: ").strip()
    senha = input("Digite a senha: ").strip()

    conexao = conectar()
    cursor = conexao.cursor()

    # Busca a empresa com o cnpj e senha correspondentes
    sql = "SELECT id_empresa, nome_fantasia FROM empresa WHERE cnpj = %s AND senha = %s"
    cursor.execute(sql, (cnpj, senha))
    empresa = cursor.fetchone()

    cursor.close()
    conexao.close()

    if empresa:
        print(f"\nLogin realizado com sucesso! Bem-vindo(a), {empresa[1]}.")
        return empresa[0] # Retorna o ID para usarmos nas vagas
    else:
        print("\nErro: CNPJ ou senha incorretos.")
        return None

def cadastrar_vaga(id_empresa_logada):
    from vagas.menu_vaga_empresa import opçoes_menu_vagas_empresa
    opçoes_menu_vagas_empresa(id_empresa_logada)