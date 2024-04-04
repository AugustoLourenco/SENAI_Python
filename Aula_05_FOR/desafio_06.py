# DESAFIO 06 - Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

inicio = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
fim = (inicio + (10 - 1) * razao) + 1

for pa in range (inicio, fim, razao):
    print(pa, end=" - ")
else:
    print("FIM")