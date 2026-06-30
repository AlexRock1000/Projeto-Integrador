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

def minhas_vagas(id_candidato_logado):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT v.id_vaga, v.titulo, v.descricao, v.tipo_vaga, v.area_atuacao, v.modalidade, v.carga_horaria, v.salario, v.beneficios, v.requisitos, v.escolaridade_minima, v.experiencia_exigida, v.cidade, v.estado, v.quantidade_vagas, v.data_publicacao, v.data_encerramento, v.status_vaga, v.id_empresa FROM inscricao_vaga iv INNER JOIN vaga v ON iv.id_vaga = v.id_vaga WHERE iv.id_candidato = %s"

    print("\n---------- MINHAS VAGAS ----------")
    try:
        cursor.execute(sql, (id_candidato_logado,))
        resultado = cursor.fetchall()
        if not resultado:
            print("\nVocê ainda não se candidatou a nenhuma vaga.")
            return []
        
        lista_minhas_vagas = []
        for linha in resultado:
            id_vaga, titulo, descricao, tipo_vaga, area_atuacao, modalidade, carga_horaria, salario, beneficios, requisitos, escolaridade_minima, experiencia_exigida, cidade, estado, quantidade_vagas, data_publicacao, data_encerramento, status_vaga, id_empresa = linha

            vaga = Vagas(id_vaga=id_vaga, titulo=titulo, descricao=descricao, tipo_vaga=tipo_vaga, area_atuacao=area_atuacao, modalidade=modalidade, carga_horaria=carga_horaria, salario=salario, beneficios=beneficios, requisitos=requisitos, escolaridade_minima=escolaridade_minima, experiencia_exigida=experiencia_exigida, cidade=cidade, estado=estado, quantidade_vagas=quantidade_vagas, data_publicacao=data_publicacao, data_encerramento=data_encerramento, status_vaga=status_vaga, id_empresa=id_empresa)

            vaga.mostrar()
            lista_minhas_vagas.append(vaga)
        
        return lista_minhas_vagas
    except Exception as err:
        print(f"\nErro ao buscar suas vagas: {err}")
        return []
    finally:
        conexao.close()