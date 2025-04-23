from config.utils import *
from funcionarios.login_funcionario import login_funcionario
from carros.cadastro_carros import cadastro_carro
from carros.edicao_carros import edicao_menu
from carros.exibir_carros import exibir_carros
from carros.exclusao_caros import excluir_carro

def menu_principal():
    while not login_funcionario():
        limpar_tela()
        print("Login inválido. Tente novamente.")
    while True:
        print("Menu Principal")
        print("1. Cadastrar Carro")
        print("2. Editar Carro")
        print("3. Excluir Carro")
        print("4. Exibir Carros")
        print("5. Sair")
        opcao = input("Digite a opção desejada: ")
        if opcao == "1":
            cadastro_carro()
        elif opcao == "2":
            edicao_menu()
        elif opcao == "3":
            excluir_carro()
        elif opcao == "4":
            exibir_carros()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu_principal()

