# DESAFIO EXTRA 4 - Crie um programa para entrar com a base e a altura de um retângulo e imprimir respectivamente o perímetro e a área correspondente.

base_retangulo = float(input("Digite o valor da base do retângulo: "))
altura_retangulo = float(input("Digite o valor da altura do retângulo: "))

soma_base = base_retangulo * 2
soma_altura = altura_retangulo * 2
perimetro_retangulo = soma_base + soma_altura

area_retangulo = base_retangulo * altura_retangulo

print(f"O Perímetro do retângulo é: {perimetro_retangulo}")
print(f"A Área do retângulo é: {area_retangulo}")