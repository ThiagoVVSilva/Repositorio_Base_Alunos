alunos = [
    {"nome":"João",  "idade":20,"nota":8.5},
    {"nome":"Maria",  "idade":18,"nota":9.2},
    {"nome":"Pedro", "idade":19,"nota":9.8},
    {"nome": "Ana",  "idade":21,"nota":9.0}
    ]

total_notas = 0
quantidade_alunos = len(alunos)

for aluno in alunos:
    total_notas += aluno["nota"]
media_notas = total_notas/quantidade_alunos
print(f"A media das notas dos alunos é {media_notas:.2f}")
