import requests #1. Definir chave de API

api_key ='2a1ac38a32354cb7b19133643251408'
cidade = input('Digite o nome da cidade: ').strip()
url = f'https://api.weatherapi.com/v1/current.json'

#2. Parametros da requisão
parametros ={
    'key':api_key,
    'q':cidade,
    'lang':'pt' #define a lingua da resposta como portugue
}
#3. Fazer a requesisão
resposta = requests.get(url, params=parametros)

#4. verificar se a requisisão
if resposta.status_code == 200:
    dados = resposta.json()
    temperatura = dados['current']['text']
    print(f'Temperatura na cidade {cidade}é {temperatura}°C.')
    print(resposta.content)