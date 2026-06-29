from vagas.cadastrar_vagas import cadastrar_vagas

def menu_vagas_empresa():
    print("""
    -------------------------
            MENU VAGAS
    -------------------------
    1 - CADASTRAR UMA NOVA VAGA
    2 - MOSTRAR VAGAS CADASTRADAS
    3 - VOLTAR PARA O MENU ANTERIOR
    0 - SAIR
    -------------------------
    """)

def opçoes_menu_vagas(id_empresa_logada):
    while True:
        menu_vagas_empresa()
        try:
            opçao = input("Escolha uma opção: ")
            if opçao == "0":
                print("Saindo...")
                exit()
            elif opçao == "1": cadastrar_vagas(id_empresa_logada)
            elif opçao == "2": ...
            elif opçao == "3": return
            else: 
                print("Opção inválida.")

        except ValueError:
            print("Erro: Digita direito abestado!")

def mostrar_vagas_cadastradas():
    vagas = listar_vagas()
    if not vagas:
        print("\nNenhuma vaga cadastrada.")
        return

    for vaga in vagas:
        vaga.mostrar()
