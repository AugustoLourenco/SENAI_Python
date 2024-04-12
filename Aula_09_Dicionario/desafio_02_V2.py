from random import *
from time import *
from operator import *

dicionario = {
    "Jogador 1" : randint(1,6),
    "Jogador 2" : randint(1,6),
    "Jogador 3" : randint(1,6),
    "Jogador 4" : randint(1,6)
}

for k, v in dicionario.items():
    print(f"{k} tirou {v} no dado.")
    sleep(1)
    
# sorted(iterable, key=key, reverse=reverse)
# sorted(quem, qual a chave, quer inverter)

ranking = sorted(dicionario.items(), key=itemgetter(1), reverse=True)
print(ranking)
print(f"O vencedor é o {ranking[0][0]}! Ele tirou {ranking[0][1]} no dado.")

for i, v in enumerate(ranking):
    print(f"{i+1}º lugar: {v[0]} com {v[1]}")
    sleep(1)