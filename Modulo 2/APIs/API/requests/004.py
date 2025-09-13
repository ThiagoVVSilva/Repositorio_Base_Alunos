import requests
from bs4 import BeautifulSoup

# 01 importe uma url
url = 'https://sp.senai.br/unidade/santanadeparnaiba'

# 02 fazer requisição do http
rpt = requests.get(url)
if rpt.status_code == 200:
    # 03 usar o beautifulsoup para interpretar o html
    soup = BeautifulSoup(rpt.text,'html.parser')
    # 04 encontre o titulo da pg
    titulo = soup.title.string
    # 05 imprimir o titulo
    print(f"o titulo da pagina é: {titulo}, o melhor do Brasil")
else:
    print("Erro ao acessar a pagina:",rpt.status_code)