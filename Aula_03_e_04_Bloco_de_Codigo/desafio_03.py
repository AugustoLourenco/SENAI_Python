# DESAFIO 03 - Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem cobrando R$ 0,50 por Km para viagens de até 200 Km e R$ 0,45 para viagens mais longas.

print("Este é um programa que calcula o preço de uma passagem baseada nos quilômetros da viagem desejada")
distancia_usuario = int(input("Por favor, digite a distância a ser percorrida: "))
distancia_maxima = 200
acima_200 = 0.45
abaixo_200 = 0.50

if distancia_usuario > distancia_maxima:
    valor_acima = distancia_usuario * acima_200
    print (f"Para uma viagem de {distancia_usuario} km, o valor cobrado é de R${valor_acima}")
    
else :
    valor_abaixo = distancia_usuario * abaixo_200
    print (f"Para uma viagem de {distancia_usuario} km, o valor cobrado é de R${valor_abaixo}")