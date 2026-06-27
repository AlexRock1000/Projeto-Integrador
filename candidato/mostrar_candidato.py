from conexao import conectar
from candidato.candidato import Candidato

def listar_candidatos():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT * FROM candidato"
    cursor.execute(sql)

    candidatos = []
    for id_candidato, nome_completo, data_nascimento, cpf, email, genero, cidade, estado, bairro, complemento, CEP, telefone, PCD, nome_responsavel, escolaridade, resumo_profissional, habilidades, links, cadastrado_em, status in cursor.fetchall():
        candidato = Candidato(id_candidato, nome_completo, data_nascimento, cpf, email, genero, cidade, estado, bairro, complemento, CEP, telefone, PCD, nome_responsavel, escolaridade, resumo_profissional, habilidades, links, cadastrado_em, status)
        candidatos.append(candidato)

    conexao.close()
    return candidatos

def mostrar_candidato_por_codigo(id_candidato):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT id_candidato, nome_completo, data_nascimento, cpf, email, genero, cidade, estado, bairro, complemento, CEP, telefone, PCD, nome_responsavel, escolaridade, resumo_profissional, habilidades, links, cadastrado_em, status FROM candidato WHERE id_candidato = %s"
    cursor.execute(sql, (id_candidato,))

    # Buscar apenas um registro
    resultado = cursor.fetchone()
    conexao.close()

    if resultado:
        cod, nome_completo, data_nascimento, cpf, email, genero, cidade, estado, bairro, complemento, CEP, telefone, PCD, nome_responsavel, escolaridade, resumo_profissional, habilidades, links, cadastrado_em, status = resultado

        return Candidato(id_candidato=cod, nome_completo=nome_completo, data_nascimento=data_nascimento, cpf=cpf, email=email, genero=genero, cidade=cidade, estado=estado, bairro=bairro, complemento=complemento, CEP=CEP, telefone=telefone, PCD=PCD, nome_responsavel=nome_responsavel, escolaridade=escolaridade, resumo_profissional=resumo_profissional, habilidades=habilidades, links=links, cadastrado_em=cadastrado_em, status=status)

    return None