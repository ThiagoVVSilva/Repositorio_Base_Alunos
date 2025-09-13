nome_excluir = input("Nome a excluir:  ")

with open("pessoa.txt", "r") as arquivo:
    linhas = arquivo.readlines()

with open("pessoa.txt", "w")as arquivo:
    for linha in linhas:
        if nome_excluir not in linha:
            arquivo.write(linha)