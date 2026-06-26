from candidatos.menu_candidato import menu_candidato

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

while True:
    menu()
    try:
        opçao = input("Escolha uma opção: ")
        if opçao == "0":
            break
        elif opçao == "1": menu_administrador()
        elif opçao == "2": menu_candidato()
        elif opçao == "3": menu_empresa()
        elif opçao == "4": menu_escola()
        else: print("Opção inválida.")

    except ValueError:
        print("Erro: Digita direito abestado!")