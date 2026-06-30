from conexao import conectar
from datetime import datetime
from cursos.cursos import Cursos

def cadastrar_curso(id_instituicao_logada):
    print("\n--- CADASTRO DE NOVO CURSO ---")
    try:
        nome_curso = input("Nome do curso: ")
        descricao = input("Descrição do curso: ")
        area_curso = input("Área do curso (ex: Tecnologia): ")
        print("""
        Qual a categoria do curso: 
        1 - Profissionalizante
        2 - Técnico
        3 - Extensão
        4 - Livre
        5 - Workshop
        """)
        categorias = {"1": "Profissionalizante", "2": "Técnico", "3": "Extensão", "4": "Livre", "5": "Workshop"}
        categoria = categorias.get(input("Escolha: "), "Profissionalizante")

        print("""
        Qual a modalidade do curso: 
        1 - Presencial
        2 - Online
        3 - Híbrido
        """)
        modalidades = {"1": "Presencial", "2": "Online", "3": "Híbrido"}
        modalidade = modalidades.get(input("Escolha: "), "Presencial")

        carga_horaria = input("Carga horária: ")
        # Validação da Data
        data_inicio = input("Data de início (Deixe vazio se não houver): ")
        if data_inicio.strip():
            data_inicio = datetime.strptime(data_inicio, "%d/%m/%Y").strftime("%Y-%m-%d")

        else: data_inicio = None
    
        data_termino = input("Data de término (Deixe vazio se não houver): ")
        if data_termino.strip():
            data_termino = datetime.strptime(data_termino, "%d/%m/%Y").strftime("%Y-%m-%d")

        else: data_termino = None

        prazo_inscricao = input("Prazo de inscrição (Deixe vazio se não houver): ")
        if prazo_inscricao.strip():
            prazo_inscricao = datetime.strptime(prazo_inscricao, "%d/%m/%Y").strftime("%Y-%m-%d")

        else: prazo_inscricao = None

        vagas_input = input("Quantidade de vagas: ")
        quantidade_vagas = int(vagas_input) if vagas_input else None

        valor_input = input("Valor do curso: ")
        valor = float(valor_input) if valor_input else 0.00

        gratuito = 1 if valor == 0.00 else 0

        print("\nPossui certificado?\n1 - Sim\n2 - Não")
        certificado_opcao = input("Escolha uma opção: ")
        certificado = 1 if certificado_opcao == "1" else 0

        publico_alvo = input("Público-alvo: ")
        pre_requisitos = input("Pré-requisitos: ")
        cidade = input("Cidade: ")
        estado = input("Estado: ")

    except ValueError:
        print("\nErro: Por favor, insira números válidos para vagas ou valor.")
        return

    novo_curso = Cursos(nome_curso=nome_curso, descricao=descricao, area_curso=area_curso, categoria=categoria, modalidade=modalidade, carga_horaria=carga_horaria, data_inicio=data_inicio, data_termino=data_termino, prazo_inscricao=prazo_inscricao, quantidade_vagas=quantidade_vagas, valor=valor, gratuito=gratuito, certificado=certificado, publico_alvo=publico_alvo, pre_requisitos=pre_requisitos, cidade=cidade, estado=estado, id_instituicao=id_instituicao_logada) # Passando o ID da instituição logada no sistema
    
    novo_curso.salvar()

def inscriçao_curso(id_candidato_logado):
    try:
        id_curso_escolhido = int(input("\nDigite o código do curso que deseja se candidatar: "))
        
    except ValueError:
        print("Código do curso não encontrado!")
        return

    conexao = conectar()
    cursor = conexao.cursor()
   
    try:
        registro = "INSERT INTO inscricao_curso (id_candidato, id_curso) VALUES (%s, %s)"
        cursor.execute(registro, (id_candidato_logado, id_curso_escolhido))
        conexao.commit()
        print("\nInscrição realizada com sucesso!")

    except Exception as err:
        print(f"\nErro ao registrar inscrição: {err}")

    finally:
        conexao.close()