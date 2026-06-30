from instituiçao_ensino.cadastro_instituicao import cadastrar_instituicaoEnsino
from instituiçao_ensino.mostrar_instituicao import listar_instituicaoEnsino, mostrar_instituicao_por_codigo

def menu_instituicao():
    print("""
    -------------------------
    MENU INSTITUIÇÃO DE ENSINO
    -------------------------
    1 - CADASTRAR NOVA INSTITUIÇÃO DE ENSINO
    2 - CADASTRAR CURSO
    3 - VOLTAR PARA O MENU PRINCIPAL
    0 - SAIR
    -------------------------
    """)

def opçoes_menu_instituicao():
    while True:
        menu_instituicao()
        try:
            opçao = input("Escolha uma opção: ")
            if opçao == "0":
                print("Saindo...")
                exit()
            elif opçao == "1": cadastrar_instituicaoEnsino()
            elif opçao == "2": 
                from instituiçao_ensino.autenticacao import realizar_login_instituicao, cadastrar_curso
                sucesso_login = realizar_login_instituicao()
                if sucesso_login:
                    cadastrar_curso(sucesso_login)
                    
                else: print("Precisa está logado para cadastrar uma vaga!")
            elif opçao == "3": return
            else: print("Opção inválida.")

        except ValueError:
            print("Erro: Digita direito abestado!")