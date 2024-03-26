# DESAFIO EXTRA 4 - Crie um programa para entrar com a base e a altura de um retângulo e imprimir respectivamente o perímetro e a área correspondente.

base_retangulo = float(input("Digite o valor da base do retângulo: "))
altura_retangulo = float(input("Digite o valor da altura do retângulo: "))

perimetro_retangulo = (base_retangulo * 2) + (altura_retangulo * 2)

area_retangulo = base_retangulo * altura_retangulo

print(f"O Perímetro do retângulo é: {perimetro_retangulo}")
print(f"A Área do retângulo é igual a {area_retangulo}")