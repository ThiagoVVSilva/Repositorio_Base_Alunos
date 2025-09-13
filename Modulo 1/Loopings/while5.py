letra = "s"
while letra == "s":
    cotacao = float(input("Digite a cotação do dolar usd: "))

    print("-"*50)
    print("-"*15, "escolha uma opção","-"*15)
    print("-"*50)

    opcao = int(input("1 - Converter dolar para real / 2 - Converter real para dolar: "))

    if opcao == 1:
        valor = float(input("digite o valor em dolar a ser convertido para real é R$  "))
        resultado = valor * cotacao 
        print(f"o valor em reais é R$ {resultado:.2f}.")
    elif opcao == 2:
        valor = float(input("Digite o valor em real a ser convertido para dolar é USD "))
        resultado = valor / cotacao
        print(f"o valor em dolar é  US {resultado:.2f}.")
    else:
        print("digite uma opÇão valida.")
    letra = input("Deseja continuar(s/n)? : ").strip().lower()