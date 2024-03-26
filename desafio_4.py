# DESAFIO 04 - Desenvolva um programa que leia as duas notas de um aluno, calcule e mostra a sua média.
nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))

nota_soma = nota1 + nota2
nota_media = nota_soma / 2

print(f"As notas do aluno são: {nota1} e {nota2}")
print(f"Sua nota média é: {nota_media}")