# atividade de número primo
numero = int(input("Digite um número inteiro positivo: "))
if numero <= 1:
    print(f"{numero} não é primo.")
else:
    eh_primo = True
    for i in range(2, int(numero ** 0,5) + 1):
        if numero % i == 0:
            eh_primp = False
            break

if eh_primo:
    print(f"{numero} é primo.")
else:
    print(f"{numero} não é primo.")
