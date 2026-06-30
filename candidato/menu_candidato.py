from candidato.cadastra_candidato import cadastrar_candidato
from candidato.mostrar_candidato import listar_candidatos, mostrar_candidato_por_codigo

def menu_candidato():
    print("""
    -------------------------
          MENU CANDIDATO
    -------------------------
    1 - CADASTRAR NOVO CANDIDATO
    2 - ÁREA VAGAS
    3 - ÁREA CURSOS
    0 - VOLTAR PARA O MENU PRINCIPAL 
    00 - SAIR
    -------------------------
    """)

def opçoes_menu_candidato():
    while True:
        menu_candidato()
        try:
            opçao = input("Escolha uma opção: ")
            if opçao == "00":
                print("Saindo...")
                exit()
            elif opçao == "1": cadastrar_candidato()
            elif opçao == "2": 
                from candidato.autenticacao import realizar_login_candidato #Chamando a função de Login
                sucesso_login = realizar_login_candidato()
                if sucesso_login:
                    from vagas.menu_vagas_candidato import opçoes_menu_vagas
                    opçoes_menu_vagas(sucesso_login)

                else: print("Precisa está logado para se candidatar a uma vaga!")
            elif opçao == "3":
                from candidato.autenticacao import realizar_login_candidato #Chamando a função de Login
                sucesso_login = realizar_login_candidato()
                if sucesso_login:
                    from cursos.menu_curso_candidato import opçoes_menu_cursos
                    opçoes_menu_cursos(sucesso_login)

                else: print("Precisa está logado para se candidatar a uma vaga!")
            elif opçao == "0": return
            else: 
                print("Opção inválida.")

        except ValueError:
            print("Erro: Digita direito abestado!")
