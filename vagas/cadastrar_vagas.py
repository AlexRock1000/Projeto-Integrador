from datetime import datetime
from vagas.vagas import Vagas

def cadastrar_vagas(id_instituicao_logada):
    print("\n--- CADASTRO DE NOVA VAGA ---")
    try:
        nome_vaga = input("Nome da vaga: ")
        descricao = input("Descrição da vaga: ")
        area_vaga = input("Área da vaga (ex: Tecnologia): ")
        categoria = input("Categoria da vaga: ")
        print("""
              Categorias válidas: 
              Profissionalizante
              Técnico
              Extensão
              Livre
              Workshop
              """)
        modalidade = input("Modalidade da vaga: ")
        print("""
              Modalidades válidas: 
              Presencial
              Online
              Híbrido
              """)
        
        carga_horaria = input("Carga horária: ")
        # Validação da Data
        data_inicio = input("Data de início (Deixe vazio se não houver): ")
        objeto_data = datetime.strptime(data_inicio, "%d/%m/%Y")
        data_inicio = objeto_data.strftime("%Y-%m-%d")
    
        data_termino = input("Data de término (Deixe vazio se não houver): ")
        objeto_data = datetime.strptime(data_termino, "%d/%m/%Y")
        data_termino = objeto_data.strftime("%Y-%m-%d")

        prazo_inscricao = input("Prazo de inscrição (Deixe vazio se não houver): ")
        objeto_data = datetime.strptime(prazo_inscricao, "%d/%m/%Y")
        prazo_inscricao = objeto_data.strftime("%Y-%m-%d")

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

    nova_vaga = Vagas(nome_curso=nome_curso, descricao=descricao, area_curso=area_curso, categoria=categoria, modalidade=modalidade, carga_horaria=carga_horaria, data_inicio=data_inicio, data_termino=data_termino, prazo_inscricao=prazo_inscricao, quantidade_vagas=quantidade_vagas, valor=valor, gratuito=gratuito, certificado=certificado, publico_alvo=publico_alvo, pre_requisitos=pre_requisitos, cidade=cidade, estado=estado, id_instituicao=id_instituicao_logada) # Passando o ID da instituição logada no sistema
    
    nova_vaga.salvar()
