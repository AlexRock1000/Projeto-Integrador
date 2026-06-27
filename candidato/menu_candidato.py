from candidato.candidato import Candidato
from candidato.cadastra_candidato import cadastrar_candidato
from candidato.mostrar_candidato import listar_candidatos, mostrar_candidato_por_codigo

def menu_candidato():
    print("""
    -------------------------
          MENU PRINCIPAL
    -------------------------
    1 - CADASTRAR NOVO CANDIDATO
    2 - MOSTRAR CANDIDATOS
    3 - PROCURAR CANDIDATO POR CÓDIGO  
    0 - SAIR
    -------------------------
    """)

def mostrar_candidatos():
    for candidato in listar_candidatos():
        candidato.mostrar()

def mostrar_candidato():
    try:
        codigo = int(input("Qual o código do candidato: "))
        candidato = mostrar_candidato_por_codigo(codigo)
        if candidato:
            candidato.mostrar_por_codigo()
        else:
            print("Candidato não encontrado.")

    except ValueError:
        print("Erro: Insira um código válido.")

while True:
    menu_candidato()
    try:
        opçao = input("Escolha uma opção: ")
        if opçao == "0":
            break
        elif opçao == "1": cadastrar_candidato()
        elif opçao == "2": mostrar_candidatos()
        elif opçao == "3": mostrar_candidato()
        else: print("Opção inválida.")

    except ValueError:
        print("Erro: Digita direito abestado!")