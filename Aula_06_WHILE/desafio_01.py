# DESAFIO 01 - Faça um jogo, onde o computador vai “pensar” em um número entre 0 a 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no  final quantos palpites foram necessários para vencer.

from random import *

numero_aleatorio = randint(0,10)
tentativas = 0

while True:
    
    numero_usuario = int(input("Tente adivinhar qual número o computador escolheu: "))
    tentativas = tentativas + 1
    
    if numero_usuario == numero_aleatorio:
        print(f"Você acertou! O número escolhido foi o {numero_aleatorio}!")
        print(f"Você acertou na {tentativas}ª tentativa!")
        break
    print("Você errou! Tente novamente!")