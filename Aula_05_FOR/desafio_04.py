# DESAFIO 04 - Mostre a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

numero = int(input("Digite um número: "))

for elemento in range (1, 11, 1):
    print(f"{numero} x {elemento} = {numero * elemento}")