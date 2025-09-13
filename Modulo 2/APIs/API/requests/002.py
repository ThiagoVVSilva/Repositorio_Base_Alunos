import requests # Importamos a biblioteca
res = requests.get("https://www.globo.com/")# criamos uma requisição requests
try:
    resultado = res.raise_for_status()# solicitamos o status da requisição
    print(res)# pedimos para imprimir o resultado
except Exception as exc:
    print("Há um problema: %s"% (exc))# indentificamos o erro