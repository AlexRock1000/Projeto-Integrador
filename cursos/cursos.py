from conexao import conectar

class Cursos:
    def __init__(self, nome_curso, descricao, area_curso, categoria, modalidade, id_instituicao, carga_horaria=None, data_inicio=None, data_termino=None, prazo_inscricao=None, quantidade_vagas=None, valor=0.00, gratuito=1, certificado=0, publico_alvo=None, pre_requisitos=None, cidade=None, estado=None, status_curso="Aberto", id_curso=None, data_cadastro=None):
        self.id_curso = id_curso
        self.nome_curso = nome_curso
        self.descricao = descricao
        self.area_curso = area_curso
        self.categoria = categoria
        self.modalidade = modalidade
        self.carga_horaria = carga_horaria
        self.data_inicio = data_inicio
        self.data_termino = data_termino
        self.prazo_inscricao = prazo_inscricao
        self.quantidade_vagas = quantidade_vagas
        self.valor = valor
        self.gratuito = gratuito
        self.certificado = certificado
        self.publico_alvo = publico_alvo
        self.pre_requisitos = pre_requisitos
        self.cidade = cidade
        self.estado = estado
        self.status_curso = status_curso
        self.id_instituicao = id_instituicao
        self.data_cadastro = data_cadastro

    def mostrar(self):
        print(f"""
    Código do Curso: {self.id_curso}
    Nome: {self.nome_curso}
    Descrição: {self.descricao}
    Área: {self.area_curso}
    Categoria: {self.categoria}
    Modalidade: {self.modalidade}
    Carga Horária: {self.carga_horaria}
    Data de Início: {self.data_inicio}
    Data de Termino: {self.data_termino}
    Prazo de Inscrição: {self.prazo_inscricao}
    Quantidade de Vagas: {self.quantidade_vagas}
    Valor: R$ {self.valor:.2f}
    Gratuito: {"Sim" if self.gratuito else "Não"}
    Certificado: {"Sim" if self.certificado else "Não"}
    Público Alvo: {self.publico_alvo}
    Pré-requisitos: {self.pre_requisitos}
    Cidade: {self.cidade}
    Estado: {self.estado}
    Status: {self.status_curso}
    ID Instituição: {self.id_instituicao}
    Cadastrado em: {self.data_cadastro}
    """)

    def salvar(self):
        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
            INSERT INTO curso (nome_curso, descricao, area_curso, categoria, modalidade, carga_horaria, data_inicio, data_termino, prazo_inscricao, quantidade_vagas, valor, gratuito, certificado, publico_alvo, pre_requisitos, cidade, estado, status_curso, id_instituicao) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        try:
            cursor.execute(sql, (
                self.nome_curso, self.descricao, self.area_curso, self.categoria, self.modalidade,
                self.carga_horaria, self.data_inicio, self.data_termino, self.prazo_inscricao,
                self.quantidade_vagas, self.valor, self.gratuito, self.certificado, self.publico_alvo,
                self.pre_requisitos, self.cidade, self.estado, self.status_curso, self.id_instituicao
            ))
            conexao.commit()
            print("Curso cadastrado com sucesso!")
        except Exception as err:
            print(f"Erro ao salvar curso: {err}")
        finally:
            conexao.close()
