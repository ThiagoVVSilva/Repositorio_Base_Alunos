def calcular_bebida(convidados,consumo_por_pessoa_ml=800, volume_garrafa_litro=2.25):
    total_ml = convidados * consumo_por_pessoa_ml
    total_litros = total_ml/1000

    garrafas = int(total_litros//volume_garrafa_litro)
    if total_litros % volume_garrafa_litro > 0:
        garrafas += 1
    return total_litros, garrafas

def calcular_carne(convidados, consumo_por_pessoa_gramas=400):
    total_gramas = convidados * consumo_por_pessoa_gramas
    total_kg = total_gramas /1000
    return total_kg 

convidados = int(input("Digite o número de convidados: "))

litros, garrafas = calcular_bebida(convidados)
carne_kg = calcular_carne(convidados)

print("\n====Quantidade Total para o Churrasco====")
print(f"Número de convidados: {convidados}.")
print(f"Refrigerantes necessários: {litros:.2f} Litros.")
print(f"Garrafas de 2,25L: {garrafas} unidades")
print(f"Carne necessaria: {carne_kg:.2f} kg.")