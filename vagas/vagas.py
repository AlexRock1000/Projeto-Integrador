from conexao import conectar


class Vagas:
    def __init__(self, id_vaga, titulo, descricao, tipo_vaga, area_atuacao, modalidade, carga_horaria, salario, beneficios, requisitos, escolaridade_minima, experiencia_exigida, cidade, estado, quantidade_vagas, data_encerramento, id_empresa, data_publicacao=None, status_vaga="Ativa"):
        self.id_vaga = id_vaga
        self.titulo = titulo
        self.descricao = descricao
        self.tipo_vaga = tipo_vaga
        self.area_atuacao = area_atuacao
        self.modalidade = modalidade
        self.carga_horaria = carga_horaria
        self.salario = salario
        self.beneficios = beneficios
        self.requisitos = requisitos
        self.escolaridade_minima = escolaridade_minima
        self.experiencia_exigida = experiencia_exigida
        self.cidade = cidade
        self.estado = estado
        self.quantidade_vagas = quantidade_vagas
        self.data_publicacao = data_publicacao
        self.data_encerramento = data_encerramento
        self.status_vaga = status_vaga
        self.id_empresa = id_empresa

    def mostrar(self):
        salario = (f"R$ {self.salario:.2f}" if self.salario is not None else "Não informado")
        print(f"""
    ===============================
    Código da Vaga: {self.id_vaga}
    Título: {self.titulo}
    Descrição: {self.descricao}
    Tipo de Vaga: {self.tipo_vaga}
    Área de Atuação: {self.area_atuacao}
    Modalidade: {self.modalidade}
    Carga Horária: {self.carga_horaria}
    Salário: {salario}
    Benefícios: {self.beneficios}
    Requisitos: {self.requisitos}
    Escolaridade Mínima: {self.escolaridade_minima}
    Experiência Exigida: {self.experiencia_exigida}
    Cidade: {self.cidade}
    Estado: {self.estado}
    Quantidade de Vagas: {self.quantidade_vagas}
    Data de Publicação: {self.data_publicacao}
    Data de Encerramento: {self.data_encerramento}
    Status da Vaga: {self.status_vaga}
    ID da Empresa: {self.id_empresa}
    ===============================
    """)

    def salvar(self):
        conexao = conectar()
        cursor = conexao.cursor()

        sql = """INSERT INTO vaga(titulo, descricao, tipo_vaga, area_atuacao, modalidade, carga_horaria, salario, beneficios, requisitos, escolaridade_minima, experiencia_exigida, cidade, estado, quantidade_vagas, data_encerramento, status_vaga, id_empresa) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        try:
            cursor.execute(sql, (self.titulo, self.descricao, self.tipo_vaga, self.area_atuacao, self.modalidade, self.carga_horaria, self.salario, self.beneficios, self.requisitos, self.escolaridade_minima, self.experiencia_exigida, self.cidade, self.estado, self.quantidade_vagas, self.data_encerramento, self.status_vaga, self.id_empresa))

            conexao.commit()
            print("Vaga cadastrada com sucesso!")

        except Exception as err:
            print(f"Erro ao salvar vaga: {err}")

        finally:
            cursor.close()
            conexao.close()