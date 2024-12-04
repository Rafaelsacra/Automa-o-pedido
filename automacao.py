import pyautogui   
import time

pyautogui.PAUSE = 0,3
#RPA - PEGAR POSIÇÕES DO MOUSE E DA TELA
print(pyautogui.position())
print(pyautogui.size())

#RPA - FUNÇÕES DO MOUSE
time.sleep(5)
pyautogui.press('insert')

#codigo do produto
pyautogui.write(123)
pyautogui.press('down')

# transferencia
pyautogui.click(x=1605, y=105)

# quantidade de pedido
pyautogui.write(50)
pyautogui.press('down')

#clica no produto
pyautogui.click(x=1605, y=105)


 