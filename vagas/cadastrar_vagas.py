from datetime import datetime
from vagas.vagas import Vagas

def cadastrar_vagas(id_empresa_logada):
    print("\n===== CADASTRO DE NOVA VAGA =====")

    try:
        titulo = input("Título da vaga: ")
        descricao = input("Descrição da vaga: ")
        print("""
        Tipos de vaga:
        1 - Emprego
        2 - Estágio
        3 - Jovem Aprendiz
        4 - Trainee
        """)

        tipos = {
        "1": "Emprego",
        "2": "Estágio",
        "3": "Jovem Aprendiz",
        "4": "Trainee"}

        tipo_vaga = tipos.get(input("Escolha: "), "Emprego")
        area_atuacao = input("Área de atuação: ")
        print("""
        Modalidade:
        1 - Presencial
        2 - Híbrido
        3 - Remoto
        """)

        modalidades = {
        "1": "Presencial",
        "2": "Híbrido",
        "3": "Remoto"}

        modalidade = modalidades.get(input("Escolha: "), "Presencial")
        carga_horaria = input("Carga horária: ")
        salario = float(input("Salário: "))
        beneficios = input("Benefícios: ")
        requisitos = input("Requisitos: ")
        print("""
        Escolaridade mínima:
        1 - Ensino Fundamental Incompleto
        2 - Ensino Fundamental Completo
        3 - Ensino Médio Incompleto
        4 - Ensino Médio Completo
        5 - Ensino Superior Incompleto
        6 - Ensino Superior Completo
        7 - Pós-Graduação
        """)

        escolaridades = {
        "1": "Ensino Fundamental Incompleto",
        "2": "Ensino Fundamental Completo",
        "3": "Ensino Médio Incompleto",
        "4": "Ensino Médio Completo",
        "5": "Ensino Superior Incompleto",
        "6": "Ensino Superior Completo",
        "7": "Pós-Graduação"
        }
        escolaridade_minima = escolaridades.get(input("Escolha: "),"Ensino Médio Completo")

        print("""
        Experiência exigida:
        1 - Sem experiência
        2 - Até 1 ano
        3 - De 1 a 3 anos
        4 - Acima de 3 anos
        """)

        opcao = input("Escolha uma opção: ")

        experiencias = {
        "1": "Sem experiência",
        "2": "Até 1 ano",
        "3": "De 1 a 3 anos",
        "4": "Acima de 3 anos"}

        experiencia_exigida = experiencias.get(opcao)

        if experiencia_exigida is None:
            print("Opção inválida!")
            return
        
        cidade = input("Cidade: ")
        estado = input("Estado: ")
        quantidade_vagas = int(input("Quantidade de vagas: "))
        data = input("Data de encerramento (dd/mm/aaaa): ")

        if data.strip():
            data_encerramento = datetime.strptime(data, "%d/%m/%Y").strftime("%Y-%m-%d")

        else: data_encerramento = None

        nova_vaga = Vagas(id_vaga=None, titulo=titulo, descricao=descricao, tipo_vaga=tipo_vaga, area_atuacao=area_atuacao, modalidade=modalidade, carga_horaria=carga_horaria, salario=salario, beneficios=beneficios, requisitos=requisitos, escolaridade_minima=escolaridade_minima, experiencia_exigida=experiencia_exigida, cidade=cidade, estado=estado, quantidade_vagas=quantidade_vagas, data_publicacao=None, data_encerramento=data_encerramento, status_vaga="Ativa", id_empresa=id_empresa_logada)

        nova_vaga.salvar()

    except ValueError:
        print("\nErro: Valor inválido.")