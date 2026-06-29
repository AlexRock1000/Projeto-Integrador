from candidato.cadastra_candidato import cadastrar_candidato
from candidato.mostrar_candidato import listar_candidatos, mostrar_candidato_por_codigo

def menu_candidato():
    print("""
    -------------------------
          MENU CANDIDATO
    -------------------------
    1 - CADASTRAR NOVO CANDIDATO
    2 - MOSTRAR CANDIDATOS
    3 - PROCURAR CANDIDATO POR CÓDIGO
    4 - MOSTRAR VAGAS
    5 - MOSTRAR CURSOS
    6 - VOLTAR PARA O MENU PRINCIPAL 
    0 - SAIR
    -------------------------
    """)

def opçoes_menu_candidato():
    while True:
        menu_candidato()
        try:
            opçao = input("Escolha uma opção: ")
            if opçao == "0":
                print("Saindo...")
                exit()
            elif opçao == "1": cadastrar_candidato()
            elif opçao == "2": mostrar_candidatos()
            elif opçao == "3": mostrar_candidato()
            elif opçao == "4": 
                from vagas.menu_vagas_candidato import opçoes_menu_vagas
                opçoes_menu_vagas()
            elif opçao == "5":
                from cursos.menu_curso_candidato import opçoes_menu_cursos
                opçoes_menu_cursos()
            elif opçao == "6": return
            else: 
                print("Opção inválida.")

        except ValueError:
            print("Erro: Digita direito abestado!")

def mostrar_candidatos():
    candidatos = listar_candidatos()
    if not candidatos:
        print("\nNenhum candidato cadastrado.")
        return

    for candidato in candidatos:
        candidato.mostrar()

def mostrar_candidato():
    try:
        codigo = int(input("Qual o código do candidato: "))
        candidato = mostrar_candidato_por_codigo(codigo)
        if candidato:
            candidato.mostrar()
        else:
            print("\nCandidato não encontrado.")

    except ValueError:
        print("Erro: Insira um código válido.")
