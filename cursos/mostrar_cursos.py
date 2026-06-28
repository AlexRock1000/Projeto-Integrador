from conexao import conectar
from cursos.cursos import Cursos

def listar_cursos():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT * FROM curso"
    cursor.execute(sql)

    cursos = []
    for id_curso, nome_curso, descricao, area_curso, categoria, modalidade, carga_horaria, data_inicio, data_termino, prazo_inscricao, quantidade_vagas, valor, gratuito, certificado, publico_alvo, pre_requisitos, cidade, estado in cursor.fetchall():

        curso = Cursos(id_curso=id_curso, nome_curso=nome_curso, descricao=descricao, area_curso=area_curso, categoria=categoria, modalidade=modalidade, carga_horaria=carga_horaria, data_inicio=data_inicio, data_termino=data_termino, prazo_inscricao=prazo_inscricao, quantidade_vagas=quantidade_vagas, valor=valor, gratuito=gratuito, certificado=certificado, publico_alvo=publico_alvo, pre_requisitos=pre_requisitos, cidade=cidade, estado=estado)
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
        id_curso, nome_curso, descricao, area_curso, categoria, modalidade, carga_horaria, data_inicio, data_termino, prazo_inscricao, quantidade_vagas, valor, gratuito, certificado, publico_alvo, pre_requisitos, cidade, estado = resultado

        return Cursos(id_curso=id_curso, nome_curso=nome_curso, descricao=descricao, area_curso=area_curso, categoria=categoria, modalidade=modalidade, carga_horaria=carga_horaria, data_inicio=data_inicio, data_termino=data_termino, prazo_inscricao=prazo_inscricao, quantidade_vagas=quantidade_vagas, valor=valor, gratuito=gratuito, certificado=certificado, publico_alvo=publico_alvo, pre_requisitos=pre_requisitos, cidade=cidade, estado=estado)

    return None