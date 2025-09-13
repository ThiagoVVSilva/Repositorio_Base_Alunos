nomes = ["Joaquim","Maria","Ana"]

print("lista inicial:",nomes)

nomes.append("Carlos")
print(nomes)

nomes.insert(1,"Fernanda")
print("Após insert,", nomes)

nomes[2]= "Marcos"
print(nomes)

nomes.remove("Marcos")
print(nomes)

removido = nomes.pop(2)
print(f"Ápos pop(removido '{removido}'):",nomes)

nomes.clear()
print("ápos clear:", nomes)