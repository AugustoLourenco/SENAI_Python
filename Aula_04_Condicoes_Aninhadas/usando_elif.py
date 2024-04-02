prova = float(input("Digite a nota da prova entre 0 e 70: "))
atividade = float(input("Digite a média das notas das atividades entre 0 e 30: "))

# Prova = 70% da média final
# Atividade = 30% da média final

media_final = prova + atividade
print(media_final)

if media_final >= 50:
    print(f"Aprovado. Média final igual a {media_final}")
elif media_final >= 40:
    print(f"Recuperação. Média final igual a {media_final}")
else:
    print(f"Reprovado. Média final igual a {media_final}")