import json #Lendo um arquivo do tipo json
#sempre iniciamos com a importação do json ou da bibioteca que utilizaresmos
# abriremos o arquivo e o modo "r" lê esse arquivo

with open("dados.json","r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo) # esse método json.load converte o conteudo do arquivo json em um dicionario
print(dados)
print(type(dados))