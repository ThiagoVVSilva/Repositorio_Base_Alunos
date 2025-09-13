def verificar_voto(ano_nasc):
    ano_atual = 2025
    idade = ano_atual - ano_nasc
    if idade < 16:
        return idade, "Negado"
    elif idade < 18 or idade >70:
        return idade, "Opcional"
    else:
        return idade, "Obrigatorio"

ano = int(input("Digite seu ano de nascimento: "))
idade, tipo_voto = verificar_voto(ano)
print(f"Idade: {idade} anos - voto: {tipo_voto}")
