from administrador.administrador import Administradores
from administrador.cadastro_administrador import cadastrar_administrador
from administrador.mostrar_administrador import listar_administradores, mostrar_administrador_por_codigo

def menu_administrador():
    print("""
    -------------------------
          MENU ADMINISTRADOR
    -------------------------
    1 - CADASTRAR NOVO ADMINISTRADOR
    2 - MOSTRAR ADMINISTRADORES
    3 - PROCURAR ADMINISTRADOR POR CÓDIGO
    4 - VOLTAR PARA O MENU PRINCIPAL
    0 - SAIR
    -------------------------
    """)

def opçoes_menu_administrador():
    while True:
        menu_administrador()
        try:
            opçao = input("Escolha uma opção: ")
            if opçao == "0":
                print("Saindo...")
                exit()
            elif opçao == "1": cadastrar_administrador()
            elif opçao == "2": mostrar_administradores()
            elif opçao == "3": mostrar_administrador()
            elif opçao == "4": return
            else: print("Opção inválida.")

        except ValueError:
            print("Erro: Digita direito abestado!")

def mostrar_administradores():
    administradores = listar_administradores()
    if not administradores:
        print("Nenhum administrador cadastrado.")
        return

    for administrador in administradores:
        administrador.mostrar()

def mostrar_administrador():
    try:
        codigo = int(input("Qual o código do administrador: "))
        administrador = mostrar_administrador_por_codigo(codigo)
        if administrador:
            administrador.mostrar_por_codigo()
        else:
            print("Administrador não encontrado.")

    except ValueError:
        print("Erro: Insira um código válido.")