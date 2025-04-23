import re
import os
from config.salvar_dados import CAMINHO_CLIENTES, CAMINHO_CARROS
import json
    
def validacao_email(email):
    padrao = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(padrao, email):
        if '..' in email or email.endswith('.'):
            return False
        return True
    else:
        return False
    
def validacao_telefone(telefone):
    padrao = r'^\d{10,11}$'
    if re.match(padrao, telefone):
        return True
    else:
        return False

def validacao_cpf(cpf):
    padrao = r'^\d{11}$'
    if re.match(padrao, cpf):
        return True
    else:
        return False

def validacao_placa(placa):
    padrao = r'^[A-Z]{3}\d{1}[A-Z]{1}\d{2}$'
    if re.match(padrao, placa):
        return True
    else:
        return False

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_titulo(titulo):
    print("=" * 50)
    print(f"{titulo:^50}")
    print("=" * 50)

def formatar_telefone(telefone):
    if len(telefone) == 11:
        return f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"
    else:
        return f"({telefone[:2]}) {telefone[2:6]}-{telefone[6:]}" 

def formatar_cpf(cpf):
    if len(cpf) == 11:
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    else:
        return cpf

def carregar_funcionarios(caminho):
    funcionarios = []
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                partes = linha.strip().split(";")
                if len(partes) == 3:
                    usuario, senha, funcao = partes
                    funcionarios.append({
                        "usuario": usuario,
                        "senha": senha,
                        "funcao": funcao
                    })
    except FileNotFoundError:
        print("Arquivo de funcionários não encontrado.")
    return funcionarios

def carregar_funcionarios():
    caminho_arquivo = "config/dados/arquivos/funcionarios_db.txt"
    funcionarios = []

    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                partes = linha.strip().split(';')
                if len(partes) == 3:
                    usuario, senha, funcao = partes
                    funcionarios.append({
                        'usuario': usuario,
                        'senha': senha,
                        'funcao': funcao
                    })
    except FileNotFoundError:
        print("Arquivo de funcionários não encontrado.")
    
    return funcionarios

def carregar_carros():
    if os.path.exists(CAMINHO_CARROS):
        with open(CAMINHO_CARROS, "r", encoding="utf-8") as arquivo:
            try:
                return json.load(arquivo)
            except json.JSONDecodeError:
                return []
    return []

def carregar_clientes():
    if os.path.exists(CAMINHO_CLIENTES):
        with open(CAMINHO_CLIENTES, "r", encoding="utf-8") as arquivo:
            try:
                return json.load(arquivo)
            except json.JSONDecodeError:
                return []
    return []