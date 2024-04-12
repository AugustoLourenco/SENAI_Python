# DESAFIO 02 - Crie um programa onde 4 jogadores joguem um dado e tenham resultado aleatórios. Guarde esses resultados em um dicionário. 
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior numero no dado.

from random import *

dicionario = {}
lista = list() # Podemos declarar lista dessa maneira

for c in range (1, 5):
    dicionario[f"Jogador {c}"] = randint (1,6)
    lista.append(dicionario.copy())

ordenado = dict(sorted(dicionario.items(), key=lambda item: item[1], reverse=True))   
print(ordenado)
print(ordenado[0])