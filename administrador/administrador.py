from conexao import conectar

class Administradores:
    def __init__(self, id_administrador, nome_completo, cpf, email, telefone, cargo, nivel_acesso, senha, status_conta, data_cadastro=None):
        self.id_administrador = id_administrador
        self.nome_completo = nome_completo
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.cargo = cargo
        self.nivel_acesso = nivel_acesso
        self.senha = senha
        self.status_conta = status_conta
        self.data_cadastro = data_cadastro

    def mostrar(self):
        print (f"""
    Código: {self.id_administrador}
    Nome: {self.nome_completo}
    CPF: {self.cpf}
    Email: {self.email}
    Telefone: {self.telefone}
    Cargo: {self.cargo}
    Nível de Acesso: {self.nivel_acesso}
    Telefone: {self.telefone}
    Senha: {self.senha}
    Status: {self.status_conta}
    Cadastrado_em: {self.data_cadastro}
    """)

    def mostrar_por_codigo(self):
        print(f"""
    Código: {self.id_administrador}
    Nome: {self.nome_completo}
    CPF: {self.cpf}
    Email: {self.email}
    Telefone: {self.telefone}
    Cargo: {self.cargo}
    Nível de Acesso: {self.nivel_acesso}
    Senha: {self.senha}
    Status: {self.status_conta}
    Status: {self.status_conta}
    Cadastrado_em: {self.data_cadastro}
    """)

    def salvar(self):
        conexao = conectar()
        cursor = conexao.cursor()

        sql = """INSERT INTO administrador (id_administrador, nome_completo, cpf, email, telefone, cargo, nivel_acesso, senha, status_conta, data_cadastro) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        try:
            cursor.execute(sql, (self.id_administrador, self.nome_completo, self.cpf, self.email, self.telefone, self.cargo, self.nivel_acesso, self.senha, self.status_conta, self.data_cadastro))
            conexao.commit()
            print(f"Administrador {self.nome_completo} salvo com sucesso!")
        except Exception as err:
            print(f"Erro ao salvar administrador: {err}")
        finally:
            conexao.close()
