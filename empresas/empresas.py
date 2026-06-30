from conexao import conectar

class Empresas:
    def __init__(self, razao_social, nome_fantasia, cnpj, area_atuacao, email, telefone, site, cep, endereco, bairro, cidade, estado, nome_responsavel, cargo_responsavel, descricao, senha, id_empresa=None, status_conta="Pendente", data_cadastro=None):
        self.id_empresa = id_empresa
        self.razao_social = razao_social
        self.nome_fantasia = nome_fantasia
        self.cnpj = cnpj
        self.area_atuacao = area_atuacao
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
    Código: {self.id_empresa}
    Nome: {self.nome_fantasia}
    Razão Social: {self.razao_social}
    Área de Atuação: {self.area_atuacao}
    Endereço: {self.endereco}
    Bairro: {self.bairro}
    Cidade: {self.cidade}
    Estado: {self.estado}
    Status: {self.status_conta}
    """)

    def mostrar_por_codigo(self):
        print(f"""
    Código: {self.id_empresa}
    Nome: {self.nome_fantasia}
    Razão Social: {self.razao_social}
    CNPJ: {self.cnpj}
    Email: {self.email}
    Área de Atuação: {self.area_atuacao}
    Telefone: {self.telefone}
    Site: {self.site}
    CEP: {self.cep}
    Endereço: {self.endereco}
    Bairro: {self.bairro}
    Cidade: {self.cidade}
    Estado: {self.estado}
    Nome do Responsável: {self.nome_responsavel}
    Cadastrado_em: {self.data_cadastro}
    Status: {self.status_conta}
    """)

    def salvar(self):
        conexao = conectar()
        cursor = conexao.cursor()

        sql = """INSERT INTO empresa (razao_social, nome_fantasia, cnpj, area_atuacao, email, telefone, site, cep, endereco, bairro, cidade, estado, nome_responsavel, cargo_responsavel, descricao, senha, status_conta) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        try:
            cursor.execute(sql, (
                self.razao_social, self.nome_fantasia, self.cnpj, self.area_atuacao, 
                self.email, self.telefone, self.site, self.cep, self.endereco, 
                self.bairro, self.cidade, self.estado, self.nome_responsavel, 
                self.cargo_responsavel, self.descricao, self.senha, self.status_conta
            ))
            conexao.commit()
            print(f"Empresa {self.nome_fantasia} salva com sucesso!")
        except Exception as err:
            print(f"Erro ao salvar empresa: {err}")
        finally:
            conexao.close()
