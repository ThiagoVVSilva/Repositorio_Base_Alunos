import json


dados = {
    "nome":"maria",
    "idade":30,
    "cursos":["Python", "Machine Learning"]
}

 # criar um arquivo json e escrever dentro dele
with open('dados.json','w',encoding='utf-8') as arquivo: #W é o modo para escrever, encoding é para ortografia utilizar os caracteres especiais
    json.dump(dados,arquivo,  indent=4, ensure_ascii=False) #json.dump converte um dicionario em json