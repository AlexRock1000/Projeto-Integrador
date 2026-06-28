from datetime import datetime
from conexao import conectar

class Candidato:
    def __init__(self, id_candidato=None, nome_completo=None, cpf=None, data_nascimento=None, genero=None, email=None, telefone=None, cep=None, endereco=None, bairro=None, cidade=None, estado=None, escolaridade=None, instituicao_ensino=None, curso=None, resumo_profissional=None, habilidades=None, curriculo_url=None, linkedin_url=None, senha=None, status_conta="Ativa", data_cadastro=None):

        self.id_candidato = id_candidato
        self.nome_completo = nome_completo
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.genero = genero
        self.email = email
        self.telefone = telefone
        self.cep = cep
        self.endereco = endereco
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.escolaridade = escolaridade
        self.instituicao_ensino = instituicao_ensino
        self.curso = curso
        self.resumo_profissional = resumo_profissional
        self.habilidades = habilidades
        self.curriculo_url = curriculo_url
        self.linkedin_url = linkedin_url
        self.senha = senha
        self.status_conta = status_conta
        
        # Se for um cadastro novo, define a data e hora atual
        if data_cadastro is None:
            self.data_cadastro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        else:
            self.data_cadastro = data_cadastro

    def mostrar(self):
        print(f"""
    --------------------------------------------------
    Código: {self.id_candidato}
    Nome: {self.nome_completo}
    CPF: {self.cpf}
    Data de Nascimento: {self.data_nascimento}
    Gênero: {self.genero}
    Email: {self.email}
    Telefone: {self.telefone}
    CEP: {self.cep}
    Endereço: {self.endereco}
    Bairro: {self.bairro}
    Cidade: {self.cidade}
    Estado: {self.estado}
    Escolaridade: {self.escolaridade}
    Instituição de Ensino: {self.instituicao_ensino}
    Curso: {self.curso}
    Resumo Profissional: {self.resumo_profissional}
    Habilidades: {self.habilidades}
    Currículo: {self.curriculo_url}
    LinkedIn: {self.linkedin_url}
    Status da Conta: {self.status_conta}
    Data de Cadastro: {self.data_cadastro}
    --------------------------------------------------
    """)

    def salvar(self):
        conexao = conectar()
        cursor = conexao.cursor()

        sql = """INSERT INTO candidato (nome_completo, cpf, data_nascimento, genero, email, telefone, cep, endereco, bairro, cidade, estado, escolaridade, instituicao_ensino, curso, resumo_profissional, habilidades, curriculo_url, linkedin_url, senha, status_conta, data_cadastro) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        valores = (self.nome_completo, self.cpf, self.data_nascimento, self.genero, self.email, self.telefone, self.cep, self.endereco, self.bairro, self.cidade, self.estado, self.escolaridade, self.instituicao_ensino, self.curso, self.resumo_profissional, self.habilidades, self.curriculo_url, self.linkedin_url, self.senha, self.status_conta, self.data_cadastro)

        cursor.execute(sql, valores)
        print(f"Candidato {self.nome_completo} salvo com sucesso!")
        conexao.commit()
        
        # Recupera o ID gerado pelo banco e salva no objeto
        self.id_candidato = cursor.lastrowid
        
        cursor.close()
        conexao.close()
