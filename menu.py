from administrador.menu_administrador import opçoes_menu_administrador
from candidato.menu_candidato import opçoes_menu_candidato
from empresas.menu_empresa import opçoes_menu_empresa

def menu():
    print("""
    -------------------------
          MENU PRINCIPAL
    -------------------------
    1 - ÁREA ADMINISTRADOR.
    2 - ÁREA DE CANDIDATO.
    3 - ÁREA EMPRESA.
    4 - ÁREA ESCOLAS.  
    0 - SAIR
    -------------------------
    """)

def opçoes_menu():
    while True:
        menu()
        try:
            opçao = input("Escolha uma opção: ")
            if opçao == "0":
                break
            elif opçao == "1": opçoes_menu_administrador()
            elif opçao == "2": opçoes_menu_candidato()
            elif opçao == "3": opçoes_menu_empresa()
            elif opçao == "4": ...
            else: print("Opção inválida.")

        except ValueError:
            print("Erro: Digita direito abestado!")

opçoes_menu()