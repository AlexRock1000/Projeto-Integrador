from conexao import conectar
from cursos.cursos import Cursos

def listar_cursos():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT * FROM curso"
    cursor.execute(sql)

    cursos = []
    for id_curso, nome_curso, descricao, area_curso, categoria, modalidade, carga_horaria, data_inicio, data_termino, prazo_inscricao, quantidade_vagas, valor, gratuito, certificado, publico_alvo, pre_requisitos, cidade, estado, status_curso, id_instituicao, data_cadastro in cursor.fetchall():

        curso = Cursos(id_curso=id_curso, nome_curso=nome_curso, descricao=descricao, area_curso=area_curso, categoria=categoria, modalidade=modalidade, carga_horaria=carga_horaria, data_inicio=data_inicio, data_termino=data_termino, prazo_inscricao=prazo_inscricao, quantidade_vagas=quantidade_vagas, valor=valor, gratuito=gratuito, certificado=certificado, publico_alvo=publico_alvo, pre_requisitos=pre_requisitos, cidade=cidade, estado=estado, status_curso=status_curso, id_instituicao=id_instituicao, data_cadastro=data_cadastro)

        cursos.append(curso)

    conexao.close()
    return cursos

def mostrar_curso_por_codigo(id_curso):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT * FROM curso WHERE id_curso = %s"
    cursor.execute(sql, (id_curso,))

    resultado = cursor.fetchone()
    conexao.close()

    if resultado:
        id_curso, nome_curso, descricao, area_curso, categoria, modalidade, carga_horaria, data_inicio, data_termino, prazo_inscricao, quantidade_vagas, valor, gratuito, certificado, publico_alvo, pre_requisitos, cidade, estado, status_curso, id_instituicao, data_cadastro = resultado

        return Cursos(id_curso=id_curso, nome_curso=nome_curso, descricao=descricao, area_curso=area_curso, categoria=categoria, modalidade=modalidade, carga_horaria=carga_horaria, data_inicio=data_inicio, data_termino=data_termino, prazo_inscricao=prazo_inscricao, quantidade_vagas=quantidade_vagas, valor=valor, gratuito=gratuito, certificado=certificado, publico_alvo=publico_alvo, pre_requisitos=pre_requisitos, cidade=cidade, estado=estado, status_curso=status_curso, id_instituicao=id_instituicao, data_cadastro=data_cadastro)

    return None

def meus_cursos(id_candidato_logado):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT c.id_curso, c.nome_curso, c.descricao, c.area_curso, c.categoria, c.modalidade, c.carga_horaria, c.data_inicio, c.data_termino, c.prazo_inscricao, c.quantidade_vagas, c.valor, c.gratuito, c.certificado, c.publico_alvo, c.pre_requisitos, c.cidade, c.estado, c.status_curso, c.id_instituicao, c.data_cadastro FROM inscricao_curso i INNER JOIN curso c ON i.id_curso = c.id_curso WHERE i.id_candidato = %s"

    print("\n---------- MEUS CURSOS ----------")
    try:
        cursor.execute(sql, (id_candidato_logado,))
        resultado = cursor.fetchall()
        if not resultado:
            print("\nVocê ainda não se inscreveu em nenhum curso.")
            return []

        lista_meus_cursos = []
        for linha in resultado:
            id_curso, nome_curso, descricao, area_curso, categoria, modalidade, carga_horaria, data_inicio, data_termino, prazo_inscricao, quantidade_vagas, valor, gratuito, certificado, publico_alvo, pre_requisitos, cidade, estado, status_curso, id_instituicao, data_cadastro = linha

            curso = Cursos(id_curso=id_curso, nome_curso=nome_curso, descricao=descricao, area_curso=area_curso, categoria=categoria, modalidade=modalidade, carga_horaria=carga_horaria, data_inicio=data_inicio, data_termino=data_termino, prazo_inscricao=prazo_inscricao, quantidade_vagas=quantidade_vagas, valor=valor, gratuito=gratuito, certificado=certificado, publico_alvo=publico_alvo, pre_requisitos=pre_requisitos, cidade=cidade, estado=estado, status_curso=status_curso, id_instituicao=id_instituicao, data_cadastro=data_cadastro)

            curso.mostrar()
            lista_meus_cursos.append(curso)

        return lista_meus_cursos
    except Exception as err:
        print(f"\nErro ao buscar suas inscrições: {err}")
        return []
    finally:
        conexao.close()