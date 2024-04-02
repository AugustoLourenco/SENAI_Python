# DESAFIO 06 - Crie um programa que faça o computador jogar Jokenpô com você: 

from random import choice

opcoes = ["PEDRA", "PAPEL", "TESOURA"]
escolha_maquina = choice(opcoes)

escolha_usuario = input("Informe a sua escolha: ").upper()

if escolha_usuario == escolha_maquina:
    print(f"Empate! Ambos escolheram {escolha_maquina}.")
elif escolha_maquina == "PEDRA" and escolha_usuario == "TESOURA":
    print(f"Você perdeu! A máquina escolheu {escolha_maquina}.")
elif escolha_maquina == "PEDRA" and escolha_usuario == "PAPEL":
    print(f"Você ganhou! A máquina escolheu {escolha_maquina}.")
elif escolha_maquina == "PAPEL" and escolha_usuario == "TESOURA":
    print(f"Você ganhou! A máquina escolheu {escolha_maquina}.")
elif escolha_maquina == "PAPEL" and escolha_usuario == "PEDRA":
    print(f"Você perdeu! A máquina escolheu {escolha_maquina}.")
elif escolha_maquina == "TESOURA" and escolha_usuario == "PEDRA":
    print(f"Você ganhou! A máquina escolheu {escolha_maquina}.") 
else:
    print(f"Você perdeu! A máquina escolheu {escolha_maquina}.")     