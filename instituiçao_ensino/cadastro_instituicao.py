from instituiçao_ensino.instituicao_ensino import InstituicaoEnsino
from datetime import datetime

def cadastrar_instituicaoEnsino():
    try:
        nome_instituicao = input("Qual o nome da instituição de ensino: ")
        cnpj = input("Qual o CNPJ da instituição de ensino: ")
        
        print("""
        Tipos de instituição disponíveis:
        1 - Universidade
        2 - Faculdade
        3 - Escola Técnica
        4 - ONG
        5 - Curso Livre
        6 - Instituto Federal
        7 - Outro
        """)
        tipo_opcao = input("Escolha o tipo de instituição: ")
        tipo_mapa = {"1": "Universidade", "2": "Faculdade", "3": "Escola Técnica", "4": "ONG", "5": "Curso Livre", "6": "Instituto Federal", "7": "Outro"}
        tipo_instituicao = tipo_mapa.get(tipo_opcao, "Outro")
        email = input("Qual o email da instituição de ensino: ")
        telefone = input("Qual o telefone da instituição de ensino: ")
        site = input("Qual o site da instituição de ensino: ")
        cep = input("Qual o CEP da instituição de ensino: ")
        endereco = input("Qual o endereço da instituição de ensino: ")
        bairro = input("Qual o bairro da instituição de ensino: ")
        cidade = input("Qual a cidade da instituição de ensino: ")
        estado = input("Qual o estado da instituição de ensino: ")
        nome_responsavel = input("Qual o nome do responsável: ")
        cargo_responsavel = input("Qual o cargo do responsável: ")
        descricao = input("Descreva a instituição de ensino: ")
        senha = input("Crie uma senha: ")
        print("""
        Status da conta disponíveis:
        1 - Pendente
        2 - Aprovada
        3 - Inativa
        """)
        status_opcao = input("Escolha o status da conta: ")
        status_mapa = {"1": "Pendente", "2": "Aprovada", "3": "Inativa"}
        status_conta = status_mapa.get(status_opcao, "Pendente")
        
        data_cadastro = datetime.now()
    except ValueError:
        print("Erro: Por favor, insira os dados corretamente.")
        return

    instituicao = InstituicaoEnsino(None, nome_instituicao, cnpj, tipo_instituicao, email, telefone, site, cep, endereco, bairro, cidade, estado, nome_responsavel, cargo_responsavel, descricao, senha, status_conta, data_cadastro)
    instituicao.salvar()