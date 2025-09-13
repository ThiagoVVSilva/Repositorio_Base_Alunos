numero = int(input("Digite um número inteiro positivo: "))

raiz = numero ** 0.5
print(f"raiz quadrada de {numero} é: {raiz:.2f}:")

print(f"Divisibilidade de {numero}")
for divisor in range(2, 10):
    if numero % divisor == 0:
        print(f"{numero} é divisivel por {divisor}")
    else:
        print(f"{numero} não é divisivel por {divisor}") 