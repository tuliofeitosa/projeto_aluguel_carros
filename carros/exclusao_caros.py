from config.utils import *
from config.salvar_dados import salvar_carros
from carros.exibir_carros import exibir_carros

def excluir_carro():
    limpar_tela()
    exibir_titulo("Exclusão de Carros")
    while True:
        carros = carregar_carros()

        if not carros:
            print("Nenhum carro cadastrado.")
            return

        exibir_carros()

        try:
            escolha = int(input("Digite o número do carro que deseja excluir: "))
            if 1 <= escolha <= len(carros):
                carro_excluido = carros[escolha - 1]
                confirmacao = input(
                    f"Você tem certeza que deseja excluir o carro {carro_excluido['placa']}?\n1. Sim\n2. Não\nDigite a opção: "
                ).strip()

                if confirmacao == '1':
                    carros.pop(escolha - 1)
                    salvar_carros(carros)
                    print(f"Carro com placa {carro_excluido['placa']} excluído com sucesso.")
                elif confirmacao == '2':
                    print("Exclusão cancelada.")
                else:
                    print("Opção inválida. Exclusão cancelada.")
            else:
                print("Número inválido.")
        except ValueError:
            print("Entrada inválida.")

        repetir = input("\nDeseja excluir mais um carro?\n1. Sim\n2. Não\nDigite a opção: ").strip()
        if repetir != '1':
            break