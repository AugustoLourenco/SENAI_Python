# DESAFIO 04 - Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitorias consecutivas que ele conquistou no final do jogo. 

from random import *

opcoes = ["PAR", "ÍMPAR"]

vitorias = 0

while True:

    # Escolha Máquina
    escolha_maquina = choice(opcoes)
    numero_maquina = randint (0,10)
    print(f"A máquina escolheu {escolha_maquina}")

    # Escolha Usuário
    escolha_usuario = input("Escolha Par ou Ímpar: ").upper()
    numero_usuario = int(input("Escolha um número de 0 a 10: "))
    
    soma = numero_maquina + numero_usuario
    
    par_ou_impar = soma % 2
    

    if par_ou_impar == 0 and escolha_usuario == "PAR":
        print(f"Você ganhou! {soma} é par!")
        vitorias = vitorias + 1
    elif par_ou_impar == 1 and escolha_usuario == "ÍMPAR":
        print(f"Você ganhou! {soma} é ímpar!")
        vitorias = vitorias + 1
    elif par_ou_impar == 0 and escolha_maquina == "PAR":
        print(f"Você perdeu! {soma} é par!")
        break
    elif par_ou_impar == 1 and escolha_maquina == "ÍMPAR":
        print(f"Você perdeu! {soma} é ímpar!")
        break
    else:
        print("A opção está incorreta")
        continue
print(f"Você ganhou {vitorias} seguidas.")