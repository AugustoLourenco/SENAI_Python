from random import choice

opcoes = ["PEDRA", "PAPEL", "TESOURA"]
valor = 0
valor_ficha = 5

while True:

    escolha_maquina = choice(opcoes)

    escolha_usuario = input("Informe a sua escolha: ").upper()
    print(f"O valor gasto foi R${valor}")

    if escolha_usuario == escolha_maquina:
        print(f"Empate! Ambos escolheram {escolha_maquina}.")
    elif escolha_maquina == "PEDRA" and escolha_usuario == "TESOURA":
        print(f"Você perdeu! A máquina escolheu {escolha_maquina}.")
    elif escolha_maquina == "PEDRA" and escolha_usuario == "PAPEL":
        print(f"Você ganhou! A máquina escolheu {escolha_maquina}.")
        break
    elif escolha_maquina == "PAPEL" and escolha_usuario == "TESOURA":
        print(f"Você ganhou! A máquina escolheu {escolha_maquina}.")
        break
    elif escolha_maquina == "PAPEL" and escolha_usuario == "PEDRA":
        print(f"Você perdeu! A máquina escolheu {escolha_maquina}.")
    elif escolha_maquina == "TESOURA" and escolha_usuario == "PEDRA":
        print(f"Você ganhou! A máquina escolheu {escolha_maquina}.")
        break 
    elif escolha_maquina == "TESOURA" and escolha_usuario == "PAPEL":
        print(f"Você perdeu! A máquina escolheu {escolha_maquina}.") 
    else:
        print("A opção está incorreta")
        continue 
    valor = valor + valor_ficha    
print(f"Você tem que pagar R${valor + valor_ficha}")