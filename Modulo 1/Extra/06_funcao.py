n = int(input("Digite um numero: "))
def par_impar(n):
    if n % 2 == 0:
        return"par"
    else:
        return"impar"
print(par_impar(n))