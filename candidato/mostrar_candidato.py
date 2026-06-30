from conexao import conectar
from candidato.candidato import Candidato

def listar_candidatos():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT * FROM candidato"
    cursor.execute(sql)

    candidatos = []
    for registro in cursor.fetchall():
        (id_cand, nome, num_cpf, dt_nasc, gen, mail, tel, num_cep, end, bai, cid, est, esc, inst, cur, res, hab, curr_url, lnk_url, pwd, status_conta, data_cadastro) = registro

        candidato = Candidato(id_candidato=id_cand, nome_completo=nome, cpf=num_cpf, data_nascimento=dt_nasc, genero=gen, email=mail, telefone=tel, cep=num_cep, endereco=end, bairro=bai, cidade=cid, estado=est, escolaridade=esc, instituicao_ensino=inst, curso=cur, resumo_profissional=res, habilidades=hab, curriculo_url=curr_url, linkedin_url=lnk_url, senha=pwd, status_conta=status_conta, data_cadastro=data_cadastro)

        candidatos.append(candidato)

    conexao.close()
    return candidatos

def mostrar_candidato_por_codigo(id_candidato):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT * FROM candidato WHERE id_candidato = %s"

    cursor.execute(sql, (id_candidato,))

    # Buscar apenas um registro
    resultado = cursor.fetchone()
    conexao.close()

    if resultado:
        (cod, nome, num_cpf, dt_nasc, gen, mail, tel, num_cep, end, bai, cid, est, esc, inst, cur, res, hab, curr_url, lnk_url, pwd, status_conta, data_cadastro) = resultado

        return Candidato(id_candidato=cod, nome_completo=nome, cpf=num_cpf, data_nascimento=dt_nasc, genero=gen, email=mail, telefone=tel, cep=num_cep, endereco=end, bairro=bai, cidade=cid, estado=est, escolaridade=esc, instituicao_ensino=inst, curso=cur, resumo_profissional=res, habilidades=hab, curriculo_url=curr_url, linkedin_url=lnk_url, senha=pwd, status_conta=status_conta, data_cadastro=data_cadastro)
        
    return None