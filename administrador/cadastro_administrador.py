from administrador.administrador import Administradores
from datetime import datetime

def cadastrar_administrador():
    try:
        nome_completo = input("Qual o nome completo do administrador: ")
        cpf = input("Qual o CPF do administrador: ")
        email = input("Qual o email do administrador: ")
        telefone = int(input("Qual o telefone do administrador: "))
        cargo = input("Qual o cargo do administrador: ")
        print("""
        Níveis de acesso disponíveis:
        1 - Administrador
        2 - Moderador
        3 - Super Administrador
        """)
        nivel_opcao = input("Escolha o nível de acesso: ")
        nivel_mapa = {"1": "Administrador", "2": "Moderador", "3": "Super Administrador"}
        nivel_acesso = nivel_mapa.get(nivel_opcao, "Administrador")
        
        senha = input("Crie uma senha: ")
        
        print("""
        Status da conta disponíveis:
        1 - Ativa
        2 - Inativa
        """)
        status_opcao = input("Escolha o status da conta: ")
        status_mapa = {"1": "Ativa", "2": "Inativa"}
        status_conta = status_mapa.get(status_opcao, "Ativa")
        
        data_cadastro = datetime.now()
    except ValueError:
        print("Erro: Por favor, insira os dados corretamente.")
        return

    administrador = Administradores(None, nome_completo, cpf, email, telefone, cargo, nivel_acesso, senha, status_conta, data_cadastro)
    administrador.salvar()