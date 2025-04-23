from config.utils import *

def exibir_carros ():
    limpar_tela()
    exibir_titulo("Exibição de Carros")
    carros = carregar_carros()
    if not carros:
        print("Nenhum carro cadastrado.")
        return
    
    exibir_titulo("Carros Cadastrados")
    for i, carro in enumerate(carros, start=1):
        print(f"Carro {i}:")
        print(f"Marca: {carro['marca']}")
        print(f"Modelo: {carro['modelo']}")
        print(f"Ano: {carro['ano']}")
        print(f"Cor: {carro['cor']}")
        print(f"Valor Diária: R$ {carro['valor_diaria']:.2f}")
        print(f"Placa: {carro['placa']}")
        print(f"Disponibilidade: {'Disponível' if carro['disponibilidade'] == 1 else 'Indisponível'}")
        print("-" * 50)