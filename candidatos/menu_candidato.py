from conexao import conectar
from candidatos.candidatos import Candidatos, listar_candidatos, mostrar_candidato_por_codigo

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

def cadastrar_candidato():
    try:
        nome_completo = input("Qual seu nome completo: ")
        data_nascimento = int(input("Qual sua data de nascimento: "))
        cpf = int(input("Qual o número do seu CPF: "))
        email = input("Qual seu email: ")
        genero = input("Qual seu gênero: ")
        estado = input("Qual estado você mora: ")
        cidade = input("Qual nome da sua cidade: ")
        bairro = input("Qual nome do seu bairro: ")
        rua = input("Qual o nome da sua rua: ")
        numero = int(input("Qual o número da sua casa: "))
        complemento = input("Complemento: ")
        CEP = int(input("Qual o CEP: "))
        telefone = int(input("Qual seu telefone: "))
        PCD = input("Você é PCD: ")
        nome_responsavel = input("Qual o nome do seu responsável: ")
        escolaridade = input("Qual sua escolaridade: ")
        resumo_profissional = input("Diga seu resumo profissional: ")
        habilidades = input("Quais são saus habilidades: ")
        links = input("Deseja compartilhar links: ")

    except ValueError:
        print("Erro: Por favor, insira os dados corretamente.")
        return
    
    candidato = Candidatos(nome_completo, data_nascimento, cpf, email, genero, cidade, estado, rua, bairro, numero, complemento, CEP, telefone, PCD, nome_responsavel, escolaridade, resumo_profissional, habilidades, links)
    candidato.salvar()

def mostrar_candidatos():
    for candidato in listar_candidatos():
        candidato.mostrar()

def mostrar_candidato():
    codigo = int(input("Qual o código do candidato: "))
    candidato = mostrar_candidato_por_codigo(codigo)
    if candidato:
        candidato.mostrar_por_codigo()
    else:
        print("Candidato não encontrado.")

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