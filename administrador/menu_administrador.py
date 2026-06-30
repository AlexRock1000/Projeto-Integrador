from administrador.administrador import Administradores
from administrador.cadastro_administrador import cadastrar_administrador
from administrador.mostrar_administrador import listar_administradores, mostrar_administrador_por_codigo
from candidato.mostrar_candidato import listar_candidatos, mostrar_candidato_por_codigo
from empresas.mostrar_empresa import listar_empresas, mostrar_empresa_por_codigo
from instituiçao_ensino.mostrar_instituicao import listar_instituicaoEnsino, mostrar_instituicao_por_codigo

def menu_administrador():
    print("""
    -------------------------
          MENU ADMINISTRADOR
    -------------------------
    1 - CADASTRAR NOVO ADMINISTRADOR
    2 - MOSTRAR ADMINISTRADORES
    3 - PROCURAR ADMINISTRADOR POR CÓDIGO
    4 - MOSTRAR CANDIDATOS CADASTRADOS
    5 - PROCURAR CANDIDATO POR CÓDIGO
    6 - MOSTRAR EMPRESAS
    7 - PROCURAR EMPRESA POR CÓDIGO
    8 - MOSTRAR INSTITUIÇÕES DE ENSINO
    9 - PROCURAR INSTITUIÇÃO DE ENSINO POR CÓDIGO
    0 - VOLTAR PARA O MENU PRINCIPAL
    00 - SAIR
    -------------------------
    """)

def opçoes_menu_administrador():
    while True:
        menu_administrador()
        try:
            opçao = input("Escolha uma opção: ")
            if opçao == "00":
                print("Saindo...")
                exit()
            elif opçao == "1": cadastrar_administrador()
            elif opçao == "2": mostrar_administradores()
            elif opçao == "3": mostrar_administrador()
            elif opçao == "4": mostrar_candidatos()
            elif opçao == "5": mostrar_candidato()
            elif opçao == "6": mostrar_empresas()
            elif opçao == "7": mostrar_empresa()
            elif opçao == "8": mostrar_instituicoes()
            elif opçao == "9": mostrar_instituicao()
            elif opçao == "0": return
            else: print("Opção inválida: Digita direito abestado!")

        except ValueError:
            print("Erro: Digita direito abestado!")

def mostrar_administradores():
    administradores = listar_administradores()
    if not administradores:
        print("Nenhum administrador cadastrado.")
        return

    for administrador in administradores:
        administrador.mostrar()

def mostrar_administrador():
    try:
        codigo = int(input("Qual o código do administrador: "))
        administrador = mostrar_administrador_por_codigo(codigo)
        if administrador:
            administrador.mostrar_por_codigo()
        else:
            print("Administrador não encontrado.")

    except ValueError:
        print("Erro: Insira um código válido.")

def mostrar_candidatos():
    candidatos = listar_candidatos()
    if not candidatos:
        print("\nNenhum candidato cadastrado.")
        return

    for candidato in candidatos:
        candidato.mostrar()

def mostrar_candidato():
    try:
        codigo = int(input("Qual o código do candidato: "))
        candidato = mostrar_candidato_por_codigo(codigo)
        if candidato:
            candidato.mostrar_por_codigo()
        else:
            print("\nCandidato não encontrado.")

    except ValueError:
        print("Erro: Insira um código válido.")

def mostrar_empresas():
    empresas = listar_empresas()
    if not empresas:
        print("Nenhuma empresa cadastrada.")
        return

    for empresa in empresas:
        empresa.mostrar()

def mostrar_empresa():
    try:
        codigo = int(input("Qual o código da empresa: "))
        empresa = mostrar_empresa_por_codigo(codigo)
        if empresa:
            empresa.mostrar_por_codigo()
        else:
            print("Empresa não encontrada.")

    except ValueError:
        print("Erro: Insira um código válido.")

def mostrar_instituicoes():
    instituicoes = listar_instituicaoEnsino()
    if not instituicoes:
        print("Nenhuma instituição de ensino cadastrada.")
        return

    for instituicao in instituicoes:
        instituicao.mostrar()

def mostrar_instituicao():
    try:
        codigo = int(input("Qual o código da instituição de ensino: "))
        instituicao = mostrar_instituicao_por_codigo(codigo)
        if instituicao:
            instituicao.mostrar_por_codigo()
        else:
            print("Instituição de ensino não encontrada.")

    except ValueError:
        print("Erro: Insira um código válido.")