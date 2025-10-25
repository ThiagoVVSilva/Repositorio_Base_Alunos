import pyautogui
import time
#comando pára mover o mouse e clicar
#mover o mouse para a posição (100; 200)

pyautogui.moveTo(1200,2000, duration=1)
pyautogui.click()
pyautogui.moveTo(170,200, duration=1)
pyautogui.click()
pyautogui.write("Automatizacao com pyautogui", interval=0.1)
time.sleep(2)
pyautogui.moveTo(700,120, duration=1)
pyautogui.click()
