from empresas.empresas import Empresas
from empresas.mostrar_empresa import listar_empresas, mostrar_empresa_por_codigo
from empresas.cadastrar_empresa import cadastrar_empresa

def menu_empresa():
    print("""
    -------------------------
          MENU EMPRESA
    -------------------------
    1 - CADASTRAR NOVA EMPRESA
    2 - MOSTRAR EMPRESAS
    3 - PROCURAR EMPRESA POR CÓDIGO
    4 - VOLTAR PARA O MENU PRINCIPAL
    0 - SAIR
    -------------------------
    """)

def opçoes_menu_empresa():
    while True:
        menu_empresa()
        try:
            opçao = input("Escolha uma opção: ")
            if opçao == "0":
                print("Saindo...")
                exit()
            elif opçao == "1": cadastrar_empresa()
            elif opçao == "2": mostrar_empresas()
            elif opçao == "3": mostrar_empresa()
            elif opçao == "4": return
            else: print("Opção inválida.")

        except ValueError:
            print("Erro: Digita direito abestado!")

def mostrar_empresas():
    empresas = listar_empresas()
    if not empresas:
        print("Nenhuma empresa cadastrada.")
        return

    for empresa in empresas:
        empresa.mostrar()

def mostrar_empresa():
    try:
        codigo = int(input("Qual o código da empresa: "))
        empresa = mostrar_empresa_por_codigo(codigo)
        if empresa:
            empresa.mostrar_por_codigo()
        else:
            print("Empresa não encontrada.")

    except ValueError:
        print("Erro: Insira um código válido.")