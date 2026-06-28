from instituiçao_ensino.cadastro_instituicao import cadastrar_instituicaoEnsino
from instituiçao_ensino.mostrar_instituicao import listar_instituicaoEnsino, mostrar_instituicao_por_codigo


def menu_instituicao():
    print("""
    -------------------------
          MENU INSTITUIÇÃO DE ENSINO
    -------------------------
    1 - CADASTRAR NOVA INSTITUIÇÃO DE ENSINO
    2 - MOSTRAR INSTITUIÇÕES DE ENSINO
    3 - PROCURAR INSTITUIÇÃO DE ENSINO POR CÓDIGO
    4 - VOLTAR PARA O MENU PRINCIPAL
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
            elif opçao == "2": mostrar_instituicoes()
            elif opçao == "3": mostrar_instituicao()
            elif opçao == "4": return
            else: print("Opção inválida.")

        except ValueError:
            print("Erro: Digita direito abestado!")

def mostrar_instituicoes():
    instituicoes = listar_instituicaoEnsino()
    if not instituicoes:
        print("Nenhuma instituição de ensino cadastrada.")
        return

    for instituicao in instituicoes:
        instituicao.mostrar()

def mostrar_instituicao():
    try:
        codigo = int(input("Qual o código da instituição de ensino: "))
        instituicao = mostrar_instituicao_por_codigo(codigo)
        if instituicao:
            instituicao.mostrar_por_codigo()
        else:
            print("Instituição de ensino não encontrada.")

    except ValueError:
        print("Erro: Insira um código válido.")