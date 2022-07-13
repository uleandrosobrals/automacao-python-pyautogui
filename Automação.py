import pyautogui
import time
pyautogui.PAUSE = 1

#Abrir o navegador Chrome
pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(2)

#Acessar Portal Suporte Processos
pyautogui.write("http://")
pyautogui.press('enter')
# > Relatórios
pyautogui.click(x=2399, y=91)
pyautogui.mouseDown()
#>Vendas
pyautogui.click(x=2373, y=139)
pyautogui.mouseDown()
#>Lojas
pyautogui.moveTo(x=2517, y=197)
time.sleep(1)
pyautogui.click(clicks=2)

#Gerar Relatório
pyautogui.moveTo(x=2126, y=259)
pyautogui.click()

#Exportar
pyautogui.moveTo(x=2589, y=261)
pyautogui.click()
pyautogui.moveTo(x=2157, y=278)
pyautogui.click()
pyautogui.moveTo(x=2665, y=429)
pyautogui.click()

