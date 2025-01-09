import pandas as pd
from basepandas import carregar_dados
import pyautogui   
import time

# Lista de arquivos Excel
arquivos = [
    "frios2.xlsx", "frios4.xlsx", "frios5.xlsx", "frios7.xlsx", "frios8.xlsx",
    "cond2.xlsx", "cond4.xlsx", "cond5.xlsx", "cond7.xlsx", "cond8.xlsx"
]

# Função para carregar dados de um arquivo Excel e executar automação
def executar_automacao(caminho_arquivo):
    dados = carregar_dados(caminho_arquivo)
    for index, row in dados.iterrows():
        pyautogui.PAUSE = 0.3
        print(pyautogui.position())
        print(pyautogui.size())
        time.sleep(2)

        pyautogui.click(x=1612, y=104)

    #codigo do produto
        codigo = row['codigo']
        pyautogui.write(str(codigo))
        pyautogui.press('down')

        if codigo == 0:
            print("Código zero encontrado. Parando o PyAutoGUI.")
            break

            # transferencia
        pyautogui.click(x=1978, y=477)

        # quantidade de pedido
        pyautogui.write(str(row['quantidade']))
        pyautogui.press('down')

        #clica no produto
        pyautogui.click(x=1574, y=347)

# Menu interativo
def menu_arquivos():
    while True:
        print("\nMenu de Arquivos Excel")
        for i, arquivo in enumerate(arquivos, start=1):
            print(f"{i}. {arquivo}")
        print("0. Sair")

        try:
            opcao = int(input("\nEscolha um arquivo para executar a automação (ou 0 para sair): "))

            if opcao == 0:
                print("Encerrando o programa.")
                break

            if 1 <= opcao <= len(arquivos):
                caminho_arquivo = f"C:/Users/Usuario/Desktop/Automaorder/{arquivos[opcao - 1]}"
                executar_automacao(caminho_arquivo)
            else:
                print("Opção inválida. Tente novamente.")

        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

# Executa o menu
menu_arquivos()

  


 