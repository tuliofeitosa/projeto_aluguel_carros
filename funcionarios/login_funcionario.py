from config.utils import *
def login_funcionario():
    funcionarios = carregar_funcionarios()

    usuario_input = input("Usuário: ")
    senha_input = input("Senha: ")

    for funcionario in funcionarios:
        if funcionario['usuario'] == usuario_input and funcionario['senha'] == senha_input:
            print(f"Login realizado com sucesso! Bem-vindo(a), {usuario_input} ({funcionario['funcao']})")
            return funcionario['funcao']

    print("Usuário ou senha incorretos.")
    return None
