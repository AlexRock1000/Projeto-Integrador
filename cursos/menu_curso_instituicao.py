from cursos.cadastrar_cursos import cadastrar_curso

def menu_curso_instituicao():
    print("""
    -------------------------
            MENU CURSOS
    -------------------------
    1 - CADASTRAR UM NOVO CURSO
    2 - MOSTRAR CURSOS CADASTRADOS
    3 - VOLTAR PARA O MENU ANTERIOR
    0 - SAIR
    -------------------------
    """)

def opçoes_menu_cursos_instituicao(id_instituicao_logada):
    while True:
        menu_curso_instituicao()
        try:
            opçao = input("Escolha uma opção: ")
            if opçao == "0":
                print("Saindo...")
                exit()
            elif opçao == "1": cadastrar_curso(id_instituicao_logada)
            elif opçao == "2": ...
            elif opçao == "3": return
            else: 
                print("Opção inválida.")

        except ValueError:
            print("Erro: Digita direito abestado!")

def mostrar_cursos_cadastrados():
    cursos = listar_cursos()
    if not cursos:
        print("\nNenhum curso cadastrado.")
        return

    for curso in cursos:
        curso.mostrar()