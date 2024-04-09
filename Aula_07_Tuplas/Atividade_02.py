# DESAFIO 02 - Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na Tupla.

from random import *

for elemento in range (1, 6):

    numero_aleatorio = randint(0,20)
    print(numero_aleatorio)
    
    tupla_aleatoria = tuple(numero_aleatorio)
    print("Tupla aleatória: ", tupla_aleatoria)     