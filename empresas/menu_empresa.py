from empresas.mostrar_empresa import listar_empresas, mostrar_empresa_por_codigo
from empresas.cadastrar_empresa import cadastrar_empresa

def menu_empresa():
    print("""
    -------------------------
          MENU PRINCIPAL
    -------------------------
    1 - CADASTRAR NOVA EMPRESA
    2 - MOSTRAR EMPRESAS
    3 - PROCURAR EMPRESA POR CÓDIGO
    0 - SAIR
    -------------------------
    """)

def mostrar_empresas():
    for empresa in listar_empresas():
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

while True:
    menu_empresa()
    try:
        opçao = input("Escolha uma opção: ")
        if opçao == "0":
            break
        elif opçao == "1": cadastrar_empresa()
        elif opçao == "2": mostrar_empresas()
        elif opçao == "3": mostrar_empresa()
        else: print("Opção inválida.")

    except ValueError:
        print("Erro: Digita direito abestado!")