# DESAFIO 02 - Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na Tupla.

from random import *

n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print('Os valores sorteados foram: ', end='')

for numeros in n:
    print(f"{numeros}", end=' ')

print(f"\nO maior valor sorteado foi {max(n)}")
print(f"O menor valor sorteado foi {min(n)}")