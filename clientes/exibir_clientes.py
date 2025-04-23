from config.utils import *
from config.utils import carregar_clientes

def exibir_clientes():
    clientes = carregar_clientes()
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return

    exibir_titulo("Clientes Cadastrados")
    for i, cliente in enumerate(clientes, start=1):
        print(f"Cliente {i}:")
        print(f"Nome: {cliente['nome']}")
        print(f"E-mail: {cliente['email']}")
        print(f"Telefone: {cliente['telefone_formatado']}")
        print(f"CPF: {cliente['cpf_formatado']}")
        print("-" * 50)