# DESAFIO 01 - Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostra-lo por extenso.

contagem = 'ZERO', 'UM', 'DOIS', 'TRES', 'QUATRO', ' CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ', 'ONZE', 'DOZE', 'TREZE', 'QUATORZE', 'QUINZE', 'DEZESSEIS', 'DESESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE'

while True:

    numero_usuario = int(input("Digite um número: "))
    numero_extenso = contagem[numero_usuario]
    print(numero_extenso)
    
    if numero_usuario < 0 or numero_usuario > 20:
        break
print("Digite um número de 0 a 20!") 
