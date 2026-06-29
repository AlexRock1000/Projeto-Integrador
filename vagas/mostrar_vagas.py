from conexao import conectar
from vagas.vagas import Vagas

def listar_vagas():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT * FROM vaga"
    cursor.execute(sql)

    vagas = []
    for id_vaga, titulo, descricao, tipo_vaga, area_atuacao, modalidade, carga_horaria, salario, beneficios, requisitos, escolaridade_minima, experiencia_exigida, cidade, estado, quantidade_vagas, data_publicacao, data_encerramento, status_vaga, id_empresa in cursor.fetchall():

        vaga = Vagas(id_vaga=id_vaga, titulo=titulo, descricao=descricao, tipo_vaga=tipo_vaga, area_atuacao=area_atuacao, modalidade=modalidade, carga_horaria=carga_horaria, salario=salario, beneficios=beneficios, requisitos=requisitos, escolaridade_minima=escolaridade_minima, experiencia_exigida=experiencia_exigida, cidade=cidade, estado=estado, quantidade_vagas=quantidade_vagas, data_publicacao=data_publicacao, data_encerramento=data_encerramento, status_vaga=status_vaga, id_empresa=id_empresa)

        vagas.append(vaga)

    cursor.close()
    conexao.close()

    return vagas

def mostrar_vaga_por_codigo(id_vaga):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT * FROM vaga WHERE id_vaga = %s"
    cursor.execute(sql, (id_vaga,))

    resultado = cursor.fetchone()

    cursor.close()
    conexao.close()

    if resultado:
        id_vaga, titulo, descricao, tipo_vaga, area_atuacao, modalidade, carga_horaria, salario, beneficios, requisitos, escolaridade_minima, experiencia_exigida, cidade, estado, quantidade_vagas, data_publicacao, data_encerramento, status_vaga, id_empresa = resultado

        return Vagas(id_vaga=id_vaga, titulo=titulo, descricao=descricao, tipo_vaga=tipo_vaga, area_atuacao=area_atuacao, modalidade=modalidade, carga_horaria=carga_horaria, salario=salario, beneficios=beneficios, requisitos=requisitos, escolaridade_minima=escolaridade_minima, experiencia_exigida=experiencia_exigida, cidade=cidade, estado=estado, quantidade_vagas=quantidade_vagas, data_publicacao=data_publicacao, data_encerramento=data_encerramento, status_vaga=status_vaga, id_empresa=id_empresa)

    return None