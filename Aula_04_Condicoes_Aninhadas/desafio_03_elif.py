# DESAFIO 03 - Crie um programa que leia duas notas entre 0 a 10 de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida.
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 a 6.9: RECUPERAÇÃO
# Média igual ou superior a 7.0: APROVADO

nota_1 = float(input("Digite a nota da primeira prova: "))
nota_2 = float(input("Digite a nota da segunda prova: "))

if nota_1 <= 10.0 and nota_1 >= 0 and nota_2 >= 0 and nota_2 <= 10.0:

    nota_media = (nota_1+nota_2) / 2

    if nota_media >= 7.0:
        print(f"Aprovado! Média {nota_media}")
    elif nota_media >= 5.0:
        print(f"Recuperação! Média {nota_media}")
    else:
        print(f"Reprovado! Média {nota_media}")
else:
    print("Por favor informe uma nota válida")