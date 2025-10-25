#atividade sobre pyautogui
#abra a calculadora e execute uma equação
import pyautogui
import time 

pyautogui.hotkey('win', 'r')
pyautogui.write("calc")
pyautogui.press("Enter")
time.sleep(1)
pyautogui.write("1+1=")
pyautogui.press("Enter")
time.sleep(3)   
pyautogui.moveTo(330,50)
pyautogui.click()