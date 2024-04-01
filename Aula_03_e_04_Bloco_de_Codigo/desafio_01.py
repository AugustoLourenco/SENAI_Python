from random import randint

print("Este é um jogo que te desafia a adivinhar um número aleatório de 0 a 5")

numero_aleatorio = randint(0,5)
numero_usuario = int(input("Tente adivinhar qual número o computador escolheu: "))

if numero_usuario == numero_aleatorio :
    print("Parabéns! Você venceu.")
else :
    print(f"Não foi dessa vez! O número escolhido foi {numero_aleatorio}")