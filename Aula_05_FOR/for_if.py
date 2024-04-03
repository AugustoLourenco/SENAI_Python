from random import randint

maquina = 0
usuario = 0

for elemento in range (1, 11):
    numero_aleatorio = randint(0,5)
    numero_usuario = int(input(f"{elemento}º Rodada. Digite um numero: "))
    
    if numero_usuario == numero_aleatorio:
        print("Você acertou!")
        usuario = usuario + 1
    else:
        print("Você errou!")
        maquina = maquina + 1
else:
    
    if usuario > maquina:
        print("Você venceu!")
    elif usuario == maquina:
        print("Empate!")
    else:
        print("A máquina venceu!")      