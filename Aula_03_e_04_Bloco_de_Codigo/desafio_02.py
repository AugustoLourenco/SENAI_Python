# DESAFIO 02 - Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada Km acima do limite.

velocidade = int(input("Por favor, digite a velocidade do veículo: "))
velocidade_permitida = 80
velocidade_ultrapassada = velocidade - velocidade_permitida
multa_por_km = 7

if velocidade > velocidade_permitida :
    multa_valor = velocidade_ultrapassada * multa_por_km
    print(f"Você foi multado! A sua velocidade foi de {velocidade} km/h!")
    print(f"Multa de R${multa_valor},00 pela infração.")
else :
    print(f"A sua velocidade foi de {velocidade} km/h. Tudo certo, boa viagem!")