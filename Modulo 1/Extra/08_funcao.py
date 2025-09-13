altura = float(input("Digite a altura (CM): "))
largura = float(input("Digite a Altura em (CM):"))
profundidade = float(input("Digite a profundidade em (CM): "))

def calcular_volume_cm3(altura,largura, profundidade):
    return altura * largura * profundidade

volume_cm3 = calcular_volume_cm3(altura,largura,profundidade)

print(f"\nAs medidas do Aquario são: ")
print(f"Altura: {altura} cm")
print(f"Largura: {largura} cm")
print(f"Profundidade: {profundidade} cm")
print(f"Portanto, seu volume é {volume_cm3:.2f} cm3 ou b({volume_cm3/1000:.2f} Litros.)")
