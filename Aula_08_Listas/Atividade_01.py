# DESAFIO 01 - Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []
maior = 0
menor = 0
inicio = 1
fim = 6
salto = 1

for elemento in range (inicio, fim, salto):
    
    numero_usuario = int(input(f"Digite o {elemento}º número: "))
    lista.append(numero_usuario)
    
    maior = max(lista)
    menor = min(lista)
    
print(f"O maior valor digitado foi: {maior}. Ele ocupa a {lista.index(maior)+1}ª posição na lista")
print(f"O menor valor digitado foi: {menor}. Ele ocupa a {lista.index(menor)+1}ª posição na lista") 