from conexao import conectar
from empresas.empresas import Empresas

def listar_empresas():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT * FROM empresas"
    cursor.execute(sql)

    empresas = []
    for id_empresa, nome_fantasia, razao_social, cnpj, area_atuacao, email, telefone, site, cep, endereco, bairro, cidade, estado, nome_responsavel, cargo_responsavel, descricao, senha, status, data_cadastro in cursor.fetchall():
        empresa = Empresas(id_empresa=id_empresa, nome_fantasia=nome_fantasia, razao_social=razao_social, cnpj=cnpj, area_atuacao=area_atuacao, email=email, telefone=telefone, site=site, cep=cep, endereco=endereco, bairro=bairro, cidade=cidade, estado=estado, nome_responsavel=nome_responsavel, cargo_responsavel=cargo_responsavel, descricao=descricao, senha=senha, status=status, data_cadastro=data_cadastro)   
        empresas.append(empresa)

    conexao.close()
    return empresas

def mostrar_empresa_por_codigo(id_empresa):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT * FROM empresas WHERE id_empresa = %s"
    cursor.execute(sql, (id_empresa,))

    resultado = cursor.fetchone()
    conexao.close()

    if resultado:
        id_empresa, razao_social, nome_fantasia, cnpj, area_atuacao, email, telefone, site, cep, endereco, bairro, cidade, estado, nome_responsavel, cargo_responsavel, descricao, senha, status, data_cadastro = resultado
        return Empresas(id_empresa=id_empresa, razao_social=razao_social, nome_fantasia=nome_fantasia, cnpj=cnpj, area_atuacao=area_atuacao, email=email, telefone=telefone, site=site, cep=cep, endereco=endereco, bairro=bairro, cidade=cidade, estado=estado, nome_responsavel=nome_responsavel, cargo_responsavel=cargo_responsavel, descricao=descricao, senha=senha, status=status, data_cadastro=data_cadastro)

    return None