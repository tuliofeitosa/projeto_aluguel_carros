from config.utils import *
from config.salvar_dados import salvar_carro
from carros.exibir_carros import exibir_carros
from config.utils import carregar_carros
from config.salvar_dados import salvar_carros

def selecionar_carro():
    carros = carregar_carros()

    if not carros:
        print("Nenhum carro cadastrado.")
        return None, None, []

    exibir_carros()

    try:
        escolha = int(input("Digite o número do carro que deseja editar: "))
        if 1 <= escolha <= len(carros):
            return escolha - 1, carros[escolha - 1], carros
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")
    
    return None, None, carros

def edicao_marca(carro):
    print(f"Marca atual: {carro['marca']}")
    nova_marca = input("Digite a nova marca (ou pressione Enter para manter a atual): ")
    if nova_marca:
        carro['marca'] = nova_marca
    return carro    

def edicao_modelo(carro):
    print(f"Modelo atual: {carro['modelo']}")
    novo_modelo = input("Digite o novo modelo (ou pressione Enter para manter o atual): ")
    if novo_modelo:
        carro['modelo'] = novo_modelo
    return carro

def edicao_ano(carro):
    print(f"Ano atual: {carro['ano']}")
    novo_ano = input("Digite o novo ano (ou pressione Enter para manter o atual): ")
    if novo_ano:
        try:
            carro['ano'] = int(novo_ano)
        except ValueError:
            print("Ano inválido.")
    return carro

def edicao_cor(carro):
    print(f"Cor atual: {carro['cor']}")
    nova_cor = input("Digite a nova cor (ou pressione Enter para manter a atual): ")
    if nova_cor:
        carro['cor'] = nova_cor
    return carro

def edicao_preco(carro):
    print(f"Valor de diária atual: {carro['preco']}")
    novo_preco = input("Digite o novo valor de diária (ou pressione Enter para manter o atual): ")
    if novo_preco:
        try:
            carro['preco'] = float(novo_preco)
        except ValueError:
            print("Preço inválido.")
    return carro

def edicao_placa(carro):
    print(f"Placa atual: {carro['placa']}")
    nova_placa = input("Digite a nova placa (ou pressione Enter para manter a atual): ")
    if nova_placa:
        if validacao_placa(nova_placa):
            carro['placa'] = nova_placa
        else:
            print("Placa inválida.")
    return carro

def edicao_menu():
    limpar_tela()
    exibir_titulo("Edição de Carros")
    indice, carro, carros = selecionar_carro()
    
    if carro is None:
        return
    
    while True:
        print("Escolha o que deseja editar:")
        print("1. Marca")
        print("2. Modelo")
        print("3. Ano")
        print("4. Cor")
        print("5. Preço")
        print("6. Placa")
        print("7. Retorna ao menu principal")
        print("8. Sair")
        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            carro = edicao_marca(carro)
        elif opcao == "2":
            carro = edicao_modelo(carro)
        elif opcao == "3":
            carro = edicao_ano(carro)
        elif opcao == "4":
            carro = edicao_cor(carro)
        elif opcao == "5":
            carro = edicao_preco(carro)
        elif opcao == "6":
            carro = edicao_placa(carro)
        elif opcao == "7":
            print("Retornando ao menu principal...")
            edicao_menu()
        elif opcao == "8":
            break
        else:
            print("Opção inválida.")
            continue

        carros[indice] = carro
        salvar_carros(carros)
        print("Carro atualizado com sucesso!")

        print(f"Deseja editar mais alguma coisa? \n1. Sim \n2. Não\nDigite a opção desejada: ")
        if opcao == "1":
            continue
        elif opcao == "2":
            break
        else:
            print("Opção inválida.")
            break