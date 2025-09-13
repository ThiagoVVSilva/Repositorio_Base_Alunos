
nome = input("Digite seu nome:  ")
email = input("Digite seu email:  ")

with open("pessoa.txt","a") as arquivo:
    arquivo.write(nome + "  |  "+ email + "\n")