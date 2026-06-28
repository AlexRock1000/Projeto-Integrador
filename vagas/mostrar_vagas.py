from conexao import conectar
from vagas.vagas import Vagas

def listar_vagas():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT * FROM vaga"
    cursor.execute(sql)

    vagas = []
    for id_vaga, nome_curso, descricao, area_curso, categoria, modalidade, carga_horaria, data_inicio, data_termino, prazo_inscricao, quantidade_vagas, valor, gratuito, certificado, publico_alvo, pre_requisitos, cidade, estado in cursor.fetchall():

        vaga = Vagas(id_vaga=id_vaga, nome_curso=nome_curso, descricao=descricao, area_curso=area_curso, categoria=categoria, modalidade=modalidade, carga_horaria=carga_horaria, data_inicio=data_inicio, data_termino=data_termino, prazo_inscricao=prazo_inscricao, quantidade_vagas=quantidade_vagas, valor=valor, gratuito=gratuito, certificado=certificado, publico_alvo=publico_alvo, pre_requisitos=pre_requisitos, cidade=cidade, estado=estado)
        vagas.append(vaga)

    conexao.close()
    return vagas

def mostrar_vaga_por_codigo(id_vaga):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT * FROM vaga WHERE id_vaga = %s"
    cursor.execute(sql, (id_curso,))

    resultado = cursor.fetchone()
    conexao.close()

    if resultado:
        id_curso, nome_curso, descricao, area_curso, categoria, modalidade, carga_horaria, data_inicio, data_termino, prazo_inscricao, quantidade_vagas, valor, gratuito, certificado, publico_alvo, pre_requisitos, cidade, estado = resultado

        return Vagas(id_curso=id_curso, nome_curso=nome_curso, descricao=descricao, area_curso=area_curso, categoria=categoria, modalidade=modalidade, carga_horaria=carga_horaria, data_inicio=data_inicio, data_termino=data_termino, prazo_inscricao=prazo_inscricao, quantidade_vagas=quantidade_vagas, valor=valor, gratuito=gratuito, certificado=certificado, publico_alvo=publico_alvo, pre_requisitos=pre_requisitos, cidade=cidade, estado=estado)

    return None