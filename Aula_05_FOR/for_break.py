from random import *

numero_aleatorio = randint(1,20)
print(numero_aleatorio)
for elemento in range (1, 11):
    
    numero_usuario = int(input(f"{elemento}º Rodada. Digite um numero: "))
    
    if numero_usuario == numero_aleatorio:
        print("Você acertou!")
        break

else:
    print("A máquina venceu!")
    
print("GAME OVER")