# DESAFIO 03 - Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na sua posição correta de inserção (sem usar o sort()). 
# No final mostre a lista ordenada na tela 

lista = []

for elemento in range (1, 6):

    numero_usuario = int(input(f"Digite o {elemento}º número: "))
    lista.append(numero_usuario)