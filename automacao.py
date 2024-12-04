from basepandas import carregar_dados
import pyautogui   
import time


caminho_arquivo = r'C:/Users/Usuario/Desktop/Automaorder/teste.xlsx'

dados = carregar_dados(caminho_arquivo)

for index, row in dados.iterrows():
    

    pyautogui.PAUSE = 0.3
    #RPA - PEGAR POSIÇÕES DO MOUSE E DA TELA
    print(pyautogui.position())
    print(pyautogui.size())

    time.sleep(3)

    #RPA - FUNÇÕES DO MOUSE
    time.sleep(0.5)
    pyautogui.click(x=1612, y=104)

    #codigo do produto
    pyautogui.write(str(row['codigo']))
    pyautogui.press('down')

    # transferencia
    pyautogui.click(x=1879, y=463)

    # quantidade de pedido
    pyautogui.write(str(row['quantidade']))
    pyautogui.press('down')

    #clica no produto
    pyautogui.click(x=1574, y=347)


 