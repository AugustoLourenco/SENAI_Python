# DESAFIO 02 - Escreva um programa que leia dois números inteiros e compare- os, mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

if n1 > n2:
    print(f"O primeiro número é maior. {n1} > {n2}")
elif n1 < n2: 
    print(f"O segundo número é maior. {n2} > {n1} ")
else:
    print(f"Os números são iguais. {n1} = {n2}")
