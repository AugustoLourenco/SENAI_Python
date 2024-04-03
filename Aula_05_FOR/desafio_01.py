# DESAFIO 01 - Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0, com uma pausa de 1 segundo entre eles. 

import time

inicio = 10
fim = -1
salto = -1

for contagem_regressiva in range (inicio, fim, salto):
    print(contagem_regressiva)
    time.sleep(1)
else:
    print("KABUM!")