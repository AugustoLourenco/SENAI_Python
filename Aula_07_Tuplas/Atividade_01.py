# DESAFIO 01 - Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostra-lo por extenso.

contagem = 'ZERO', 'UM', 'DOIS', 'TRES', 'QUATRO', ' CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ', 'ONZE', 'DOZE', 'TREZE', 'QUATORZE', 'QUINZE', 'DEZESSEIS', 'DESESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE'

while True:

    numero_usuario = int(input("Digite um número: "))
    numero_extenso = contagem[numero_usuario]
    
    if numero_usuario >= 0 and numero_usuario <= 20:
        print(f"Você digitou o número {numero_extenso}!") 
    else:
        break
print("Tente novamente: ")
    