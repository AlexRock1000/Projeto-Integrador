from empresas.mostrar_empresa import listar_empresas, mostrar_empresa_por_codigo
from empresas.cadastrar_empresa import cadastrar_empresa

def menu_empresa():
    print("""
    -------------------------
          MENU EMPRESA
    -------------------------
    1 - CADASTRAR NOVA EMPRESA
    2 - CADASTRAR UMA VAGA
    3 - VOLTAR PARA O MENU PRINCIPAL
    0 - SAIR
          -------------------------
    """)

def opçoes_menu_empresa():
    while True:
        menu_empresa()
        try:
            opçao = input("Escolha uma opção: ")
            if opçao == "0":
                print("Saindo...")
                exit()
            elif opçao == "1": cadastrar_empresa()
            elif opçao == "2": 
                from empresas.autenticacao import realizar_login_empresa, cadastrar_vaga
                sucesso_login = realizar_login_empresa()
                if sucesso_login:
                    cadastrar_vaga(sucesso_login)
                    
                else: print("Precisa está logado para cadastrar uma vaga!")
            elif opçao == "3": return
            else: print("Opção inválida.")

        except ValueError:
            print("Erro: Digita direito abestado!")