#escreveer txt automaticamente

import pyautogui
import time
#abra um bloco de notas numa pagina em branco
#aguarde 5 s para vc abrir o bloco de notas
time.sleep(5)

#escrever o txt
pyautogui.write("Automatizacao com pyautogui", interval=0.1)