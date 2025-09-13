import pyautogui
import webbrowser
import time

#passo 1: abrir o yt com uma musica especifica

url = "https://www.youtube.com/watch?v=HyHNuVaZJ-k&list=RDHyHNuVaZJ-k&start_radio=1"
webbrowser.open(url)

#passo 2:aguardar o carregamento da pagina

time.sleep(5) #ajustar de acordo com a velo da internet utilizada

#passo 3 : garantir q o video comece (apertar o space para o play)
#pyautogui.press("space") #toca o video