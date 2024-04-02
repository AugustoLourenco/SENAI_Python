from random import randint

numero_aleatorio = randint(0,5)
maquina = 0
usuario = 0

for elemento in range (1, 11):
    numero_usuario = int(input(f"{elemento}º Rodada. Digite um numero: "))
    
    if numero_usuario == numero_aleatorio:
        print("Você acertou!")
        usuario = usuario + 1
    else:
        print("Você acertou!")
        maquina = maquina + 1       