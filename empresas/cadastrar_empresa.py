from conexao import conectar
from empresas.empresas import Empresas
from datetime import datetime

def cadastrar_empresa():
    try:
        nome_fantasia = input("Qual o nome fantasia da empresa: ")
        objeto_data = datetime.strptime(data_fundacao, "%d/%m/%Y") # Converte DD/MM/AAAA para o formato do MySQL (AAAA-MM-DD)
        data_fundacao = objeto_data.strftime("%Y-%m-%d")
        razao_social = input("Qual a razão social da empresa: ")
        cnpj = int(input("Qual o número do CNPJ: "))
        email = input("Qual o email da empresa: ")
        telefone = int(input("Qual o telefone da empresa: "))
        estado = input("Qual estado você mora: ")
        cidade = input("Qual nome da sua cidade: ")
        bairro = input("Qual nome do seu bairro: ")
        cep = int(input("Qual o CEP: "))
        endereco = input("Qual o endereço da empresa: ")
        cargo_responsavel = input("Qual o cargo do responsável: ")
        nome_responsavel = input("Qual o nome do seu responsável: ")
        area_atuacao = input("Qual a área de atuação da empresa: ")
        site = input("Qual o site da empresa: ")
        descricao = input("Descreva a empresa: ")
        senha = input("Crie uma senha: ")

    except ValueError:
        print("Erro: Por favor, insira os dados corretamente.")
        return

    status = "Ativo"
    data_cadastro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    empresa = Empresas(razao_social, nome_fantasia, cnpj, area_atuacao, email, telefone, site, cep, endereco, bairro, cidade, estado, nome_responsavel, cargo_responsavel, descricao, senha, status=status, data_cadastro=data_cadastro)
    empresa.salvar()