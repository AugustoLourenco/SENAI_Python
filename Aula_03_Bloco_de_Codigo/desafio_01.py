# DESAFIO 01 - Escreva um programa que faça o computador “pensar” em um número inteiro entre 5 e 0 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
# from random import * = Importar toda a biblioteca

print("Este é um jogo que te desafia a adivinhar um número aleatório de 0 a 5")

numero_aleatorio = randint(0,5)
numero_usuario = int(input("Tente adivinhar qual número o computador escolheu: "))

if numero_usuario == numero_aleatorio :
    print("Parabéns! Você venceu.")
else :
    print(f"Não foi dessa vez! O número escolhido foi {numero_aleatorio}")