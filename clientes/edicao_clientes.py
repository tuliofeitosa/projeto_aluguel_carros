from config.utils import *
from config.salvar_dados import salvar_cliente
from clientes.exibir_clientes import exibir_clientes
from config.utils import carregar_clientes

def selecionar_cliente():
    clientes = carregar_clientes()

    if not clientes:
        print("Nenhum cliente cadastrado.")
        return None, None, []

    exibir_clientes()

    try:
        escolha = int(input("Digite o número do cliente que deseja editar: "))
        if 1 <= escolha <= len(clientes):
            return escolha - 1, clientes[escolha - 1], clientes
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")
    
    return None, None, clientes