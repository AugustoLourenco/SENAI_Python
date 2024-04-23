# DESAFIO 03

# Escreva um programa que solicite ao usuário para digitar um número inteiro e exiba o resultado da sua raiz quadrada. 
# Lide com o erro caso o número seja negativo.
from math import *

try:
    n1 = int(input("Entre com um número inteiro: "))
    raiz_quadrada = sqrt(n1)
    print(raiz_quadrada)
    
except ValueError:
    print("Favor inserir um número inteiro válido")
    
else:
    print(raiz_quadrada)