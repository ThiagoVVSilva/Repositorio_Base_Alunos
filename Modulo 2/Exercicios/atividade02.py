import pyautogui

pyautogui.hotkey("win","r") #clica em varias teclas ao msm tempo
pyautogui.write("chrome") #ele escreve o que e pedido
pyautogui.press("Enter") #ele clica uma tecla individual
pyautogui.sleep(1) #espera o tempo colocado
pyautogui.moveTo(190,60) #ele move o mouse
pyautogui.click() #ele clica no mouse
pyautogui.write("youtube.com")
pyautogui.press("Enter")
pyautogui.sleep(3)
pyautogui.moveTo(900,150)
pyautogui.click()
pyautogui.write("i'm still standing")
pyautogui.press("Enter")
pyautogui.sleep(2)
pyautogui.moveTo(600,600)
pyautogui.click()

#ele vai para youtube sem o uso de url e pesquisa uma musica (eu sei ir por url tbm pq a professora é incrivel)