letra = "s"

while letra == "s":

    nome  = input("Digite o nome do aluno: ")
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceiro nota: "))
    soma = n1 + n2 + n3 
    media = soma / 3

    print(f"A media do aluno(a) {nome} é {round(media,2)}.")
    if media >= 7 :
        print(f"Aluno(a) :{nome} está aprovado(a).")
    elif media > 3:
        print(f"Aluno(a) : {nome} está de recuperação.")
    else:
        print(f"Aluno(a): {nome} está reprovado(a).")
        letra = input("deseja continuar? (s/n): ").strip().lower()