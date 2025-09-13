with open("pessoa.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        print(linha.strip())
  #ler linha por linha e mostra de forma listada