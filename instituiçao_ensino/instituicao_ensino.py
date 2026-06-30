from conexao import conectar

class InstituicaoEnsino:
    def __init__(self, id_instituicao, nome_instituicao, cnpj, tipo_instituicao, email, telefone, site, cep, endereco, bairro, cidade, estado, nome_responsavel, cargo_responsavel, descricao, senha, status_conta, data_cadastro=None):
        self.id_instituicao = id_instituicao
        self.nome_instituicao = nome_instituicao
        self.cnpj = cnpj
        self.tipo_instituicao = tipo_instituicao
        self.email = email
        self.telefone = telefone
        self.site = site
        self.cep = cep
        self.endereco = endereco
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.nome_responsavel = nome_responsavel
        self.cargo_responsavel = cargo_responsavel
        self.descricao = descricao
        self.senha = senha
        self.status_conta = status_conta
        self.data_cadastro = data_cadastro

    def mostrar(self):
        print (f"""
    Código: {self.id_instituicao}
    Nome: {self.nome_instituicao}
    Tipo de Instituição: {self.tipo_instituicao}
    Endereço: {self.endereco}
    Bairro: {self.bairro}
    Cidade: {self.cidade}
    Estado: {self.estado}
    Descrição: {self.descricao}
    Status: {self.status_conta}
    """)

    def mostrar_por_codigo(self):
        print(f"""
    Código: {self.id_instituicao}
    Nome: {self.nome_instituicao}
    CNPJ: {self.cnpj}
    Tipo de Instituição: {self.tipo_instituicao}
    Email: {self.email}
    Telefone: {self.telefone}
    Endereço: {self.endereco}
    Bairro: {self.bairro}
    Cidade: {self.cidade}
    Estado: {self.estado}
    Nome do Responsável: {self.nome_responsavel}
    Cargo do Responsável: {self.cargo_responsavel}
    Descrição: {self.descricao}
    Senha: {self.senha}
    Status: {self.status_conta}
    Cadastrado_em: {self.data_cadastro}
    """)

    def salvar(self):
        conexao = conectar()
        cursor = conexao.cursor()

        sql = """INSERT INTO instituicao_ensino (nome_instituicao, cnpj, tipo_instituicao, email, telefone, site, cep, endereco, bairro, cidade, estado, nome_responsavel, cargo_responsavel, descricao, senha, status_conta, data_cadastro) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        try:
            cursor.execute(sql, (self.nome_instituicao, self.cnpj, self.tipo_instituicao, self.email, self.telefone, self.site, self.cep, self.endereco, self.bairro, self.cidade, self.estado, self.nome_responsavel, self.cargo_responsavel, self.descricao, self.senha, self.status_conta, self.data_cadastro))
            conexao.commit()
            print(f"Instituição de Ensino {self.nome_instituicao} salva com sucesso!")
        except Exception as err:
            print(f"Erro ao salvar instituição de ensino: {err}")
        finally:
            conexao.close()
