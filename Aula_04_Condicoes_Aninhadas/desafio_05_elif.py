# DESAFIO 05 - Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: Todos os lados iguais
# Isósceles: Dois lados iguais
# Escaleno: Todos os lados diferentes
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
    if reta_A == reta_B == reta_C:
        print(f"Os lados são: {reta_A}, {reta_B} e {reta_C}. Todos os lados são iguais. Triângulo Equilátero.")
    elif reta_A == reta_B or reta_B == reta_C or reta_A == reta_C:
        print(f"Os lados são: {reta_A}, {reta_B} e {reta_C}. Dois lados iguais. Triângulo Isósceles.")
    else:
        print(f"Os lados são: {reta_A}, {reta_B} e {reta_C}. Todos os lados diferentes. Triângulo Escaleno.")
else:
    print("Não foi possível formar o triângulo.")