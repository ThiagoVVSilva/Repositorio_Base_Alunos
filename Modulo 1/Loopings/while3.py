letra = "s"

while letra == "s":
    n1 = float(input("Digite um número: "))
    n2 = float(input("digite a porcentagem que deseja descobrir: "))

    porcentagem = (n1*n2)/100

    print(f"{n2} % do número {n1} é igual a {porcentagem}.")

    a = input("deseja continuar? (s/n): ").strip().lower()