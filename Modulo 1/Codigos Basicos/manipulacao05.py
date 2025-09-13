busca = input("Digite o nome para buscar:  ")

with open("pessoa.txt", "r") as arquivo:
    encontrado = False 
    for linha in arquivo:
            if busca.lower() in linha.lower():
                 print("encontrado:", linha.strip())
                 encontrado = True
    if not encontrado:
        print("Nome não encontrado.")