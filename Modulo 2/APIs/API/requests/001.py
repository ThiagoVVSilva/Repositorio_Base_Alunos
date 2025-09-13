# 1 instalamos o rrequests com o comando do terminal: pip install resquests
# 2 importamos o requests para o nosso arquivo
import requests

res = requests.get("https://www.wikipedia.org")
print(res.status_code)# verificar o status da requisição
print(res.text[:500])#imprimir os primeiros 500 caracteres 