from conexao import conectar
from instituiçao_ensino.instituicao_ensino import InstituicaoEnsino

def listar_instituicaoEnsino():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT * FROM instituicao_ensino"
    cursor.execute(sql)

    instituicaoEnsino = []
    for id_instituicao, nome_instituicao, cnpj, tipo_instituicao, email, telefone, site, cep, endereco, bairro, cidade, estado, nome_responsavel, cargo_responsavel, descricao, senha, status_conta, data_cadastro in cursor.fetchall():

        instituicao = InstituicaoEnsino(id_instituicao=id_instituicao, nome_instituicao=nome_instituicao, cnpj=cnpj, tipo_instituicao=tipo_instituicao, email=email, telefone=telefone, site=site, cep=cep, endereco=endereco, bairro=bairro, cidade=cidade, estado=estado, nome_responsavel=nome_responsavel, cargo_responsavel=cargo_responsavel, descricao=descricao, senha=senha, status_conta=status_conta, data_cadastro=data_cadastro)
        instituicaoEnsino.append(instituicao)

    conexao.close()
    return instituicaoEnsino

def mostrar_instituicao_por_codigo(id_instituicao):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT * FROM instituicao_ensino WHERE id_instituicao = %s"
    cursor.execute(sql, (id_instituicao,))

    resultado = cursor.fetchone()
    conexao.close()

    if resultado:
        id_instituicao, nome_instituicao, cnpj, tipo_instituicao, email, telefone, site, cep, endereco, bairro, cidade, estado, nome_responsavel, cargo_responsavel, descricao, senha, status_conta, data_cadastro = resultado

        return InstituicaoEnsino(id_instituicao=id_instituicao, nome_instituicao=nome_instituicao, cnpj=cnpj, tipo_instituicao=tipo_instituicao, email=email, telefone=telefone, site=site, cep=cep, endereco=endereco, bairro=bairro, cidade=cidade, estado=estado, nome_responsavel=nome_responsavel, cargo_responsavel=cargo_responsavel, descricao=descricao, senha=senha, status_conta=status_conta, data_cadastro=data_cadastro)

    return None