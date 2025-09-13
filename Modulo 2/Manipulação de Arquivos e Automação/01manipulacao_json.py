import json
#Convertendo um arquivo texto(string) em dicionario
# # Sting no formato Json, usar aspas duplas e os valores 
json_data = '{"nome","Ana","idade":30,"estudante":true}'

dados_python = json.loads(json_data) #lendo o arquivo

print(dados_python['nome']) # traz as informações armazenadas nas respectivas chaves
print(dados_python('idade'))
print(dados_python['estudante'])