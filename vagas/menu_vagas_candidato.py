from vagas.mostrar_vagas import listar_vagas, mostrar_vaga_por_codigo, minhas_vagas

def menu_vagas_candidato():
    print("""
    -------------------------
          MENU VAGAS
    -------------------------
    1 - MOSTRAR TODAS AS VAGAS
    2 - PROCURAR VAGA POR CÓDIGO
    3 - SE CANDIDATAR A UMA VAGA
    4 - MINHAS VAGAS
    5 - VOLTAR PARA O MENU ANTERIOR
    0 - SAIR
    -------------------------
    """)

def opçoes_menu_vagas(id_candidato_logado):
    while True:
        menu_vagas_candidato()
        try:
            opçao = input("Escolha uma opção: ")
            if opçao == "0":
                print("Saindo...")
                exit()
            elif opçao == "1": mostrar_vagas()
            elif opçao == "2": mostrar_vaga()
            elif opçao == "3":
                from vagas.cadastrar_vagas import inscriçao_vaga
                inscriçao_vaga(id_candidato_logado)
            elif opçao == "4": minhas_vagas(id_candidato_logado)
            elif opçao == "5": return
            else: 
                print("Opção inválida.")

        except ValueError:
            print("Erro: Digita direito abestado!")

def mostrar_vagas():
    vagas = listar_vagas()
    if not vagas:
        print("\nNenhuma vaga cadastrada.")
        return

    for vaga in vagas:
        vaga.mostrar()

def mostrar_vaga():
    try:
        codigo = int(input("Qual o código da vaga: "))
        vaga = mostrar_vaga_por_codigo(codigo)
        if vaga:
            vaga.mostrar()
        else:
            print("\nVaga não encontrada.")

    except ValueError:
        print("Erro: Insira um código válido.")