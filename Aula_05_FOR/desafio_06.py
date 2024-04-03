# DESAFIO 06 - Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

inicio = int(input("Digite o primeiro termo: "))
fim = inicio + 10
razao = int(input("Digite a razão: "))

for pa in range (inicio, fim, razao):
    print(pa)
else:
    print("FIM")