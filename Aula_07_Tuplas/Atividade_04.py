# DESAFIO 04 - Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram o números pares.

inicio = 1
fim = 5
salto = 1

for elemento in range (inicio, fim, salto):
    numero_usuario = int(input(f"Digite o {elemento}º número: "))
print(numero_usuario)