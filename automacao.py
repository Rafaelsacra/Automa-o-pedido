import pandas as pd
from basepandas import carregar_dados
import pyautogui   
import time

# Lista de arquivos Excel
arquivos = [
    "frios2.xlsx", "frios4.xlsx", "frios5.xlsx", "frios7.xlsx", "frios8.xlsx",
    "cond2.xlsx", "cond4.xlsx", "cond5.xlsx", "cond7.xlsx", "cond8.xlsx"
]

caminho_arquivo = r'C:/Users/Usuario/Desktop/Automaorder/frios8.xlsx'

dados = carregar_dados(caminho_arquivo)

for index, row in dados.iterrows():
    

    pyautogui.PAUSE = 0.3
    #RPA - PEGAR POSIÇÕES DO MOUSE E DA TELA
    print(pyautogui.position())
    print(pyautogui.size())

    time.sleep(2)

    #RPA - FUNÇÕES DO MOUSE
    time.sleep(0.5)
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

  


 