# DESAFIO 02 - Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

inicio = 0
fim = 51
salto = 2

for pares in range (inicio, fim, salto):
    print(pares)
else:
    print("Acabou")