from config.utils import *
from config.salvar_dados import salvar_carro

def cadastro_carro():
    limpar_tela()
    exibir_titulo("Cadastro de Carros")
    while True:
        marca = input("Digite a marca do carro: ").strip()
        if marca:
            break
        else:
            print("Marca não pode ser vazia. Tente novamente.")
    while True:
        modelo = input("Digite o modelo do carro: ").strip()
        if modelo:
            break
        else:
            print("Modelo não pode ser vazio. Tente novamente.")
    while True:
        ano = input("Digite o ano do carro (ex: 2020): ").strip()
        if ano.isdigit() and len(ano) == 4:
            break
        else:
            print("Ano inválido. Tente novamente.")
    while True: 
        cor = input("Digite a cor do carro: ").strip()
        if cor:
            break
        else:
            print("Cor não pode ser vazia. Tente novamente.")
    while True:
        valor_diaria = float(input("Digite o valor da diária do carro: "))
        if valor_diaria:
            break
        else:
            print("Valor não pode estar vazio. Tente novamente")
    while True:
        placa = input("Digite a placa do carro (ex: ABC1D23): ").strip()
        if validacao_placa(placa):
            break
        else:
            print("Placa inválida. Tente novamente.")
    disponibilidade = 1
    limpar_tela()
    salvar_carro(marca, modelo, ano, cor, valor_diaria, placa, disponibilidade)