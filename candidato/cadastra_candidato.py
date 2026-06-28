from datetime import datetime
from conexao import conectar
from candidato.candidato import Candidato

def cadastrar_candidato():
    try:
        nome_completo = input("Qual seu nome completo: ")
        cpf = input("Qual o número do seu CPF: ")
        
        # Validação da Data
        data_input = input("Qual sua data de nascimento (DD/MM/AAAA): ")
        objeto_data = datetime.strptime(data_input, "%d/%m/%Y")
        data_nascimento = objeto_data.strftime("%Y-%m-%d")
        
        # Tratamento para o ENUM do Gênero
        print("\nEscolha seu gênero:")
        print("1 - Masculino\n2 - Feminino\n3 - Outro\n4 - Prefiro não informar")
        opc_genero = input("Opção: ")
        mapa_genero = {"1": "Masculino", "2": "Feminino", "3": "Outro", "4": "Prefiro não informar"}
        genero = mapa_genero.get(opc_genero, "Prefiro não informar")
        
        email = input("\nQual seu email: ")
        telefone = input("Qual seu telefone: ")
        cep = input("Qual o CEP: ")
        endereco = input("Qual seu endereço: ")
        bairro = input("Qual nome do seu bairro: ")
        cidade = input("Qual nome da sua cidade: ")
        estado = input("Qual a sigla do estado (Ex: SP): ")
        
        # Tratamento para o ENUM da Escolaridade
        print("""
            Qual sua escolaridade:
        1 - Ensino Fundamental Incompleto
        2 - Ensino Fundamental Completo
        3 - Ensino Médio Incompleto
        4 - Ensino Médio Completo
        5 - Ensino Superior Incompleto
        6 - Ensino Superior Completo""")

        opc_escolaridade = input("Opção: ")
        mapa_escolaridade = {
            "1": "Ensino Fundamental Incompleto",
            "2": "Ensino Fundamental Completo",
            "3": "Ensino Médio Incompleto",
            "4": "Ensino Médio Completo",
            "5": "Ensino Superior Incompleto",
            "6": "Ensino Superior Completo"}
        
        # Garante que envie uma opção válida ou joga erro para o except
        if opc_escolaridade not in mapa_escolaridade:
            raise ValueError("Opção de escolaridade inválida.")
        escolaridade = mapa_escolaridade[opc_escolaridade]

        instituicao_ensino = input("\nQual o nome da sua instituição de ensino: ")
        curso = input("Qual curso você está cursando: ")
        resumo_profissional = input("Diga seu resumo profissional: ")
        habilidades = input("Quais são suas habilidades: ")
        curriculo_url = input("Qual o URL do seu currículo: ")
        linkedin_url = input("Qual o URL do seu LinkedIn: ")
        senha = input("Crie uma senha: ")

    except ValueError as e:
        print(f"\nErro: Dados inválidos ou formato incorreto! ({e})")
        return
    
    candidato = Candidato(nome_completo=nome_completo, cpf=cpf, data_nascimento=data_nascimento, genero=genero, email=email, telefone=telefone, cep=cep, endereco=endereco, bairro=bairro, cidade=cidade, estado=estado, escolaridade=escolaridade,instituicao_ensino=instituicao_ensino, curso=curso, resumo_profissional=resumo_profissional, habilidades=habilidades, curriculo_url=curriculo_url, linkedin_url=linkedin_url, senha=senha)
    
    candidato.salvar()
