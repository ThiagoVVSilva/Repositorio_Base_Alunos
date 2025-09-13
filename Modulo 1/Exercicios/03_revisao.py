escolha = input("Digite 'C' para converter de Fahrenheit para Celsius ou 'F' para converter de Celsius para Fahrenheit: ").upper()

if escolha == 'C' : 
    temp = float(input("digite a temperatura em Fahrenheit"))
    resultado = (temp - 32) * 5/9
    print(f"{temp}°F equivale a {resultado:.1f}°C")
elif escolha == 'F' : 
    temp = float(input("Digite a temperatura em Celcius: "))
    resultado = temp * 9/5 + 32
    print(f"{temp}°F equivale a {resultado:.1f}°F")
else:
    print("Opção invalida.")