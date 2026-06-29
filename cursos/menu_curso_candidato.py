from cursos.mostrar_cursos import listar_cursos, mostrar_curso_por_codigo

def menu_cursos():
    print("""
    -------------------------
          MENU CURSOS
    -------------------------
    1 - MOSTRAR TODOS CURSOS
    2 - PROCURAR CURSO POR CÓDIGO
    3 - VOLTAR PARA O MENU ANTERIOR 
    0 - SAIR
    -------------------------
    """)

def opçoes_menu_cursos():
    while True:
        menu_cursos()
        try:
            opçao = input("Escolha uma opção: ")
            if opçao == "0":
                print("Saindo...")
                exit()
            elif opçao == "1": mostrar_cursos()
            elif opçao == "2": mostrar_curso()
            elif opçao == "3": return
            else: 
                print("Opção inválida.")

        except ValueError:
            print("Erro: Digita direito abestado!")

def mostrar_cursos():
    cursos = listar_cursos()
    if not cursos:
        print("\nNenhum curso cadastrado.")
        return

    for curso in cursos:
        curso.mostrar()

def mostrar_curso():
    try:
        codigo = int(input("Qual o código do curso: "))
        curso = mostrar_curso_por_codigo(codigo)
        if curso:
            curso.mostrar()
        else:
            print("\nCusrso não encontrado.")

    except ValueError:
        print("Erro: Insira um código válido.")