# DESAFIO 05 - Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
# Condições Necessárias: 
# a + b > c
# a + c > b
# b + c > a

reta_A = int(input("Digite o tamanho da reta A: "))
reta_B = int(input("Digite o tamanho da reta B: "))
reta_C = int(input("Digite o tamanho da reta C: "))

soma_AB = reta_A + reta_B
soma_AC = reta_A + reta_C
soma_BC = reta_B + reta_C

if soma_AB > reta_C and soma_AC > reta_B and soma_BC > reta_A:
    print("Foi possível formar o triângulo.")
else:
    print("Não foi possível formar o triângulo.")