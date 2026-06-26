from conexao import conectar

class Candidatos:
    def __init__(self, nome_completo, data_nascimento, cpf, email, genero, cidade, estado, rua, bairro, numero, complemento, CEP, telefone, PCD, nome_responsavel, escolaridade, resumo_profissional, habilidades, links, senha, id_aluno = None, data_cadastro = None, status = None):
        self.id_aluno = id_aluno
        self.nome_completo = nome_completo
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.email = email
        self.genero = genero
        self.cidade = cidade
        self.estado = estado
        self.rua = rua
        self.bairro = bairro
        self.numero = numero
        self.complemento = complemento
        self.CEP = CEP
        self.telefone = telefone
        self.PCD = PCD
        self.nome_responsavel = nome_responsavel
        self.escolaridade = escolaridade
        self.resumo_profissional = resumo_profissional
        self.habilidades = habilidades
        self.links = links
        self.senha = senha
        self.data_cadastro = data_cadastro
        self.status = status

    def mostrar(self):
        print (f"""
    Código: {self.id_aluno}
    Nome: {self.nome_completo}
    Data de Nascimento: {self.data_nascimento}
    CPF: {self.cpf}
    Email: {self.email}
    Gênero: {self.genero}
    Cidade: {self.cidade}
    Estado: {self.estado}
    Rua: {self.rua}
    Bairro: {self.bairro}
    Número: {self.numero}
    Complemento: {self.complemento}
    CEP: {self.CEP}
    Telefone: {self.telefone}
    PCD: {self.PCD}
    Nome do Responsável: {self.nome_responsavel}
    Escolaridade: {self.escolaridade}
    Resumo Profissional: {self.resumo_profissional}
    Habilidades: {self.habilidades}
    Links: {self.links}
    Cadastrado_em: {self.data_cadastro}
    Status: {self.status}
    """)

    def mostrar_por_codigo(self):
        print(f"""
    Código: {self.id_aluno}
    Nome: {self.nome_completo}
    Data de Nascimento: {self.data_nascimento}
    CPF: {self.cpf}
    Email: {self.email}
    Gênero: {self.genero}
    Cidade: {self.cidade}
    Estado: {self.estado}
    Rua: {self.rua}
    Bairro: {self.bairro}
    Número: {self.numero}
    Complemento: {self.complemento}
    CEP: {self.CEP}
    Telefone: {self.telefone}
    PCD: {self.PCD}
    Nome do Responsável: {self.nome_responsavel}
    Escolaridade: {self.escolaridade}
    Resumo Profissional: {self.resumo_profissional}
    Habilidades: {self.habilidades}
    Links: {self.links}
    Cadastrado_em: {self.data_cadastro}
    Status: {self.status}
    """)

    def salvar(self):
        conexao = conectar()
        cursor = conexao.cursor()

        sql = "INSERT INTO candidatos (nome_completo, data_nascimento, cpf, email, genero, cidade, estado, rua, bairro, numero, complemento, CEP, telefone, PCD, nome_responsavel, escolaridade, resumo_profissional, habilidades, links) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        cursor.execute(sql, (self.nome_completo, self.data_nascimento, self.cpf, self.email, self.genero, self.cidade, self.estado, self.rua, self.bairro, self.numero, self.complemento, self.CEP, self.telefone, self.PCD, self.nome_responsavel, self.escolaridade, self.resumo_profissional, self.habilidades, self.links))

        conexao.commit()
        conexao.close()