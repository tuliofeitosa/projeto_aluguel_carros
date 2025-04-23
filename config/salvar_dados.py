import json
import os

CAMINHO_CLIENTES = "config/dados/arquivos/clientes_db.txt"
CAMINHO_CARROS = "config/dados/arquivos/carros_db.txt"
def salvar_cliente(nome, email, telefone_formatado, cpf_formatado):
    cliente = {
        "nome": nome,
        "email": email,
        "telefone_formatado": telefone_formatado,
        "cpf": cpf_formatado
    }

    if os.path.exists(CAMINHO_CLIENTES):
        with open(CAMINHO_CLIENTES, "r", encoding="utf-8") as arquivo:
            try:
                clientes = json.load(arquivo)
            except json.JSONDecodeError:
                clientes = []
    else:
        clientes = []

    clientes.append(cliente)

    with open(CAMINHO_CLIENTES, "w", encoding="utf-8") as arquivo:
        json.dump(clientes, arquivo, indent=4, ensure_ascii=False)

def salvar_carro(marca, modelo, ano, cor, valor_diaria, placa, disponibilidade):
    carro = {
        "marca": marca,
        "modelo": modelo,
        "ano": ano,
        "cor": cor,
        "valor_diaria": valor_diaria,
        "placa": placa,
        "disponibilidade": disponibilidade
    }

    if os.path.exists(CAMINHO_CARROS):
        with open(CAMINHO_CARROS, "r", encoding="utf-8") as arquivo:
            try:
                carros = json.load(arquivo)
            except json.JSONDecodeError:
                carros = []
    else:
        carros = []

    carros.append(carro)

    with open(CAMINHO_CARROS, "w", encoding="utf-8") as arquivo:
        json.dump(carros, arquivo, indent=4, ensure_ascii=False)

import json

def salvar_carros(lista_carros):
    with open(CAMINHO_CARROS, "w", encoding="utf-8") as arquivo:
        json.dump(lista_carros, arquivo, indent=4, ensure_ascii=False)

