import pyautogui

#loop para fazer o mouse repetir em forma de quadrado

for i in range(10):
    pyautogui.moveTo(100 + 10 * i,100 + 10 * i, duration=0.25)
    pyautogui.moveTo(200 + 10 * i,100 + 10 * i, duration=0.25)
    pyautogui.moveTo(200 + 10 * i,200 + 10 * i, duration=0.25)
    pyautogui.moveTo(100 + 10 * i,200 + 10 * i, duration=0.25)

