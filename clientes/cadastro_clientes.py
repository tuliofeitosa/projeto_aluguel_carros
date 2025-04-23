from config.utils import *
from config.salvar_dados import salvar_cliente

def cadastro_clientes():
    while True:
        nome = input("Digite o nome do cliente: ").strip()
        if nome:
            break
        else:
            print("Nome não pode ser vazio.")
    
    while True:
        email = input("Digite o e-mail do cliente: ").strip()
        if validacao_email(email):
            break
        else:
            print("E-mail inválido. Tente novamente.")
    
    while True:
        telefone = input("Digite o telefone do cliente: ").strip()
        if validacao_telefone(telefone):
            break
        else:
            print("Telefone inválido. Tente novamente.")
    telefone_formatado = formatar_telefone(telefone)
    
    while True:
        cpf = input("Digite o CPF do cliente: ").strip()
        if validacao_cpf(cpf):
            break
        else:
            print("CPF inválido. Tente novamente.")
    limpar_tela()
    salvar_cliente(nome, email, telefone_formatado, cpf)
