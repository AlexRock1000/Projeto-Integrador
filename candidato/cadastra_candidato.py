from conexao import conectar
from candidato.candidato import Candidato

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
        complemento = input("Complemento: ")
        CEP = int(input("Qual o CEP: "))
        telefone = int(input("Qual seu telefone: "))
        PCD = input("Você é PCD: ")
        nome_responsavel = input("Qual o nome do seu responsável: ")
        escolaridade = input("Qual sua escolaridade: ")
        resumo_profissional = input("Diga seu resumo profissional: ")
        habilidades = input("Quais são saus habilidades: ")
        links = input("Deseja compartilhar links: ")
        senha = input("Crie uma senha: ")

    except ValueError:
        print("Erro: Por favor, insira os dados corretamente.")
        return
    
    candidato = Candidato(nome_completo, data_nascimento, cpf, email, genero, cidade, estado, bairro, complemento, CEP, telefone, PCD, nome_responsavel, escolaridade, resumo_profissional, habilidades, links, senha)
    candidato.salvar()