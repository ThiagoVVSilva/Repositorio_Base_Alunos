n1 = float(input("Digite o primeiro número: "))
n2 = float(input("digite o segundo número"))

soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2

print(f"soma: {soma}")
print(f"subtração: {subtracao}")
print(f"multiplicação {multiplicacao}")

if n2 != 0:
    divisao = n1/n2
    print(f"Divisão:{divisao:.2f}")
else:
    print("Não existe divisão de número negatiovo!")