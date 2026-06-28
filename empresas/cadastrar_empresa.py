from conexao import conectar
from empresas.empresas import Empresas
from datetime import datetime

def cadastrar_empresa():
    try:
        razao_social = input("Qual a razão social da empresa: ")
        nome_fantasia = input("Qual o nome fantasia da empresa: ")
        cnpj = int(input("Qual o número do CNPJ: "))
        area_atuacao = input("Qual a área de atuação da empresa: ")
        email = input("Qual o email da empresa: ")
        telefone = int(input("Qual o telefone da empresa: "))
        site = input("Qual o site da empresa: ")
        cep = int(input("Qual o CEP: "))
        endereco = input("Qual o endereço da empresa: ")
        bairro = input("Qual o bairro da empresa: ")
        cidade = input("Qual a cidade da empresa: ")
        estado = input("Qual o estado da empresa: ")
        nome_responsavel = input("Qual o nome do responsável pela empresa: ")
        cargo_responsavel = input("Qual o cargo do responsável pela empresa: ")
        descricao = input("Descreva a empresa: ")
        senha = input("Crie uma senha: ")

    except ValueError:
        print("Erro: Por favor, insira os dados corretamente.")
        return
    
    empresa = Empresas(razao_social, nome_fantasia, cnpj, area_atuacao, email, telefone, site, cep, endereco, bairro, cidade, estado, nome_responsavel, cargo_responsavel, descricao, senha)
    
    empresa.salvar()