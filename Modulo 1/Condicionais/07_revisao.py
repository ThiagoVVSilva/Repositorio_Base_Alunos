valor1 = int(input("Digite a preimeira nota: "))
valor2 = int(input("Digite a segunda nota: "))
valor3 = int(input("Digite a terceira nota: "))

med = (valor1 + valor2 + valor3) /3

if med >= 7:
    print("sua nota é positiva :)")
elif  5 >= med < 7:
    print("recuperaçâo, mais sorte na proxima ;-;")
else:
    print("sua nota é negativa :(")

print(f"e a pontuação total é {med}")

