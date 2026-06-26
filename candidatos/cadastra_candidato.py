from conexao import conectar
from candidatos.candidatos import Candidatos

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