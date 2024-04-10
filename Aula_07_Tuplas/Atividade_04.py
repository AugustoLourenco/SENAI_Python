# DESAFIO 04 - Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram o números pares.

inicio = 1
fim = 5
salto = 1

minha_lista = []
minha_lista_pares = []

for i in range (inicio, fim, salto):
    numeros = int(input(f"Digite o sei {i}º numero: "))
    minha_lista.append(numeros)
    
    resto = numeros % 2
    if resto == 0:
        minha_lista_pares.append(numeros)

minha_tupla = tuple(minha_lista)
quantidade_nove = minha_tupla.count(9)
posicao3 = minha_tupla.index(3)
numeros_pares = tuple(minha_lista_pares)

print(quantidade_nove)
print(posicao3+1)
print(numeros_pares)